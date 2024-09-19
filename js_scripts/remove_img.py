import fitz  # PyMuPDF

# Path to the input PDF file
input_pdf = "../scripts/habiba.pdf"
output_pdf = "./output_images/habiba_no_left_images_text.pdf"

# Open the input PDF
pdf_document = fitz.open(input_pdf)

# Load the first page
page = pdf_document.load_page(0)

# Get list of images on the first page
images = page.get_images(full=True)

# Collect image xrefs and their bounding boxes
image_data = []
for img in images:
    xref = img[0]  # image reference number
    bbox = page.get_image_bbox(xref)  # Get image bounding box
    if bbox:
        image_data.append((xref, bbox))

# Remove images on the left side
for xref, bbox in image_data:
    if bbox.x0 < page.rect.width / 2:  # Left side condition
        page.remove_image(xref)

# Extract text to check its positions (bounding boxes)
text_blocks = page.get_text("dict")["blocks"]

# Redact text below the removed images on the left side
for block in text_blocks:
    if block["type"] == 0:  # Only process text blocks
        if block["bbox"][0] < page.rect.width / 2:  # Left side condition
            for line in block["lines"]:
                for span in line["spans"]:
                    page.add_redact_annot(span["bbox"], fill=(1, 1, 1))  # Redact with white background

# Apply redactions to remove text visually
page.apply_redactions()

# Save the modified PDF without images and text on the left side
pdf_document.save(output_pdf)
pdf_document.close()

# Output file path
print(f"Output PDF saved to: {output_pdf}")
