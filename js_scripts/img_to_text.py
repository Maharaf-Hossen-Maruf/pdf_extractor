from PIL import Image
import pytesseract

# Optional: Specify the path to the Tesseract executable if not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # For Ubuntu

# Function to extract text from an image
def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Set custom configuration to use both Bangla and English languages
    custom_config = r'--oem 1 --psm 6'  # LSTM-based OCR, treat the image as a block of text

    # Extract text from image (for both Bangla and English)
    text = pytesseract.image_to_string(img, lang='ben+eng', config=custom_config)

    return text

# Specify the path to the image file
image_path = './output/page-0.png'  # Replace with your image path

# Extract the text from the image
extracted_text = extract_text_from_image(image_path)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)

# Optional: Save the extracted text to a file
output_file = 'output_text_old.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(f"Text has been saved to {output_file}")
