import fitz  # PyMuPDF
from PIL import Image
import io
import base64
import json
import re

# For Teereact 
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
import pdfplumber


# pdf_path =  "../scripts/pdf_2_new.pdf"

def new_pattern(pdf_path):
    # There Is For Tessreact start 
    # Path to the Tesseract executable (customize based on your system)
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # Function to extract text from images using Tesseract
    def extract_text_from_image(image_path):
        # Set language to both Bengali (ben) and English (eng)
        text = pytesseract.image_to_string(Image.open(image_path), lang='ben+eng')
        return text

    # Function to convert PDF pages to images and perform OCR
    def extract_text_from_pdf(pdf_path):
        # Convert PDF pages to images
        pages = convert_from_path(pdf_path, dpi=146)
        
        all_text = ""
        image_folder = "pdf_images"
        os.makedirs(image_folder, exist_ok=True)
        # print("------------------------------There Is Print ---------------------------------------------")

        # Loop over each page and extract text
        for i, page in enumerate(pages):
            image_path = f"{image_folder}/page_{i+1}.jpg"
            page.save(image_path, 'JPEG')

            # Extract text from the current page
            page_text = extract_text_from_image(image_path)
            # for i in page_text:
            #     print(i)

            all_text += page_text + "\n\n"



        return all_text

    extracted_text = extract_text_from_pdf(pdf_path)

    # For data Cleaning
    text = re.sub(r'\s+', ' ', extracted_text).strip()



    # There Is For Tessreact End

    # The input text adf
    # text = """
    # বাংলাদেশ নির্বাচন কমিশন জাতীয় পরিচয় নিবন্ধন অনুবিভাগ নির্বাচন কমিশন সচিবালয়, আগারগীও, ঢাকা-১২০৭। রিপোর্টের ধরনঃ ভোটার তথ্য রিপোর্ট তারিখঃ ০৬-০৯-২০২৪ ১৭:৩৬:৪৩ National ID 5082303487 Pin 19802695432989341 Status printed Afis Status NO_MATCH Lock Flag N Death Voter No 261187989341 Form No 1989341 SI No 5097 Tag old Name(Bangla) মোঃ সোহেল Name(English) Md. Shohel Date of Birth 1980-03-02 Birth Place কুমিল্লা Birth Other Birth Registration No Father Name মোঃ হোসাইন আহমেদ Mother Name সালেহা বেগম Spouse Name নাকজাটিয়া Gender male Marital unmarried Occupation ব্যবসা Disability Disability Other Present Address Division ঢাকা District ঢাকা RMO 9 City Corporation Or ঢাকা দক্ষিণ সিটি Municipality কর্পোরেশন Upozila মতিঝিল Union/Ward ওয়ার্ড নং-০৯ Mouza/Moholla Additional আরামবাগ Mouza/Moholla Ward For Union 0 Village/Road Porishod Additional Home/HoldingNo ১৭৩/১,আরামবাগ Village/Road Post Office জিপিও Postal Code 1000 Region ঢাকা Permanent Address 11019107 চট্টগ্রাম District কুমিল্লা RMO City Corporation Or Municipality Upozila লাকসাম Union/Ward মুদাফফরগঞ্জ দক্ষিণ Mouza/Moholla Additional Mouza/Moholla Ward For Union 5 Village/Road Porishod Additional নাকজাটিয়া Home/HoldingNo Village/Road Post Office সিরাং বাজার Postal Code Region কুমিল্লা Education ৮ম শ্রেণী Education Other Education Sub Identification Blood Group TIN Driving Passport NID Father NID Mother Nid Spouse Voter No Father Voter No Mother Voter No Spouse Phone Mobile 01625980677 Religion Islam Religion Other Death Date Of Father Death Date Of Mother Death Date Of Spouse No Finger 0 No Finger Print 0 Voter Area 'আরামবাগ(261187) Voter At present Photo Signature No Available Voter Documents
    # """

    # text = """বাংলাদেশ নির্বাচন কমিশন জাতীয় পরিচয় নিবন্ধন অনুবিভাগ নির্বাচন কমিশন সচিবালয়, আগারগীও, ঢাকা-১২০৭। রিপোর্টের ধরনঃ ভোটার তথ্য রিপোর্ট তারিখঃ ০৬-০৯-২০২৪ ১৭:৩৬:৪৩ National ID 5082303487 Pin 19802695432989341 Status printed Afis Status NO_MATCH Lock Flag N Death Voter No 261187989341 Form No 1989341 SI No 5097 Tag old Name(Bangla) মোঃ সোহেল Name(English) Md. Shohel Date of Birth 1980-03-02 Birth Place কুমিল্লা Birth Other Birth Registration No Father Name মোঃ হোসাইন আহমেদ Mother Name সালেহা বেগম Spouse Name Gender male Marital unmarried Occupation ব্যবসা Disability Disability Other Present Address Division ঢাকা District ঢাকা RMO 9 City Corporation Or ঢাকা দক্ষিণ সিটি Municipality কর্পোরেশন Upozila মতিঝিল Union/Ward ওয়ার্ড নং-০৯ Mouza/Moholla Additional আরামবাগ Mouza/Moholla Ward For Union 0 Village/Road Porishod Additional Home/HoldingNo ১৭৩/১,আরামবাগ Village/Road Post Office জিপিও Postal Code 1000 Region ঢাকা Permanent Address 11019107 চট্টগ্রাম District কুমিল্লা RMO City Corporation Or Municipality Upozila লাকসাম Union/Ward মুদাফফরগঞ্জ দক্ষিণ Mouza/Moholla Additional Mouza/Moholla Ward For Union 5 Village/Road Porishod Additional নাকজাটিয়া Home/HoldingNo Village/Road Post Office সিরাং বাজার Postal Code Region কুমিল্লা Education ৮ম শ্রেণী Education Other Education Sub Identification Blood Group TIN Driving Passport NID Father NID Mother Nid Spouse Voter No Father Voter No Mother Voter No Spouse Phone Mobile Religion Islam Religion Other Death Date Of Father Death Date Of Mother Death Date Of Spouse No Finger 0 No Finger Print 0 Voter Area 'আরামবাগ(261187) Voter At present Photo Signature No Available Voter Documents"""

    # Regular expression patterns to extract the necessary fields
    patterns = {
        "nid": r"National ID (\d+)",
        "pin": r"Pin (\d+)",
        "voterNo": r"Voter No (\d+)",
        "formNum": r"Form No (\d+)",
        # "nameEnglish": r"Name\(English\) ([\w\s.]+)",
        "nameEnglish": r"Name\(English\) ([\w\s.]+)(?=\sDate of Birth)",
        "dateOfBirth": r"Date of Birth (\d{4}-\d{2}-\d{2})",
        # "bloodGroup": r"Blood Group (\w*)",
        # "bloodGroup": r"Blood Group (A[+-]|B[+-]|AB[+-]|O[+-])",
        "bloodGroup": r"Blood Group\s*([^T]+) TIN",
        "mobile": r"Mobile (\d*)",
        "marital": r"Marital (\w+)",
        "religion": r"Religion (\w+)",
        # "voterAt": r"Voter At ([\w\s]+)",
        "voterAt": r"Voter At (\bpresent\b)",

        # "voterArea": r"Voter Area '([\w\s()]+)'",
        "voterArea": r"Voter Area ([^\n]+?) Voter At",


        "gender": r"Gender (\w+)",
        # "dateOfBirth": r"Date of Birth (\d{4}-\d{2}-\d{2})",
        # "nameBangla": r"Name\(Bangla\) ([\w\s.]+)",
        "nameBangla": r"Name\(Bangla\) ([^\n]+?) Name\(English\)",

        # "birthPlace": r"Birth Place ([\w\s]+)",
        "birthPlace": r"Birth Place ([^\n]+?) Birth Other",

        "fatherName": r"Father Name ([^\n]+?) Mother Name",
        "motherName": r"Mother Name ([^\n]+?) Spouse Name",

        # "spouseName": r"Spouse Name (\w*)",
        "spouseName": r"Spouse Name(?: ([^\n]+?))? Gender",

        # "address": r"Permanent Address.*District ([\w\s]+)",
        # "spouse": r"Spouse Name (\w*)",
        
        "present_homeHoldingNo": r"Home/HoldingNo\s*([^V]+)Village/Road",
        "present_villageRoadAdditional": r"Village/Road Porishod Additional\s*([^H]+)Home/HoldingNo",
        "present_mouzaMohollaAdditional": r"Mouza/Moholla Additional\s*([^M]+)Mouza/Moholla Ward",
        "present_postOffice": r"Post Office\s*([^P]+)Postal Code",
        "present_postalCode": r"Postal Code\s*([^R]+)Region",
        "present_upozila": r"Upozila\s*([^U]+)Union/Ward",
        "present_cityCorporation": r"City Corporation Or\s*([^M]+)Municipality",
        "present_district": r"District\s*([^R]+)RMO",


    }

    permanentAddress= {

            "parmanent_homeHoldingNo": r"Home/HoldingNo\s*([^V]+)Village/Road",
            "parmanent_villageRoadAdditional": r"Village/Road Porishod Additional\s*([^H]+)Home/HoldingNo",
            "parmanent_mouzaMohollaAdditional": r"Mouza/Moholla Additional\s*([^M]+)Mouza/Moholla Ward",
            "parmanent_postOffice": r"Post Office\s*([^P]+)Postal Code",
            "parmanent_postalCode": r"Postal Code\s*([^R]+)Region",
            "parmanent_upozila": r"Upozila\s*([^U]+)Union/Ward",
            "parmanent_cityCorporation": r"City Corporation Or\s*([^M]+)Municipality",
            "parmanent_district": r"District\s*([^R]+)RMO",
        }

    # Extracting the data using the regular expressions
    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        data[key] = match.group(1) if match else None


    for key, pattern in permanentAddress.items():
        match = re.findall(pattern, text)
        data[key] = match[-1].strip() if match else None

    # For Image Base64
    # statr here
    image_data = {}

    def clamp(value, min_value, max_value):
        """Helper function to ensure values are within a specified range."""
        return max(min_value, min(value, max_value))

    # Open the PDF using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[-1]  # Get the first page
        page_width = first_page.width
        page_height = first_page.height

        # Extract images from the first page
        images = first_page.images

        for idx, img in enumerate(images):
            # Get the bounding box of the image
            x0, y0, x1, y1 = img["x0"], img["top"], img["x1"], img["bottom"]

            # Clamp the bounding box coordinates to ensure they are within the page bounds
            x0 = clamp(x0, 0, page_width)
            y0 = clamp(y0, 0, page_height)
            x1 = clamp(x1, 0, page_width)
            y1 = clamp(y1, 0, page_height)

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

    # image_data = pdf_images_to_base64(pdf_path)




    # ends here 
    data["image1_base64"] = image_data
    # Convert the data to JSON format
    json_data = json.dumps(data, ensure_ascii=False, indent=4)

    return json_data

    # Output the JSON data
    # print(json_data)

    # Optionally, save it to a file

    # with open("voter_info_new_1.json", "w", encoding="utf-8") as file:
    #     file.write(json_data)
