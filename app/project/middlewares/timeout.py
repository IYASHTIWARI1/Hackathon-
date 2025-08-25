from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import PlainTextResponse
import asyncio

class TimeoutMiddleware(BaseHTTPMiddleware):
    def _init_(self, app, timeout: int = 15):
        super()._init_(app)
        self.timeout = timeout

    async def dispatch(self, request, call_next):
        try:
            return await asyncio.wait_for(call_next(request), timeout=self.timeout)
        except asyncio.TimeoutError:
            return PlainTextResponse("Request timed out", status_code=504)