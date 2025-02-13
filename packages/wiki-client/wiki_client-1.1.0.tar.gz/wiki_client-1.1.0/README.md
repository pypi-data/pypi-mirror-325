# Python Wiki Client

`python-wiki-client` is a Python package for interacting with the [wiki-api](https://wiki-api.ir) APIs. This package allows you to send GET requests to various URLs, retrieve responses, and work with the Wiki-API endpoints.

## Prerequisites

To use this package, you need to have **Python 3.6 or higher** installed.

## Installation

To install this package via `pip`, run the following command:

### Install via PyPI

```bash
pip install wiki-client
```

## Usage

Once the package is installed, you can use it in your Python project as follows:

### Synchronous Example

```python
from WikiAPI.Sync import WikiAPI

wiki = WikiAPI()

response = wiki.request("apis-1/ChatGPT", {"q": "Hello"})

print(response)
# Output:
# {'status_code': 200, 'body': '{"status": true, "channel": "@Wiki_API", "site": "Wiki-Api.ir", "developers": "@B3dev, @Dumacel", "results": "Hello! How can I assist you today? 😊"}'}
```

### Asynchronous Example

If you want to make requests asynchronously, you can use the asynchronous version of the API:

```python
import asyncio
from WikiAPI.Async import WikiAPI

wiki = WikiAPIAsync()

async def fetch_data():
    response = await wiki.request("apis-1/ChatGPT", {"q": "Hello"})
    print(response)

asyncio.run(fetch_data())
```