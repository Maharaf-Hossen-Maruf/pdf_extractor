import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

# Path to the Tesseract executable (customize based on your system)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Function to extract text from images using Tesseract
def extract_text_from_image(image_path):
    # Set language to both Bengali (ben) and English (eng)
    text = pytesseract.image_to_string(Image.open(image_path), lang='ben+eng')
    return text

# Function to convert PDF pages to images and perform OCR
def extract_text_from_pdf(pdf_path, output_txt='new_pdf_1_tes.txt'):
    # Convert PDF pages to images
    pages = convert_from_path(pdf_path, dpi=146)
    
    all_text = ""
    image_folder = "pdf_images"
    os.makedirs(image_folder, exist_ok=True)
    # print("------------------------------There Is Print ---------------------------------------------")

    # Loop over each page and extract text
    for i, page in enumerate(pages):
        image_path = f"{image_folder}/page_{i+1}.jpg"
        page.save(image_path, 'JPEG')

        # Extract text from the current page
        page_text = extract_text_from_image(image_path)
        # for i in page_text:
        #     print(i)

        all_text += page_text + "\n\n"

    # Save the extracted text to a .txt file
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write(all_text)

    return all_text


# Path to your PDF
pdf_path = '../scripts/pdf_3_new.pdf'  # Path to your PDF
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)