import asyncio
from pathlib import Path
import sys
import inspect
from inspect_ai.tool import tool
from inspect_ai.model._chat_message import ChatMessageUser, ChatMessageAssistant, ChatMessageTool, ChatMessageSystem
from inspect_ai.solver import TaskState, Generate
from inspect_ai.util import store
from inspect_ai import Task, eval
from inspect_ai.dataset import Sample
from inspect_ai.solver import solver
from inspect_ai.solver._chain import chain

from multiagent_inspect.core import _trim_messages, TOKEN_ENCODING

sys.path.append(str(Path(__file__).parent.parent))
from multiagent_inspect import SubAgentConfig, init_sub_agents

@tool
def dummy_tool():
    async def execute():
        """Dummy tool, use when being asked to"""
        return "dummy123"
    return execute

async def test_state(state: TaskState):
    tools = state.tools
    assert len(tools) == 3, f"Expected 3 tools, got {len(tools)}"

    specs_str = await tools[0]()
    specs_str = str(specs_str)

    assert "id1" in specs_str and "001" in specs_str, "Agent IDs should be in the specifications"
    assert "Test agent" in specs_str, "Public description should be in the specifications"
    assert "dummy_tool" in specs_str, "Tool name should be in the specifications"

    sig = inspect.signature(tools[1])
    assert "sub_agent_id" in sig.parameters, "run_sub_agent tool should have sub_agent_id parameter"


async def test_chat(state: TaskState):
    tools = state.tools

    question = "Are you ready to do a task for me? If so, answer 'YES' and nothing else."
    result = await tools[2]("id1", question)
    result = str(result)
    assert result.lower() == "yes", "Chat logic failed"

    agent1 = store().get("sub_agents", {}).get("id1")
    assert agent1 is not None, "Agent id1 not found"

    assert len(agent1.messages) == 3, "Agent should have 3 messages"
    assert type(agent1.messages[1]) == ChatMessageUser, "Second message should be a user message"
    assert type(agent1.messages[2]) == ChatMessageAssistant, "Third message should be an assistant message"
    assert agent1.messages[1].content == question, "User message should be the question"
    assert agent1.messages[2].content.lower() == "yes", "Assistant message should be 'yes'"

async def test_run(state: TaskState):
    tools = state.tools

    await tools[1]("id1", "Start by saying exactly 'I accept the task'. Then use the dummy tool and then end the run immediately (stop reason is the output of the dummy tool).")

    agent1 = store().get("sub_agents", {}).get("id1")
    assert agent1 is not None, "Agent id1 not found"

    tool_count = 0
    for msg in agent1.messages:
        if type(msg) == ChatMessageTool:
            if tool_count == 0:
                assert msg.text == "dummy123", "First tool call should be the dummy tool"
            elif tool_count == 1:
                assert msg.function == "_end_run", "Second tool call should be the end run tool"
                assert "dummy123" in msg.text, "End run tool should contain the output of the dummy tool"
            tool_count += 1

async def test_trim_messages_removes(state: TaskState):
    sys_msg = ChatMessageSystem(content="S" * 50)
    user_msg1 = ChatMessageUser(content="U" * 100)
    asst_msg1 = ChatMessageAssistant(content="A" * 100)
    user_msg2 = ChatMessageUser(content="U" * 100)
    messages = [sys_msg, user_msg1, asst_msg1, user_msg2]
    sys_tokens = len(TOKEN_ENCODING.encode(sys_msg.text))
    rest_tokens = sum(len(TOKEN_ENCODING.encode(m.text)) for m in messages[1:])
    max_tokens = sys_tokens + rest_tokens - 10
    
    trimmed = _trim_messages(messages.copy(), max_tokens)
    trimmed_total = sum(len(TOKEN_ENCODING.encode(m.text)) for m in trimmed)
    assert trimmed_total <= max_tokens, f"Trimmed total tokens {trimmed_total} exceeds max_tokens {max_tokens}"
    assert len(trimmed) < len(messages), "Expected some messages to be trimmed"
    assert trimmed[0].text == sys_msg.text, "System message must be preserved"
    assert trimmed[1].text != user_msg1.text, "User message should be trimmed"

async def test_trim_messages_no_removal(state: TaskState):
    sys_msg = ChatMessageSystem(content="Hello system")
    user_msg = ChatMessageUser(content="Hello user")
    messages = [sys_msg, user_msg]
    total_tokens = sum(len(TOKEN_ENCODING.encode(m.text)) for m in messages)
    max_tokens = total_tokens + 10  # Allow room so nothing is trimmed
    trimmed = _trim_messages(messages.copy(), max_tokens)
    assert trimmed == messages, "Messages should not be removed if under limit"

async def test_tool_first_message_removed(state: TaskState):
    from inspect_ai.model._chat_message import ChatMessageTool
    sys_msg = ChatMessageSystem(content="System message")
    tool_msg = ChatMessageTool(content="Tool message", function="dummy_tool")
    user_msg = ChatMessageUser(content="User message")
    messages = [sys_msg, tool_msg, user_msg]
    # Set max_tokens high enough so token count is not the driving factor.
    max_tokens = sum(len(TOKEN_ENCODING.encode(m.text)) for m in messages) + 100
    trimmed = _trim_messages(messages.copy(), max_tokens)
    assert len(trimmed) == 2, "Expected the tool message to be removed, only system and user message should remain."
    assert not isinstance(trimmed[1], ChatMessageTool), "The first message after system should not be a tool call."
    assert trimmed[1].text == user_msg.text, "After removal, user message should follow system message."

async def test_multiple_tool_calls_removed(state: TaskState):
    from inspect_ai.model._chat_message import ChatMessageTool
    sys_msg = ChatMessageSystem(content="System")
    tool_msg1 = ChatMessageTool(content="Tool1", function="dummy_tool")
    tool_msg2 = ChatMessageTool(content="Tool2", function="dummy_tool")
    user_msg = ChatMessageUser(content="User")
    messages = [sys_msg, tool_msg1, tool_msg2, user_msg]
    # Set max_tokens high enough so token count is not the driving factor.
    max_tokens = sum(len(TOKEN_ENCODING.encode(m.text)) for m in messages) + 100
    trimmed = _trim_messages(messages.copy(), max_tokens)
    # We expect that both tool messages are removed, leaving only system and user messages.
    assert len(trimmed) == 2, "Expected both tool messages to be removed, leaving system and user messages."
    assert trimmed[0].text == sys_msg.text, "System message must be preserved"
    assert trimmed[1].text == user_msg.text, "User message should follow system message after removing tool messages"

@solver
def test_solver():
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        unit_test_fn = state.metadata["test_fn"]
        await unit_test_fn(state)
        print(f"Test {state.metadata['test_fn'].__name__} passed")
        return state

    return solve

if __name__ == "__main__":
    all_tests = [
        test_state,
        test_chat,
        test_run,
        test_trim_messages_removes,
        test_trim_messages_no_removal,
        test_tool_first_message_removed,
        test_multiple_tool_calls_removed
    ]

    dataset = []
    for test_fn in all_tests:
        dataset.append(Sample(input=test_fn.__name__, metadata={"test_fn": test_fn}))
    
    agent1 = SubAgentConfig(agent_id="id1", tools=[dummy_tool()], public_description="Test agent")
    agent2 = SubAgentConfig()
    solver = chain([init_sub_agents([agent1, agent2]), test_solver()])
    
    task = Task(dataset=dataset, solver=solver, epochs=2)

    eval(task, model="openai/gpt-4o-mini")