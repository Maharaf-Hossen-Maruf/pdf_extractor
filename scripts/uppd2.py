import PyPDF2
import json

def extract_text_from_pdf(pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as pdf_file:
        # Initialize the PDF reader
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_text = ""

        # Extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            # Try to decode the text properly
            try:
                pdf_text += page.extract_text()
            except Exception as e:
                print(f"Error extracting text from page {page_num}: {e}")

    # Return extracted text
    return pdf_text

def clean_bangla_text(text):
    """
    Clean and decode text to handle Bangla characters more accurately.
    """
    try:
        # Re-encode as utf-8 to handle Bangla text better
        text = text.encode('latin1').decode('utf-8')
    except Exception as e:
        print(f"Error while encoding text: {e}")
    
    return text

def convert_text_to_json(pdf_text):
    # Manually parse the text to extract relevant information
    data = {}

    lines = pdf_text.splitlines()
    
    for line in lines:
        if "National ID" in line:
            data['National ID'] = line.split()[-1]
        elif "Pin" in line:
            data['Pin'] = line.split()[-1]
        elif "Status" in line:
            data['Status'] = line.split()[-1]
        elif "Name(Bangla)" in line:
            data['Name(Bangla)'] = line.split(' ', 1)[-1].strip()
        elif "Name(English)" in line:
            data['Name(English)'] = line.split(' ', 1)[-1].strip()
        elif "Date of Birth" in line:
            data['Date of Birth'] = line.split()[-1]
        elif "Father Name" in line:
            data['Father Name'] = line.split(' ', 2)[-1].strip()
        elif "Mother Name" in line:
            data['Mother Name'] = line.split(' ', 2)[-1].strip()
        elif "Gender" in line:
            data['Gender'] = line.split()[-1]
        elif "Marital" in line:
            data['Marital Status'] = line.split()[-1]
        elif "Occupation" in line:
            data['Occupation'] = line.split(' ', 1)[-1].strip()
        elif "Present Address" in line:
            data['Present Address'] = line.strip()
        elif "Permanent Address" in line:
            data['Permanent Address'] = line.strip()

    return data

def save_to_json(data, output_file):
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

# Use regular string paths for file locations
pdf_file_path = "./habiba.pdf"
output_file = "output_data.json"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Clean up Bangla text (attempt to fix encoding issues)
cleaned_text = clean_bangla_text(pdf_text)

# Convert the cleaned text to JSON format
pdf_data = convert_text_to_json(cleaned_text)

# Save the JSON data to a file
save_to_json(pdf_data, output_file)
