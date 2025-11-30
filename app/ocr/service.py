from fastapi import UploadFile
from .ocr_engine import get_ocr_engine
from PIL import Image
import numpy as np
import io

class OCRService:
    async def extract_text(self, file: UploadFile):
        data = await file.read()

        image = Image.open(io.BytesIO(data)).convert("RGB")
        img_np = np.array(image)

        ocr = get_ocr_engine()
        result = ocr.ocr(img_np)

        # PaddleOCR 3.3.2 구조: result = [ { ... } ]
        ocr_out = result[0]
        texts = ocr_out.get("rec_texts", [])
        scores = ocr_out.get("rec_scores", [])

        return {
            "text": "\n".join(texts),
            "lines": texts,
            "scores": scores,
        }
