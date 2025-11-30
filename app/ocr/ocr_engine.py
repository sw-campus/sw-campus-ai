from paddleocr import PaddleOCR

_ocr = None

def get_ocr_engine():
    global _ocr
    if _ocr is None:
        _ocr = PaddleOCR(lang="korean")
    return _ocr
