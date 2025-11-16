import requests


class FetchService:
    def get_data(self, url: str):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            return response.json()
            

        except Exception:
            return {"status": "offline", "value": 0}
