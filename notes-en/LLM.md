# LLM & AI Agent

## Transformer

- See [Machine_Learning.Transformer](Machine%20Learning.md#transformer)

The Transformer architecture includes an encoder and a decoder, with three possible variations:
1. **Encoder-only** structure.
2. **Decoder-only** structure (e.g., GPT).
3. **Full structure** with both encoder and decoder.

GPT uses the **decoder-only** structure.  
The core of Transformer is the **Attention** mechanism, which differs from other NLP models (e.g., RNN, LSTM). Traditional models struggle with long sequences due to limitations in information passing, leading to the loss of earlier information. The **Attention** mechanism allows the model to focus on different parts of the sequence, improving its ability to handle long-range dependencies.

Reference: [Transformer Detailed Explanation](https://zhuanlan.zhihu.com/p/607423406)

## Chain of Thoughts

## ReAct
Reasoning + Acting

## Agent Harness

## KV Cache

## LangChain
### Dynamic Tools
    - Utilise Middlewware
``` python
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from typing import Callable

@wrap_model_call
def state_based_tools(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse]
) -> ModelResponse:
    """Filter tools based on conversation State."""
    # Read from State: check if user has authenticated
    state = request.state
    is_authenticated = state.get("authenticated", False)
    message_count = len(state["messages"])

    # Only enable sensitive tools after authentication
    if not is_authenticated:
        tools = [t for t in request.tools if t.name.startswith("public_")]
        request = request.override(tools=tools)
    elif message_count < 5:
        # Limit tools early in conversation
        tools = [t for t in request.tools if t.name != "advanced_search"]
        request = request.override(tools=tools)

    return handler(request)

agent = create_agent(
    model="gpt-5.4",
    tools=[public_search, private_search, advanced_search],
    middleware=[state_based_tools]
)
```

### Error Handling
``` Python
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage


@wrap_tool_call
def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return handler(request)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"]
        )

agent = create_agent(
    model="gpt-5.4",
    tools=[search, get_weather],
    middleware=[handle_tool_errors]
)
```

### Response Format
https://docs.langchain.com/oss/python/langchain/structured-output
- Suggested Followed Queriess
    ```python
    class ResponseWithSuggestions(BaseModel):
        answer: str = Field(description="The answer of the query")
        follow_ups: list[str] = Field(description="Three suggested follow-up queries", max_items=3)
    ```
- Pydantic
    ```python
    from pydantic import BaseModel, Field

    class Movie(BaseModel):
        """A movie with details."""
        title: str = Field(description="The title of the movie")
        year: int = Field(description="The year the movie was released")
        director: str = Field(description="The director of the movie")
        rating: float = Field(description="The movie's rating out of 10")

    model_with_structure = model.with_structured_output(Movie)
    response = model_with_structure.invoke("Provide details about the movie Inception")
    print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)
    ```

### Messages
```python
from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

messages = [
    SystemMessage("You are a poetry expert"),
    HumanMessage("Write a haiku about spring"),
    AIMessage("Cherry blossoms bloom...")
]
response = model.invoke(messages)
```