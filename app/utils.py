import hashlib, os, tempfile

def save_temp(data: bytes, filename: str = "upload.apk") -> str:
    fd, path = tempfile.mkstemp(prefix="apk_", suffix=".apk")
    with os.fdopen(fd, "wb") as f:
        f.write(data)
    return path

def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()