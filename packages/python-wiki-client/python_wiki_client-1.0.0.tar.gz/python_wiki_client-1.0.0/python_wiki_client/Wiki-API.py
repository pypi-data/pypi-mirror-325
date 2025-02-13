import requests
import aiohttp

class WikiAPI:
    def __init__(self, base_url="https://open.wiki-api.ir"):
        self.base_url = base_url.rstrip('/')
    
    def request(self, endpoint: str, params=None):
        if params is None:
            params = {}
        
        url = f"{self.base_url}/{endpoint.strip('/')}"
        
        try:
            response = requests.get(url, params=params)
            return {
                'status_code': response.status_code,
                'body': response.text
            }
        except requests.exceptions.RequestException as e:
            return {
                'status_code': e.response.status_code if e.response else None,
                'body': str(e)
            }

class WikiAPIAsync:
    def __init__(self, base_url="https://open.wiki-api.ir"):
        self.base_url = base_url.rstrip('/')
    
    async def request(self, endpoint: str, params=None):
        if params is None:
            params = {}
        
        url = f"{self.base_url}/{endpoint.strip('/')}"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    body = await response.text()
                    return {
                        'status_code': response.status,
                        'body': body
                    }
        except aiohttp.ClientError as e:
            return {
                'status_code': None,
                'body': str(e)
            }