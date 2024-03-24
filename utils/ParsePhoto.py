import logging
from PIL import Image
from pytesseract import pytesseract

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


def analyze_photo():
    text = extract_text_from_image()
    return f'Текст изображения: {text}'


def extract_text_from_image():
    image_path = r"photo_1.jpg"
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang="rus")
    return text
