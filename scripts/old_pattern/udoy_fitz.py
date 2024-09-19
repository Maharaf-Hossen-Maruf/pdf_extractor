import fitz
import re
import base64
import unicodedata

def extract_text_from_pdf(pdf_document):
    """
    Extract text from the entire PDF document using PyMuPDF (fitz).
    """
    text_content = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_content += page.get_text()

    # Write extracted text to a file for inspection
    with open('pdf_text_output.txt', 'w', encoding='utf-8') as f:
        f.write(text_content)
    
    return text_content

x=extract_text_from_pdf('../habiba.pdf')

def clean_bengali_text(text):
    """
    Clean and fix Bangla text encoding issues using normalization.
    """
    if text:
        # Normalize text to NFC (Normalization Form C) for Bengali characters
        normalized_text = unicodedata.normalize('NFC', text)
        return normalized_text
    return ""


def extract_field_data(text, field_name):
    """
    Extract a specific field from the PDF text using regular expressions.
    """
    field_pattern = rf"{re.escape(field_name)}:?\s*(.*?)(?:\n|$)"
    match = re.search(field_pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        return clean_bengali_text(match.group(1).strip())
    else:
        print(f"Field '{field_name}' not found in the text.")
    return ""


def extract_data_from_pdf(pdf_file):
    """
    Extract images (as Base64) and text data from the PDF.
    """
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    extracted_data = {
        "userIMG": None,
        "signIMG": None,
        "nameBangla": "",
        "nameEnglish": "",
        "spouseName": "",
        "nid": "",
        "pin": "",
        "fatherName": "",
        "motherName": "",
        "dateOfBirth": "",
        "birthPlace": "",
        "bloodGroup": "",
        "address": "",
        "gender": "",
        "religion": "",
        "house_no": ""
    }

    # Extract Images and encode them as Base64
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            image = pdf_document.extract_image(xref)
            image_bytes = image["image"]

            # Convert the image bytes to Base64
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            
            # Create the data URI
            image_data_uri = f"data:image/jpeg;base64,{image_base64}"

            if img_index == 0:
                extracted_data["userIMG"] = image_data_uri
            elif img_index == 1:
                extracted_data["signIMG"] = image_data_uri

    # Extract Text
    pdf_text = extract_text_from_pdf(pdf_document)

    # Extract specific fields
    extracted_data["nameBangla"] = extract_field_data(pdf_text, "Name(Bangla)")
    extracted_data["nameEnglish"] = extract_field_data(pdf_text, "Name(English)")
    extracted_data["spouseName"] = extract_field_data(pdf_text, "Spouse Name")
    extracted_data["nid"] = extract_field_data(pdf_text, "National ID")
    extracted_data["pin"] = extract_field_data(pdf_text, "Pin")
    extracted_data["fatherName"] = extract_field_data(pdf_text, "Father Name")
    extracted_data["motherName"] = extract_field_data(pdf_text, "Mother Name")
    extracted_data["dateOfBirth"] = extract_field_data(pdf_text, "Date of Birth")
    extracted_data["birthPlace"] = extract_field_data(pdf_text, "Birth Place")
    extracted_data["bloodGroup"] = extract_field_data(pdf_text, "Blood Group")
    extracted_data["gender"] = extract_field_data(pdf_text, "Gender")
    extracted_data["religion"] = extract_field_data(pdf_text, "Religion")
    extracted_data["house_no"] = extract_field_data(pdf_text, "Home/HoldingNo")

    # Print specific field extractions for debugging
    for key, value in extracted_data.items():
        print(f"{key}: {value}")

    # Extract Address Fields and Concatenate
    house_no = extracted_data["house_no"]
    city = extract_field_data(pdf_text, r"City Corporation Or\s+Municipality")
    upozila = extract_field_data(pdf_text, "Upozila")
    district = extract_field_data(pdf_text, "District")
    village = extract_field_data(pdf_text, r"Additional\s+Village/Road") if re.search(r"Additional\s+Village/Road", pdf_text) else ""
    post_office = extract_field_data(pdf_text, "Post Office")
    post_code = extract_field_data(pdf_text, "Postal Code")
    additional_moholla = extract_field_data(pdf_text, r"Additional\s+Mouza/Moholla")
    road_or_moholla = additional_moholla

    # Format the address
    extracted_data['address'] = (
        f"বাসা/হোল্ডিং: {house_no}, "
        f"গ্রাম/রাস্তা: {road_or_moholla}, "
        f"ডাকঘর: {post_office} - {post_code}, "
        f"{upozila}, {city}, {district}"
    ).strip()

    return extracted_data
