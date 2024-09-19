import pdfplumber

from regExp import new_pattern
from regExp_old import old_pattern
# File path to the PDF
pdf_path = "../scripts/pdf_1_old.pdf"  # Update this if necessary


# Function to check for images on the last page
def check_images_in_last_page(pdf_path):
    # json_data={}
    with pdfplumber.open(pdf_path) as pdf:
        last_page = pdf.pages[-1]  # Get the last page

        # Extract images from the last page
        images = last_page.images

        # Return True if images are found, False otherwise
        if images:
            # print(f"Images found on the last page: {len(images)} images.")
            # return True
            json_data = new_pattern(pdf_path)
            # print(json_data)
        else:
            print("No images found on the last page.")
            json_data = old_pattern(pdf_path)
        
    with open("voter_info_new_1.json", "w", encoding="utf-8") as file:
        file.write(json_data)


check_images_in_last_page(pdf_path)

