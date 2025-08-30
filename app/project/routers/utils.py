import os

def ensure_dir(path: str):
    """
    Ensure that a directory exists. If it does not, create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path
import os
import hashlib

def ensure_dir(path: str):
    """
    Ensure that a directory exists. If it does not, create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def file_size_mb(file_path: str) -> float:
    """
    Get file size in MB.
    """
    if not os.path.exists(file_path):
        return 0.0
    size_bytes = os.path.getsize(file_path)
    return round(size_bytes / (1024 * 1024), 2)  # MB with 2 decimals


def sha256_file(file_path: str) -> str:
    """
    Generate SHA256 hash of a file.
    """
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def is_allowed_extension(filename: str, allowed_extensions: set) -> bool:
    """
    Check if file has an allowed extension.
    Example: allowed_extensions = {"png", "jpg", "jpeg", "pdf"}
    """
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return ext in allowed_extensions






# import os
# import hashlib

# def ensure_dir(path: str):
#     """
#     Ensure that a directory exists. If it does not, create it.
#     """
#     if not os.path.exists(path):
#         os.makedirs(path)
#     return path


# def file_size_mb(file_path: str) -> float:
#     """
#     Get file size in MB.
#     """
#     if not os.path.exists(file_path):
#         return 0.0
#     size_bytes = os.path.getsize(file_path)
#     return round(size_bytes / (1024 * 1024), 2)  # MB with 2 decimals


# def sha256_file(file_path: str) -> str:
#     """
#     Generate SHA256 hash of a file.
#     """
#     sha256 = hashlib.sha256()
#     with open(file_path, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             sha256.update(chunk)
#     return sha256.hexdigest()


# def is_allowed_extension(filename: str, allowed_extensions: list) -> bool:
#     """
#     Check if file has an allowed extension.
#     Example: allowed_extensions = [".apk", ".zip"]
#     """
#     filename = filename.lower()
#     return any(filename.endswith(ext) for ext in allowed_extensions)