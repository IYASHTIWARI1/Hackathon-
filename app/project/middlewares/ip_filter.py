from starlette.responses import PlainTextResponse

# Example IP list
ALLOWED_IPS = {"127.0.0.1", "192.168.1.100"}  # local testing

async def ip_filter(request, call_next):
    client_ip = request.client.host

    # Agar IP allowlist me nahi hai to block
    if ALLOWED_IPS and client_ip not in ALLOWED_IPS:
        return PlainTextResponse("Forbidden", status_code=403)

    return await call_next(request)