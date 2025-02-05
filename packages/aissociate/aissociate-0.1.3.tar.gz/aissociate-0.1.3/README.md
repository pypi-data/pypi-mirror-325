# AI:ssociate Python API Library
![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fgitlab.com%2Faissociate%2Faissociate-python%2F-%2Fraw%2Fmain%2Fpyproject.toml%3Fref_type%3Dheads&query=%24.project.version&logo=pypi&logoColor=ffffff&label=aissociate&link=https%3A%2F%2Fpypi.org%2Fproject%2Faissociate%2F)

```aissociate``` is a Python package that provides an interface for interacting with the [AI:ssociate](https://aissociate.at) API. 
It currently only supports asynchronous clients, making it suitable for a variety of use cases. 

## Installation

You can install `aissociate` using `pip` by creating a virtual environment and installing it with 

```sh
pip install aissociate
```


## Prerequisites
- Python >=3.8 installed
- A valid API key (request one by contacting [sales@aissociate.at](mailto:sales@aissociate.at))
- `asyncio` library installed (install using `pip install asyncio`)

## Usage

### Asynchronous Client

AIssociate provides an `AsyncAIssociateClient` for interacting with the streaming API asynchronously. Below is an example of how you can use it:

```python
import asyncio
from aissociate import AsyncAIssociateClient


client = AsyncAIssociateClient(
    api_key="<AISSOCIATE_API_KEY>",
)

async def main():
    stream = client.ask("Fasse die Judikatur des OGH zur Mietzinsminderung in der Covid-Pandemie zusammen.")
    async for event in stream:
        print(event.text, end="")


if __name__ == "__main__":
    asyncio.run(main())
```

Note that instead of explicitly setting the API Key, we recommend setting the ```AISSOCIATE_API_KEY``` as an environment 
variable either by exporting it ```export AISSOCIATE_API_KEY=<your-key>``` or by loading it from the ```.env``` file.

#### Parameters
- `api_key`: Your API key for authentication.
- `base_url`: The base URL of the API server (The default is ```https://aissociate.at```).

## Notes

The provided API key in the script is for demonstration purposes and should be replaced with a valid key.
Ensure that your API key remains confidential and is not shared publicly.

## Troubleshooting

If you receive a 401 Unauthorized response, ensure your API key is correct and active.
If the request times out, check your internet connection and API availability.