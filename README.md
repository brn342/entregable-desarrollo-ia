# Proyecto de Desarrollo IA – Opción B (OCR con Tesseract)

Este proyecto implementa un microservicio simple en **Python + FastAPI** que recibe una imagen y devuelve el texto extraído utilizando **Tesseract OCR**.
La idea es tener un endpoint limpio, directo y fácil de integrar con cualquier backend que necesite convertir imágenes a texto.

---

## ¿Qué hace este servicio?

* Expone un endpoint **POST /api/ocr/extract**
* Recibe una imagen por `multipart/form-data`
* Procesa la imagen con `pytesseract`
* Devuelve un JSON con:

  * el nombre del archivo
  * el texto extraído

---

## Resumen del flujo (breve y claro)

1. El cliente envía una imagen al endpoint `/api/ocr/extract`.
2. FastAPI valida que sea un archivo de imagen.
3. Se leen los bytes y se pasan al servicio de OCR.
4. Tesseract analiza la imagen y extrae el texto.
5. Se devuelve un JSON con el nombre del archivo y el texto obtenido.
