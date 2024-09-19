import os
import pytesseract
from pdf2image import convert_from_path

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/5/'

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Convert PDF to images
images = convert_from_path('./pypdf.pdf')

# Extract text from images
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang='ben')
    print(f"Page {i + 1}:")
    print(text)
    print("-" * 40)
