from fastapi import FastAPI
from app.ocr.router import router as ocr_router

app = FastAPI(
    title="SW Campus AI Service",
    description="AI Services for Software Campus (OCR, etc.)",
    version="0.1.0"
)

app.include_router(ocr_router, prefix="/ocr")


@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration"""
    return {"status": "healthy"}
