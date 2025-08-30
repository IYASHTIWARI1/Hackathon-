from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/upload", tags=["Upload"])

ALLOWED_TYPES = {"image/png", "image/jpeg", "application/pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="File type not allowed")

    data = await file.read()
    if len(data) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large")

    return {"filename": file.filename, "size": len(data)}
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Allowed extensions
    allowed_extensions = [".apk", ".zip"]

    # Check extension
    filename = file.filename.lower()
    if not any(filename.endswith(ext) for ext in allowed_extensions):
        raise HTTPException(status_code=400, detail="Only APK and ZIP files are allowed")

    # Save the file
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())

    return {"filename": file.filename, "message": "File uploaded successfully!"}
# app/routes.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from .utils import ensure_dir, file_size_mb, sha256_file, is_allowed_extension
from .security import max_file_size_mb, allowed_extensions

router = APIRouter()

UPLOAD_DIR = "uploads"
ensure_dir(UPLOAD_DIR)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename

    # ✅ Step 23: extension check
    # if not is_allowed_extension(filename, allowed_extensions):
    #     raise HTTPException(status_code=400, detail="Only APK and ZIP files are allowed")

    # ✅ Step 23: extension + content-type check
    if not is_allowed_extension(filename, allowed_extensions):
        raise HTTPException(status_code=400, detail=f"Invalid extension: {filename}. Only APK/ZIP allowed")

    if file.content_type not in ["application/vnd.android.package-archive", "application/zip", "application/octet-stream"]:
        raise HTTPException(status_code=400, detail=f"Invalid content-type: {file.content_type}. Only APK/ZIP allowed")

    save_path = os.path.join(UPLOAD_DIR, filename)

    # Save file
    with open(save_path, "wb") as buffer:
        buffer.write(await file.read())

    # ✅ Step 24: no dynamic execution
    # Sirf static checks karna, run/install nahi karna
    if file_size_mb(save_path) > max_file_size_mb:
        raise HTTPException(status_code=400, detail="File too large")

    file_hash = sha256_file(save_path)

    return {
        "filename": filename,
        "sha256": file_hash,
        "message": "File uploaded safely (not executed)"
    }
from .utils import ensure_dir, file_size_mb, sha256_file, is_allowed_extension

UPLOAD_DIR = ensure_dir("uploads/")

def save_upload(file):
    # check extension
    if not is_allowed_extension(file.filename, {"png", "jpg", "pdf"}):
        return {"error": "File type not allowed"}

    # save path
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {
        "filename": file.filename,
        "size_mb": file_size_mb(file_path),
        "sha256": sha256_file(file_path)
    }
import os
from fastapi import UploadFile, HTTPException
from .utils import ensure_dir, file_size_mb, sha256_file, is_allowed_extension
from routers.security import max_file_size_mb, allowed_extensions

UPLOAD_DIR = ensure_dir("uploads/")

def save_upload(file: UploadFile):
    # check extension
    if not is_allowed_extension(file.filename, allowed_extensions):
        raise HTTPException(status_code=400, detail="File type not allowed")

    # save path
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # check size
    size = file_size_mb(file_path)
    if size > max_file_size_mb:
        os.remove(file_path)  # delete file if too large
        raise HTTPException(status_code=400, detail=f"File too large (>{max_file_size_mb} MB)")
    
    

    return {
        "filename": file.filename,
        "size_mb": size,
        "sha256": sha256_file(file_path)
    }