from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.ocr_service import extract_text_from_image

router = APIRouter(
    prefix="/ocr",
    tags=["OCR"]
)


@router.post("/extract")
async def extract(file: UploadFile = File(...)):
    """
    Endpoint POST /api/ocr/extract
    Recibe una imagen (multipart/form-data) y devuelve el texto extraído.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")

    try:
        image_bytes = await file.read()
        text = extract_text_from_image(image_bytes)

        return JSONResponse(
            content={
                "filename": file.filename,
                "text": text
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando la imagen: {str(e)}")
