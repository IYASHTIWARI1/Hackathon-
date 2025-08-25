import asyncio
from starlette.responses import PlainTextResponse

# Max request body size (10 MB)
MAX_BODY_SIZE = 10 * 1024 * 1024

# Concurrency semaphore
sem = asyncio.Semaphore(200)  # max 200 requests parallel

async def body_size_limit(request, call_next):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > MAX_BODY_SIZE:
        return PlainTextResponse("Payload too large", status_code=413)
    return await call_next(request)

async def concurrency_limit(request, call_next):
    async with sem:
        return await call_next(request)