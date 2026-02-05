---
name: openai-agents
description: Explains using OpenAI Agents SDK"
---

# OpenAI Agents SDK

The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent AI workflows in Python. It provides a production-ready solution for creating agents that can use tools, hand off tasks to other agents, validate inputs/outputs with guardrails, and maintain conversation state through sessions. The SDK is provider-agnostic, supporting OpenAI's Responses and Chat Completions APIs, as well as 100+ other LLMs through LiteLLM integration.

The core primitives include Agents (LLMs with instructions, tools, and configuration), Handoffs (delegating tasks between agents), Guardrails (input/output validation), Sessions (conversation history management), and Tracing (built-in debugging and monitoring). These primitives combine with Python's native features to express complex workflows without steep learning curves, while built-in tracing enables visualization, debugging, evaluation, and fine-tuning of your agent applications.

## Installation

```bash
uv add openai-agents
# For voice support:
uv add 'openai-agents[voice]'
# For Redis session support:
uv add 'openai-agents[redis]'
```

---

## Agent

Creates an AI agent configured with instructions, tools, guardrails, handoffs, and model settings. Agents are the fundamental building blocks that process inputs, invoke tools, and produce outputs.

```python
from agents import Agent, Runner
from pydantic import BaseModel

# Basic agent with string output
basic_agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant that answers questions concisely.",
)

result = Runner.run_sync(basic_agent, "What is the capital of France?")
print(result.final_output)  # "Paris"

# Agent with structured output using Pydantic
class WeatherResponse(BaseModel):
    city: str
    temperature: int
    conditions: str

weather_agent = Agent(
    name="Weather Agent",
    instructions="Provide weather information in the requested format.",
    output_type=WeatherResponse,
    model="gpt-4o",
)

result = Runner.run_sync(weather_agent, "What's the weather in Tokyo?")
weather = result.final_output_as(WeatherResponse)
print(f"{weather.city}: {weather.temperature}F, {weather.conditions}")

# Agent with dynamic instructions
def get_instructions(ctx, agent):
    user_name = ctx.context.get("user_name", "Guest")
    return f"You are helping {user_name}. Be friendly and helpful."

dynamic_agent = Agent(
    name="Personalized Assistant",
    instructions=get_instructions,
)
```

---

## Runner.run

Executes an agent workflow asynchronously, handling the agent loop including tool calls, handoffs, and final output generation. Returns a RunResult containing all inputs, outputs, and metadata.

```python
import asyncio
from agents import Agent, Runner, RunConfig

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
)

async def main():
    # Basic async run
    result = await Runner.run(agent, "Hello, how can you help me?")
    print(result.final_output)

    # Run with custom configuration
    result = await Runner.run(
        agent,
        input="Explain quantum computing",
        max_turns=5,  # Limit agent loop iterations
        run_config=RunConfig(
            workflow_name="Explanation workflow",
            trace_include_sensitive_data=False,
        ),
    )

    # Access run metadata
    print(f"Final agent: {result.last_agent.name}")
    print(f"Total items: {len(result.new_items)}")
    print(f"Raw responses: {len(result.raw_responses)}")

    # Convert result to input for continuation
    next_input = result.to_input_list()
    continuation = await Runner.run(agent, next_input + [{"role": "user", "content": "Tell me more"}])

asyncio.run(main())
```

---

## Runner.run_sync

Executes an agent workflow synchronously, wrapping the async run method. Ideal for scripts and environments without an existing event loop.

```python
from agents import Agent, Runner

agent = Agent(
    name="Math Tutor",
    instructions="You help with math problems. Show your work step by step.",
)

# Simple synchronous execution
result = Runner.run_sync(agent, "What is 15% of 240?")
print(result.final_output)

# With max_turns to prevent infinite loops
result = Runner.run_sync(
    agent,
    "Solve: 2x + 5 = 13",
    max_turns=3,
)
print(result.final_output)
# Output: x = 4, with step-by-step explanation
```

---

## Runner.run_streamed

Executes an agent workflow with streaming, returning events as they occur. Enables real-time progress updates and token-by-token output display.

```python
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, ItemHelpers

agent = Agent(
    name="Storyteller",
    instructions="You tell engaging short stories.",
)

async def main():
    result = Runner.run_streamed(agent, "Tell me a story about a brave robot.")

    # Stream text token by token
    async for event in result.stream_events():
        if event.type == "raw_response_event":
            if isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)
        elif event.type == "agent_updated_stream_event":
            print(f"\n[Agent changed to: {event.new_agent.name}]")
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print(f"\n[Tool called: {event.item.raw_item.name}]")
            elif event.item.type == "message_output_item":
                print(f"\n[Message: {ItemHelpers.text_message_output(event.item)}]")

    # Access final result after streaming completes
    print(f"\nFinal output: {result.final_output}")

asyncio.run(main())
```

---

## function_tool

Decorator that converts any Python function into a tool usable by agents. Automatically extracts name, description, and parameter schema from the function signature and docstring.

```python
from agents import Agent, Runner, function_tool, RunContextWrapper
from typing import Any
from pydantic import BaseModel

# Simple function tool
@function_tool
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The name of the city to get weather for.
    """
    # In production, call a real weather API
    return f"The weather in {city} is sunny, 72F"

# Tool with context access
@function_tool
def get_user_info(ctx: RunContextWrapper[dict], user_id: str) -> str:
    """Retrieve user information from the context.

    Args:
        user_id: The user's unique identifier.
    """
    users = ctx.context.get("users", {})
    return users.get(user_id, "User not found")

# Async tool with complex types
class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

@function_tool
async def search_web(query: str, max_results: int = 5) -> list[SearchResult]:
    """Search the web for information.

    Args:
        query: The search query.
        max_results: Maximum number of results to return.
    """
    # Simulated search results
    return [SearchResult(title=f"Result for {query}", url="https://example.com", snippet="...")]

# Tool with custom name and error handling
@function_tool(name_override="calculate", failure_error_function=lambda ctx, e: f"Calculation error: {e}")
def calculator(expression: str) -> float:
    """Evaluate a mathematical expression safely."""
    return eval(expression, {"__builtins__": {}}, {})

agent = Agent(
    name="Assistant",
    instructions="Use tools to help answer questions.",
    tools=[get_weather, get_user_info, search_web, calculator],
)

result = Runner.run_sync(agent, "What's the weather in New York?")
print(result.final_output)
```

---

## Handoffs

Enables agents to delegate tasks to specialized sub-agents. Handoffs appear as tools to the LLM and transfer control of the conversation when invoked.

```python
import asyncio
from agents import Agent, Runner, handoff, RunContextWrapper
from pydantic import BaseModel

# Specialized agents
billing_agent = Agent(
    name="Billing Agent",
    handoff_description="Handles billing inquiries, payments, and invoices",
    instructions="You are a billing specialist. Help with payment and invoice questions.",
)

tech_support_agent = Agent(
    name="Tech Support Agent",
    handoff_description="Handles technical issues and troubleshooting",
    instructions="You are a technical support specialist. Help diagnose and fix issues.",
)

# Handoff with input data
class EscalationInfo(BaseModel):
    reason: str
    priority: str

async def on_escalate(ctx: RunContextWrapper, data: EscalationInfo):
    print(f"Escalation: {data.reason} (Priority: {data.priority})")

escalation_agent = Agent(
    name="Escalation Agent",
    instructions="Handle escalated issues with care.",
)

# Triage agent with handoffs
triage_agent = Agent(
    name="Triage Agent",
    instructions="""You are a customer service triage agent.
    Route customers to the appropriate specialist based on their needs.
    - Billing issues -> Billing Agent
    - Technical problems -> Tech Support Agent
    - Urgent matters -> Escalation Agent""",
    handoffs=[
        billing_agent,  # Simple handoff
        tech_support_agent,
        handoff(
            escalation_agent,
            on_handoff=on_escalate,
            input_type=EscalationInfo,
            tool_name_override="escalate_to_manager",
            tool_description_override="Escalate urgent issues to a manager",
        ),
    ],
)

async def main():
    result = await Runner.run(
        triage_agent,
        "I was charged twice for my subscription last month!"
    )
    print(f"Handled by: {result.last_agent.name}")
    print(f"Response: {result.final_output}")

asyncio.run(main())
```

---

## Guardrails

Validates agent inputs and outputs using configurable checks. Input guardrails run before/alongside agent execution; output guardrails validate final responses before returning.

```python
import asyncio
from pydantic import BaseModel
from agents import (
    Agent, Runner, GuardrailFunctionOutput, InputGuardrail,
    InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered,
    RunContextWrapper, TResponseInputItem, input_guardrail, output_guardrail
)

# Input guardrail using an agent
class ContentCheck(BaseModel):
    is_appropriate: bool
    reason: str

check_agent = Agent(
    name="Content Checker",
    instructions="Check if the input is appropriate and not harmful.",
    output_type=ContentCheck,
)

@input_guardrail
async def content_filter(
    ctx: RunContextWrapper, agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(check_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_appropriate,
    )

# Blocking guardrail (runs before agent starts)
blocking_guardrail = InputGuardrail(
    guardrail_function=content_filter,
    run_in_parallel=False,  # Blocks agent until complete
)

# Output guardrail
class OutputCheck(BaseModel):
    contains_pii: bool

output_check_agent = Agent(
    name="PII Checker",
    instructions="Check if the output contains personally identifiable information.",
    output_type=OutputCheck,
)

@output_guardrail
async def pii_filter(ctx: RunContextWrapper, agent: Agent, output: str) -> GuardrailFunctionOutput:
    result = await Runner.run(output_check_agent, output, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_pii,
    )

# Agent with guardrails
protected_agent = Agent(
    name="Protected Assistant",
    instructions="You are a helpful assistant.",
    input_guardrails=[blocking_guardrail],
    output_guardrails=[pii_filter],
)

async def main():
    try:
        result = await Runner.run(protected_agent, "What's the weather today?")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print(f"Input blocked: {e.guardrail_result.output.output_info}")
    except OutputGuardrailTripwireTriggered as e:
        print(f"Output blocked: {e.guardrail_result.output.output_info}")

asyncio.run(main())
```

---

## Sessions

Provides automatic conversation history management across multiple agent runs. Eliminates manual handling of message history between turns.

```python
import asyncio
from agents import Agent, Runner, SQLiteSession

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant. Remember previous context.",
)

async def main():
    # SQLite session (persists to file)
    session = SQLiteSession("user_123", "conversations.db")

    # First turn
    result = await Runner.run(
        agent,
        "My name is Alice and I love hiking.",
        session=session,
    )
    print(f"Turn 1: {result.final_output}")

    # Second turn - agent remembers context
    result = await Runner.run(
        agent,
        "What's my name and hobby?",
        session=session,
    )
    print(f"Turn 2: {result.final_output}")
    # Output: "Your name is Alice and you love hiking."

    # Different session = different conversation
    other_session = SQLiteSession("user_456", "conversations.db")
    result = await Runner.run(
        agent,
        "What's my name?",
        session=other_session,
    )
    print(f"New session: {result.final_output}")
    # Output: "I don't know your name yet."

asyncio.run(main())

# Custom session implementation
from agents.memory import Session
from typing import List

class CustomSession:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self._items: List[dict] = []

    async def get_items(self, limit: int | None = None) -> List[dict]:
        return self._items[-limit:] if limit else self._items

    async def add_items(self, items: List[dict]) -> None:
        self._items.extend(items)

    async def pop_item(self) -> dict | None:
        return self._items.pop() if self._items else None

    async def clear_session(self) -> None:
        self._items.clear()
```

---

## MCP Server Integration

Integrates Model Context Protocol (MCP) servers to expose external tools and resources to agents. Supports hosted, HTTP, SSE, and stdio transports.

```python
import asyncio
from agents import Agent, Runner, HostedMCPTool
from agents.mcp import MCPServerStdio, MCPServerStreamableHttp, MCPServerManager

# Hosted MCP tool (runs on OpenAI servers)
async def hosted_example():
    agent = Agent(
        name="Git Assistant",
        tools=[
            HostedMCPTool(
                tool_config={
                    "type": "mcp",
                    "server_label": "gitmcp",
                    "server_url": "https://gitmcp.io/openai/codex",
                    "require_approval": "never",
                }
            )
        ],
    )
    result = await Runner.run(agent, "What languages is this repo written in?")
    print(result.final_output)

# stdio MCP server (local subprocess)
async def stdio_example():
    async with MCPServerStdio(
        name="Filesystem",
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/files"],
        },
    ) as server:
        agent = Agent(
            name="File Assistant",
            instructions="Use filesystem tools to help with file operations.",
            mcp_servers=[server],
        )
        result = await Runner.run(agent, "List all files in the directory")
        print(result.final_output)

# HTTP MCP server
async def http_example():
    async with MCPServerStreamableHttp(
        name="API Server",
        params={
            "url": "http://localhost:8000/mcp",
            "headers": {"Authorization": "Bearer token123"},
        },
        cache_tools_list=True,
    ) as server:
        agent = Agent(
            name="API Assistant",
            mcp_servers=[server],
        )
        result = await Runner.run(agent, "Call the API")
        print(result.final_output)

# Multiple MCP servers with manager
async def manager_example():
    servers = [
        MCPServerStreamableHttp(name="calendar", params={"url": "http://localhost:8000/mcp"}),
        MCPServerStreamableHttp(name="docs", params={"url": "http://localhost:8001/mcp"}),
    ]
    async with MCPServerManager(servers) as manager:
        agent = Agent(
            name="Multi-tool Assistant",
            mcp_servers=manager.active_servers,
        )
        result = await Runner.run(agent, "What tools are available?")
        print(result.final_output)

asyncio.run(hosted_example())
```

---

## Tracing

Built-in tracing for debugging, monitoring, and visualizing agent workflows. Captures LLM generations, tool calls, handoffs, and custom events.

```python
import asyncio
from agents import Agent, Runner, trace, custom_span, RunConfig, set_tracing_export_api_key

agent = Agent(name="Assistant", instructions="You are helpful.")

# Higher-level trace wrapping multiple runs
async def main():
    with trace("Customer Support Workflow", group_id="thread_123"):
        # First interaction
        result1 = await Runner.run(agent, "Hello, I need help")

        # Custom span for business logic
        with custom_span("process_request"):
            # Your processing logic here
            processed = result1.final_output.upper()

        # Second interaction in same trace
        result2 = await Runner.run(agent, f"Thanks for: {processed}")

# Configure tracing via RunConfig
async def configured_run():
    result = await Runner.run(
        agent,
        "Hello",
        run_config=RunConfig(
            workflow_name="My Workflow",
            trace_id="trace_abc123def456",  # Custom trace ID
            group_id="conversation_789",     # Group related traces
            trace_include_sensitive_data=False,  # Hide sensitive data
            trace_metadata={"user_id": "123", "version": "1.0"},
        ),
    )

# Disable tracing for a run
async def no_trace_run():
    result = await Runner.run(
        agent,
        "Hello",
        run_config=RunConfig(tracing_disabled=True),
    )

# Use different API key for tracing (e.g., with non-OpenAI models)
set_tracing_export_api_key("sk-your-openai-key")

asyncio.run(main())
```

---

## Agent as Tool

Converts an agent into a callable tool, allowing orchestrator agents to invoke specialized agents without full handoffs. The orchestrator retains control of the conversation.

```python
import asyncio
from agents import Agent, Runner

# Specialized agents
translator_es = Agent(
    name="Spanish Translator",
    instructions="Translate the input text to Spanish. Only output the translation.",
)

translator_fr = Agent(
    name="French Translator",
    instructions="Translate the input text to French. Only output the translation.",
)

summarizer = Agent(
    name="Summarizer",
    instructions="Summarize the input text in 2-3 sentences.",
)

# Orchestrator that uses agents as tools
orchestrator = Agent(
    name="Language Assistant",
    instructions="""You help with language tasks. Use the available tools:
    - translate_spanish: Translate to Spanish
    - translate_french: Translate to French
    - summarize: Create a summary
    You can call multiple tools to fulfill requests.""",
    tools=[
        translator_es.as_tool(
            tool_name="translate_spanish",
            tool_description="Translate text to Spanish",
        ),
        translator_fr.as_tool(
            tool_name="translate_french",
            tool_description="Translate text to French",
        ),
        summarizer.as_tool(
            tool_name="summarize",
            tool_description="Summarize text concisely",
        ),
    ],
)

async def main():
    result = await Runner.run(
        orchestrator,
        "Translate 'Hello, how are you?' to both Spanish and French"
    )
    print(result.final_output)
    # Output includes both Spanish and French translations

asyncio.run(main())
```

---

## Hosted Tools

Built-in OpenAI tools that run on OpenAI's infrastructure, including web search, file search, code interpreter, and image generation.

```python
import asyncio
from agents import Agent, Runner, WebSearchTool, FileSearchTool, CodeInterpreterTool, ImageGenerationTool

# Agent with multiple hosted tools
research_agent = Agent(
    name="Research Assistant",
    instructions="Help users research topics using web search and analyze data.",
    tools=[
        WebSearchTool(),  # Search the web
        FileSearchTool(
            max_num_results=5,
            vector_store_ids=["vs_abc123"],  # Your OpenAI vector store
        ),
        CodeInterpreterTool(),  # Execute Python code
    ],
)

async def main():
    # Web search example
    result = await Runner.run(
        research_agent,
        "What are the latest developments in quantum computing in 2024?"
    )
    print(result.final_output)

    # Code interpreter example
    code_agent = Agent(
        name="Data Analyst",
        instructions="Analyze data and create visualizations using Python.",
        tools=[CodeInterpreterTool()],
    )
    result = await Runner.run(
        code_agent,
        "Calculate the first 20 Fibonacci numbers and show them in a list"
    )
    print(result.final_output)

# Image generation
image_agent = Agent(
    name="Artist",
    instructions="Create images based on user descriptions.",
    tools=[ImageGenerationTool(model="gpt-image-1", size="1024x1024")],
)

asyncio.run(main())
```

---

## RunConfig

Configures global settings for an entire agent run including model selection, tracing, guardrails, and handoff behavior.

```python
import asyncio
from agents import Agent, Runner, RunConfig, InputGuardrail, OutputGuardrail
from agents.models import OpenAIProvider

agent = Agent(name="Assistant", instructions="You are helpful.")

async def main():
    config = RunConfig(
        # Model configuration
        model="gpt-4o",  # Override agent's model
        model_provider=OpenAIProvider(),

        # Tracing configuration
        workflow_name="Customer Support",
        trace_id="trace_custom123",
        group_id="session_456",
        trace_metadata={"environment": "production"},
        trace_include_sensitive_data=True,
        tracing_disabled=False,

        # Global guardrails (in addition to agent's guardrails)
        input_guardrails=[],
        output_guardrails=[],

        # Handoff configuration
        handoff_input_filter=None,  # Custom filter for all handoffs
    )

    result = await Runner.run(
        agent,
        "Hello!",
        run_config=config,
        max_turns=10,
    )
    print(result.final_output)

asyncio.run(main())
```

---

## Summary

The OpenAI Agents SDK enables building sophisticated multi-agent AI applications through its composable primitives. The most common use cases include customer service bots with specialized agents handling different domains (billing, support, sales), research assistants combining web search and document analysis, code generation pipelines with review and testing agents, and conversational AI with persistent memory. The agent loop handles the complexity of tool invocation, result processing, and conversation management automatically.

Integration patterns typically involve creating a triage/orchestrator agent that routes requests to specialized agents via handoffs, using guardrails for input validation and output safety, implementing sessions for multi-turn conversations, and leveraging tracing for debugging and monitoring. The SDK works seamlessly with OpenAI models via the Responses API, but also supports any LLM through the extensible model provider interface, making it suitable for production deployments across diverse infrastructure requirements.