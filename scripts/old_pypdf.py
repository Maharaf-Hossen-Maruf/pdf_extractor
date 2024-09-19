import fitz  # PyMuPDF

# Load the PDF
pdf_path = "./pdf_1_old.pdf"
output_path = "./old_pattern/habiba_cleaned.pdf"
doc = fitz.open(pdf_path)

# Select the first page
page = doc[0]

# Get the page dimensions
page_width = page.rect.width
page_height = page.rect.height

# Adjust x0 and x1 to control the width of the redacted area
x0 = page_width * 0.7  # Left side starts at 70% of the page width (adjust as needed)
x1 = page_width * 0.3  # Right side is at the full width of the page

# Define the rectangle with adjusted width
rect = fitz.Rect(x0, 0, x1, page_height)

# Redact the area (this will remove all text and images in this area)
page.add_redact_annot(rect)  # Create a redaction annotation
page.apply_redactions()  # Apply the redaction

# Save the modified PDF
doc.save(output_path)
doc.close()

print(f"Cleaned PDF saved to {output_path}")
