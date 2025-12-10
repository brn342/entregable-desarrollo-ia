from fastapi import FastAPI
from app.api.ocr_router import router as ocr_router

app = FastAPI(
    title="Proyecto Desarrollo IA - OCR",
    version="1.0.0"
)

app.include_router(ocr_router, prefix="/api")
