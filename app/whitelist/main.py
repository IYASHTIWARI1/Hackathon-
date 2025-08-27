import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.analyzer.core import analyze_apk   # <- aapka analyzer function

# Create FastAPI app
app = FastAPI(
    title="APK Detector",
    description="Detect fake APKs",
    version="1.0.0"
)

# Upload folder path
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Root endpoint (check API is running)
@app.get("/")
async def root():
 return {"message": "APK Detector API is running!"}

# Upload endpoint
@app.post("/upload_apk/")
async def upload_apk(file: UploadFile = File(...)):
    if not file.filename.endswith(".apk"):
        raise HTTPException(status_code=400, detail="Only APK files are allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Analyze APK
    try:
        result = analyze_apk(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    return {"filename": file.filename, "analysis": result}


from project.routers import upload_routes   # <- yeh import karna zaroori hai


# router include karo
app.include_router(upload_routes.router)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# agar banks.json white_list ke andar hai
BANKS_FILE = os.path.join(BASE_DIR, "white_list", "banks.json")

with open(BANKS_FILE, "r", encoding="utf-8") as f:
    data = f.read()
    import os
from starlette.staticfiles import StaticFiles

BASE_DIR = os.path.dirname(os.path.abspath_(__file__))   # yeh app/project ka path hai

# ek level upar jaake app/static/ ko point karo
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")
STATIC_DIR = os.path.abspath(STATIC_DIR)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")