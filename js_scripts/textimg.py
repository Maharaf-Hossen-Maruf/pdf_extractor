import fitz  # PyMuPDF
from PIL import Image
import io
import base64
import json

def pdf_images_to_base64(pdf_path, page_number):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Load the specified page
    page = pdf_document.load_page(page_number)
    
    # Extract images from the page
    image_list = page.get_images(full=True)
    
    base64_images = []
    
    if not image_list:
        raise ValueError("No images found on the page.")
    
    for i, img in enumerate(image_list):
        xref = img[0]
        
        # Get the image bytes
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        
        # Convert image bytes to a Pillow Image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Save image to a bytes buffer
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")  # You can also use other formats
        
        # Encode the image to base64
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        base64_images.append({"image_index": i + 1, "base64_data": img_base64})
    
    return base64_images

def save_base64_to_json(base64_images, output_file_path):
    # Save the list of base64 images to a JSON file
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(base64_images, json_file, ensure_ascii=False, indent=4)
    print(f"Saved base64 data to {output_file_path}")

# Example usage
pdf_path =  "../scripts/pdf_9_new.pdf"
page_number = -1  # Page numbers are zero-based; page 4 is index 3
output_json_file = "output_images_base64.json"

base64_images = pdf_images_to_base64(pdf_path, page_number)
save_base64_to_json(base64_images, output_json_file)
