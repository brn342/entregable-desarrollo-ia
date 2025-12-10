from PIL import Image
import pytesseract
from io import BytesIO


def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Recibe una imagen en bytes y devuelve el texto extraído con Tesseract.
    """
    image = Image.open(BytesIO(image_bytes))

    text = pytesseract.image_to_string(image, lang="spa")
    return text.strip()
