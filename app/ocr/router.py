from fastapi import APIRouter, UploadFile, File
from .service import OCRService

router = APIRouter()
service = OCRService()


@router.post("/extract")
async def extract(image: UploadFile = File(...)):
    return await service.extract_text(image)
