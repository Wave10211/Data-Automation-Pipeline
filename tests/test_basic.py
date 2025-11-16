from backend.api.fetch_services import FetchService

def test_fetcher_returns_dict(monkeypatch):
    class DummyResp:
        def raise_for_status(self): pass
        def json(self): return {"id":1}
    def fake_get(*args, **kwargs): return DummyResp()

    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    svc = FetchService()
    assert isinstance(svc.get_data("http://x"), dict)
