"""hw5 using FastApi."""

import requests
from fastapi import FastAPI

app = FastAPI()


async def get_response(number):
    """
    Get response from server.

    Args:
        number: number for request.

    Returns:
        requests.get response to this url.
    """
    url = 'https://jsonplaceholder.typicode.com/todos/{0}'.format(number)
    return requests.get(url)


@app.get('/todo/{number}')
async def get(number: int):
    """
    Answer to a GET request with path /todo/number.

    Args:
        number: number for request

    Returns:
        Dictionary with status code, headers and result of request
    """
    response = await get_response(number)
    return {
        'status code': response.status_code,
        'headers': response.headers,
        'result': response.json(),
    }
