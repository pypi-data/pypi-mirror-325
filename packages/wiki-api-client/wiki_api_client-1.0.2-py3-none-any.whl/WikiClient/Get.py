MAIN_URL = "https://open.wiki-api.ir"

class AsyncAPI:

    def __init__(self):
        if not self.__check_version():
            raise Exception("Error: This project requires Python 3.6 or higher.")

    def __check_version(self):
        import sys
        return sys.version_info >= (3, 6)

    async def request(self, endpoint, params=None):
        if params is None:
            params = {}

        import aiohttp

        url = f"{MAIN_URL}/{endpoint.strip('/')}"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, params=params) as response:
                    response.raise_for_status()
                    status = response.status
                    data = await response.json()
                    return {
                        'status_code': status,
                        'body': data,
                    }
            except aiohttp.ClientError as e:
                return {
                    'status_code': e.status if hasattr(e, 'status') else None,
                    'body': str(e),
                }

class SyncAPI:
    
    def __init__(self):
        if not self.__check_version():
            raise Exception("Error: This project requires Python 3.6 or higher.")

    def __check_version(self):
        import sys
        return sys.version_info >= (3, 6)

    def request(self, endpoint, params=None):
        if params is None:
            params = {}

        import requests

        url = f"{MAIN_URL}/{endpoint.strip('/')}"

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                'status_code': response.status_code,
                'body': data,
            }
        except requests.exceptions.RequestException as e:
            return {
                'status_code': e.response.status_code if e.response else None,
                'body': str(e),
            }
