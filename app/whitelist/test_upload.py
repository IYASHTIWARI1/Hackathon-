from fastapi import APIRouter, UploadFile, File, HTTPException
import os, shutil, hashlib
from analyzer.core import analyze_apk   # <-- ये सही import होना चाहिए

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload_apk/")
async def upload_apk(file: UploadFile = File(...)):
    # extension check
    if not file.filename.lower().endswith(".apk"):
        raise HTTPException(status_code=400, detail="Only APK files are allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # sha256 निकालो
    with open(file_path, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()

    # APK analysis
    result = analyze_apk(file_path, sha256)

    # final response
    return {
        "filename": file.filename,
        "sha256": sha256,
        **result
    }