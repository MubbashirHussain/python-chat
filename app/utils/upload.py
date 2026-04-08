import os
import shutil
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads/profiles"

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_file(file: UploadFile) -> str | None:
    if not file:
        return None
    
    # Generate unique filename to avoid conflicts
    ext = file.filename.split(".")[-1] if "." in file.filename else ""
    filename = f"{uuid.uuid4().hex}.{ext}" if ext else uuid.uuid4().hex
    
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Return the relative path to be stored in DB
    return f"/{UPLOAD_DIR}/{filename}"
