import fitz  # PyMuPDF
from PIL import Image
import io
import base64

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
        base64_images.append(img_base64)
    
    return base64_images

def save_base64_to_txt(base64_images, output_file_prefix):
    for index, base64_string in enumerate(base64_images):
        output_file_path = f"{output_file_prefix}_image_{index + 1}.txt"
        with open(output_file_path, 'w') as file:
            file.write(base64_string)
        print(f"Saved base64 data to {output_file_path}")

# Example usage
pdf_path = "../scripts/pdf_9_new.pdf"
page_number = -1  # Page numbers are zero-based; page 4 is index 3
output_file_prefix = "output_image_base64"

base64_images = pdf_images_to_base64(pdf_path, page_number)
save_base64_to_txt(base64_images, output_file_prefix)
