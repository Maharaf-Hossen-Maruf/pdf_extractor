import pdfplumber

# File path to the PDF
pdf_path = "../scripts/pdf_6_new.pdf"  # Update this if necessary

# Function to check for images on the last page
def check_images_in_last_page(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        last_page = pdf.pages[-1]  # Get the last page

        # Extract images from the last page
        images = last_page.images

        # Return True if images are found, False otherwise
        if images:
            print(f"Images found on the last page: {len(images)} images.")
            return True
        else:
            print("No images found on the last page.")
            return False

# Call the function
if check_images_in_last_page(pdf_path):
    print("Images are present on the last page.")
else:
    print("No images found on the last page.")
