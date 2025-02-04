# Zyphra Python Client

A Python client library for interacting with the Zyphra API.

## Installation

```bash
pip install zyphra
```

## Quick Start

```python
from zyphra import ZyphraClient, ModelType

# Initialize the client
client = ZyphraClient(api_key="your-api-key")

# Chat completion example
response = client.chat.completions.create(
    model=ModelType.ZAMBA2_7B,
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Text-to-speech example
audio_data = client.audio.speech.create(
    text="Hello, world!",
    model=ModelType.ZAUDIO
)

# Using async client
async with AsyncZyphraClient(api_key="your-api-key") as client:
    response = await client.chat.completions.create(
        model=ModelType.ZAMBA2_7B,
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
```

## Features

- Supports both synchronous and asynchronous operations
- Chat completions API
- Text-to-speech capabilities
- Built-in type hints and validation
- Streaming support for both chat and audio responses

## Requirements

- Python 3.8+
- `aiohttp` for async operations
- `pydantic` for data validation
- `requests` for synchronous operations

## License

MIT License