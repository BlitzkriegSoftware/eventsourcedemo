# event source demo

A Demo of Event Sourcing in Http and Python

## Server

A simple server in FastAPI (main.py)

```powershell
# .\start-server.ps1
uv run fastapi dev --port 8080
```

## Client

In another terminal session

```powershell
# Curl test (.\start-curl-client.ps1)
curl http://localhost:8080/stream

# In a web page
# Open in a browser "index.html"
# (.\start-page-client.ps1)
```

## References

- [Python SSE](https://towardsdatascience.com/introducing-server-sent-events-in-python/#:~:text=What%20are%20Server%2DSent%20Events,to%20the%20messages%20it%20receives.)
- [UV FastAPI](https://docs.astral.sh/uv/guides/integration/fastapi/)
- [FastAPI CORS](https://fastapi.tiangolo.com/tutorial/cors/)
