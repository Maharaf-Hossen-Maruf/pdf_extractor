import fitz  # PyMuPDF
import pytesseract
from PIL import Image, ImageEnhance, ImageOps
import io
import cv2
import numpy as np
import re

# Define the path to your PDF file
pdf_path = "../scripts/pdf_1_old.pdf"
output_file_path = "./cleaned_new_1.txt"

# Function to preprocess image for better OCR results
def preprocess_image(img):
    # Convert to grayscale
    img = ImageOps.grayscale(img)
    
    # Convert to OpenCV format
    img_cv = np.array(img)

    # Apply thresholding
    _, img_cv = cv2.threshold(img_cv, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Convert back to PIL format
    img = Image.fromarray(img_cv)
    
    return img

# Function to convert a PDF page to an image, preprocess it, and then apply OCR
def pdf_to_ocr_improved(pdf_path, output_file_path):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    text=""
    
    # Open the output file to write
    with open(output_file_path, 'w', encoding='utf-8') as f:
        # Iterate over each page
        for page_num in range(len(pdf_document)):
            # Get the page
            page = pdf_document.load_page(page_num)
            
            # Convert page to an image (using zoom for higher resolution)
            zoom = 3.0  # Increase zoom for better quality
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            # Convert pixmap to PIL Image
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Preprocess the image
            img = preprocess_image(img)
            
            # Perform OCR with improved settings
            custom_config = r'--oem 3 --psm 6'  # Using Tesseract's default OCR engine with a page segmentation mode suitable for a uniform block of text
            text += pytesseract.image_to_string(img, config=custom_config, lang="eng+ben")  # English and Bengali
            
            # Write the extracted text to the output file (row-wise)
            # f.write(f"Page {page_num + 1} Text:\n")
            # f.write(text + "\n\n")
    
    return text

# Run the improved OCR function and write to output file
text = pdf_to_ocr_improved(pdf_path, output_file_path)

# Return the path of the output text file
output_file_path

cleaned_text = re.sub(r'\s+', ' ', text).strip()

# Save the cleaned text to a file
output_file_path = "cleaned_new_1.txt"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(cleaned_text)

output_file_path
