from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# CORS is required for clients to consume streams
# These settings are NOT OK in PRODUCTION, 
# Should be in configuration (12-Factor)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Generates a series of events
async def event_generator():
    while True:
        # Format required: "data: <message>\n\n"
        yield f"data: The time is {asyncio.get_event_loop().time()}\n\n"
        await asyncio.sleep(1)

# Endpoint (get)
@app.get("/stream")
async def stream():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
