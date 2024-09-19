import pdfplumber
import base64
import io
import json
from PIL import Image

# File paths
pdf_path = "../scripts/pdf_2_old.pdf"
output_json_path = "output_images_base64.json"

# Dictionary to store image data
image_data = {}

# Open the PDF using pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]  # Get the first page

    # Extract images from the first page
    images = first_page.images

    for idx, img in enumerate(images):
        # Get the bounding box of the image
        x0, y0, x1, y1 = img["x0"], img["top"], img["x1"], img["bottom"]

        # Extract the cropped region using within_bbox
        cropped_image = first_page.within_bbox((x0, y0, x1, y1)).to_image()

        # Convert the image to a PIL object
        pil_image = cropped_image.original

        # Convert the image to bytes
        buffer = io.BytesIO()
        pil_image.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()

        # Encode the image to base64
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

        # Assign to dictionary (assuming first is photo and second is signature)
        if idx == 0:
            image_data["photo"] = img_base64
        elif idx == 1:
            image_data["signature"] = img_base64

# Save the image data in JSON format
with open(output_json_path, 'w') as json_file:
    json.dump(image_data, json_file, indent=4)

print(f"Images extracted and saved as Base64 in {output_json_path}")
