
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class TesseractOCR():
    def __init__(self) -> None:
        pass

    def extract_text_from_image(file):
        pass


print(pytesseract.image_to_string(Image.open('/Users/arun/Downloads/paper1.jpg')))