import fitz  # PyMuPDF

# File paths
pdf_path = "./pdf_7_old.pdf"
output_txt_path = "output_pymupdf_text.txt"

# Open the PDF file
with fitz.open(pdf_path) as pdf:
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        for page_num in range(len(pdf)):
            # Extract text from each page
            page = pdf.load_page(page_num)
            text = page.get_text("text")  # Extract text in simple layout

            # Write the text to the output file
            output_file.write(f"--- Page {page_num + 1} ---\n")
            output_file.write(text + "\n")

print(f"Text extraction completed with PyMuPDF. Check {output_txt_path}.")
