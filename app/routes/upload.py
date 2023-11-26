import os
from fastapi import APIRouter, HTTPException, status, UploadFile, Depends
from typing import List
from uuid import uuid4

from app.dependencies import s3_client
from app.utils import token_required

upload_router = APIRouter(
    prefix="/upload",
    dependencies=[Depends(token_required)]
)

S3_BASE_URL = f"https://{os.environ.get('AWS_BUCKET_NAME')}.s3.{os.environ.get('AWS_REGION')}.amazonaws.com/"

@upload_router.post("/")
async def upload_file(files: List[UploadFile]):
    uploaded_files = []

    for file in files:
        unique_filename = str(uuid4()) + "_" + file.filename

        try:
            s3_client.upload_fileobj(file.file, os.environ.get("AWS_BUCKET_NAME"), unique_filename)
        except:
            pass

        file_url = S3_BASE_URL + unique_filename

        uploaded_files.append({"filename": unique_filename, "file_url": file_url})

    return uploaded_files