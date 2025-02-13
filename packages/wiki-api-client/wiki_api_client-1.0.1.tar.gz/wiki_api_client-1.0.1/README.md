# Python Wiki Client

`python-wiki-client` is a Python package for interacting with the [wiki-api](https://wiki-api.ir) APIs. This package allows you to send GET requests to various URLs, retrieve responses, and work with the Wiki-API endpoints.

## Prerequisites

To use this package, you need to have **Python 3.6 or higher** installed.

## Installation

To install this package via `pip`, run the following command:

### Install via PyPI

```bash
pip install wiki-api-client
```

## Usage

Once the package is installed, you can use it in your Python project as follows:

### Synchronous Example

```python
from WikiClient import Get

wiki = Get.SyncAPI()

data = wiki.request(
    'apis-1/ChatGPT-4o', # API address in Wiki-API.ir without domain name
    {'q': 'hello'}       # Required data
)

print(data)

# Output:
# {'status_code': 200, 'body': {'status': True, 'channel': '@Wiki_API', 'site': 'Wiki-Api.ir', 'developers': '@B3dev, @Dumacel', 'results': 'Hi there! How can I help you today? 😊'}}
```

### Asynchronous Example

If you want to make requests asynchronously, you can use the asynchronous version of the API:

```python
from WikiClient import Get

wiki = Get.AsyncAPI()

async def sendReq():
    response = await wiki.request(
        'apis-1/ChatGPT-4o', # API address in Wiki-API.ir without domain name
        {'q': 'hello'}       # Required data
    )
    print(response)

# Output:
# {'status_code': 200, 'body': {'status': True, 'channel': '@Wiki_API', 'site': 'Wiki-Api.ir', 'developers': '@B3dev, @Dumacel', 'results': 'Hi there! How can I help you today? 😊'}}
```