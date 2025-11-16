from fastapi import FastAPI
from backend.api.fetch_services import FetchService

app = FastAPI()

def run_pipeline():
    fetcher = FetchService()

    # endpoint stabil pentru Sprint 1
    data = fetcher.get_data("https://jsonplaceholder.typicode.com/todos/1")

    print("✅ Pipeline executed successfully.")
    print("Payload received:", data)

if __name__ == "__main__":
    run_pipeline()
