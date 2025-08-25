from fastapi import APIRouter, UploadFile, File
import os, shutil

router = APIRouter()

UPLOAD_DIR = "private_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"File '{file.filename}' saved at '{file_location}'"}