import fitz  # PyMuPDF
from PIL import Image
import io
import base64
import json
import re

# For Teereact 
# import pytesseract
# from pdf2image import convert_from_path
# from PIL import Image
# import os

# update for Old 
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import cv2
# import numpy as np

import pdfplumber


# pdf_path =  "../scripts/pdf_1_new.pdf"

def old_pattern(pdf_path):

    def pdf_extract_text(pdf_path):
        text=''
        with fitz.open(pdf_path) as pdf:
            
            for page_num in range(len(pdf)):
                # Extract text from each page
                page = pdf.load_page(page_num)
                text += page.get_text("text")  # Extract text in simple layout

                # # Write the text to the output file
                # output_file.write(f"--- Page {page_num + 1} ---\n")
                # output_file.write(text + "\n")
        return text
        




    extracted_text = pdf_extract_text(pdf_path)

    # For data Cleaning
    text = re.sub(r'\s+', ' ', extracted_text).strip()

    output_file_path = "cleaned_new_1.txt"
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(text)

    # output_file_path


    # There Is For Tessreact End

    # The input text adf
    # text = """
    # বাংলাদেশ নির্বাচন কমিশন জাতীয় পরিচয় নিবন্ধন অনুবিভাগ নির্বাচন কমিশন সচিবালয়, আগারগীও, ঢাকা-১২০৭। রিপোর্টের ধরনঃ ভোটার তথ্য রিপোর্ট তারিখঃ ০৬-০৯-২০২৪ ১৭:৩৬:৪৩ National ID 5082303487 Pin 19802695432989341 Status printed Afis Status NO_MATCH Lock Flag N Death Voter No 261187989341 Form No 1989341 SI No 5097 Tag old Name(Bangla) মোঃ সোহেল Name(English) Md. Shohel Date of Birth 1980-03-02 Birth Place কুমিল্লা Birth Other Birth Registration No Father Name মোঃ হোসাইন আহমেদ Mother Name সালেহা বেগম Spouse Name নাকজাটিয়া Gender male Marital unmarried Occupation ব্যবসা Disability Disability Other Present Address Division ঢাকা District ঢাকা RMO 9 City Corporation Or ঢাকা দক্ষিণ সিটি Municipality কর্পোরেশন Upozila মতিঝিল Union/Ward ওয়ার্ড নং-০৯ Mouza/Moholla Additional আরামবাগ Mouza/Moholla Ward For Union 0 Village/Road Porishod Additional Home/HoldingNo ১৭৩/১,আরামবাগ Village/Road Post Office জিপিও Postal Code 1000 Region ঢাকা Permanent Address 11019107 চট্টগ্রাম District কুমিল্লা RMO City Corporation Or Municipality Upozila লাকসাম Union/Ward মুদাফফরগঞ্জ দক্ষিণ Mouza/Moholla Additional Mouza/Moholla Ward For Union 5 Village/Road Porishod Additional নাকজাটিয়া Home/HoldingNo Village/Road Post Office সিরাং বাজার Postal Code Region কুমিল্লা Education ৮ম শ্রেণী Education Other Education Sub Identification Blood Group TIN Driving Passport NID Father NID Mother Nid Spouse Voter No Father Voter No Mother Voter No Spouse Phone Mobile 01625980677 Religion Islam Religion Other Death Date Of Father Death Date Of Mother Death Date Of Spouse No Finger 0 No Finger Print 0 Voter Area 'আরামবাগ(261187) Voter At present Photo Signature No Available Voter Documents
    # """

    # text = """বাংলাদেশ নির্বাচন কমিশন জাতীয় পরিচয় নিবন্ধন অনুবিভাগ নির্বাচন কমিশন সচিবালয়, আগারগীও, ঢাকা-১২০৭। রিপোর্টের ধরনঃ ভোটার তথ্য রিপোর্ট তারিখঃ ০৬-০৯-২০২৪ ১৭:৩৬:৪৩ National ID 5082303487 Pin 19802695432989341 Status printed Afis Status NO_MATCH Lock Flag N Death Voter No 261187989341 Form No 1989341 SI No 5097 Tag old Name(Bangla) মোঃ সোহেল Name(English) Md. Shohel Date of Birth 1980-03-02 Birth Place কুমিল্লা Birth Other Birth Registration No Father Name মোঃ হোসাইন আহমেদ Mother Name সালেহা বেগম Spouse Name Gender male Marital unmarried Occupation ব্যবসা Disability Disability Other Present Address Division ঢাকা District ঢাকা RMO 9 City Corporation Or ঢাকা দক্ষিণ সিটি Municipality কর্পোরেশন Upozila মতিঝিল Union/Ward ওয়ার্ড নং-০৯ Mouza/Moholla Additional আরামবাগ Mouza/Moholla Ward For Union 0 Village/Road Porishod Additional Home/HoldingNo ১৭৩/১,আরামবাগ Village/Road Post Office জিপিও Postal Code 1000 Region ঢাকা Permanent Address 11019107 চট্টগ্রাম District কুমিল্লা RMO City Corporation Or Municipality Upozila লাকসাম Union/Ward মুদাফফরগঞ্জ দক্ষিণ Mouza/Moholla Additional Mouza/Moholla Ward For Union 5 Village/Road Porishod Additional নাকজাটিয়া Home/HoldingNo Village/Road Post Office সিরাং বাজার Postal Code Region কুমিল্লা Education ৮ম শ্রেণী Education Other Education Sub Identification Blood Group TIN Driving Passport NID Father NID Mother Nid Spouse Voter No Father Voter No Mother Voter No Spouse Phone Mobile Religion Islam Religion Other Death Date Of Father Death Date Of Mother Death Date Of Spouse No Finger 0 No Finger Print 0 Voter Area 'আরামবাগ(261187) Voter At present Photo Signature No Available Voter Documents"""

    # Regular expression patterns to extract the necessary fields
    patterns = {
        "nid": r"National ID [^0-9]*([0-9]{9,})",
        "pin": r"Pin (\d+)",
        "voterNo": r"Voter No (\d+)",
        # "formNum": r"Form No (\d+)",
        # "formNum": r"Form No [^ ]*([A-Za-z0-9]{9,})",
        # "formNum": r"Form No ([A-Za-z0-9]{9,})",
        "formNum": r"Form No\s*([^S]+) Sl No",
        # "nameEnglish": r"Name\(English\) ([\w\s.]+)",
        # "nameEnglish": r"Name\(English\) ([\w\s.]+)(?=\sDate of Birth)",
        # "nameEnglish": r"Name\(English\)\s*([\w\s.]+?)(?=\s*[\|\sDate of Birth])",
        # "nameEnglish" : r"Name\(English\)\s*([A-Za-z\s.]+)(?=\s*\|\s*Date of Birth)", wokring without 5
        "nameEnglish" : r"Name\(English\)\s*(.*?)\s*(?=Date of Birth)",
        "dateOfBirth": r"Date of Birth (\d{4}-\d{2}-\d{2})",
        # "bloodGroup": r"Blood Group (\w*)",
        # "bloodGroup": r"Blood Group (A[+-]|B[+-]|AB[+-]|O[+-])",
        "bloodGroup": r"Blood Group\s*([^T]+) TIN",
        "mobile": r"Mobile (\d*)",
        "marital": r"Marital (\w+)",
        "religion": r"Religion (\w+)",
        # "voterAt": r"Voter At ([\w\s]+)",
        # "voterAt": r"Voter At (\bpresent\b)",
        "voterAt": r"Voter At\s*([^U]+) Updated By",
        

        # "voterArea": r"Voter Area '([\w\s()]+)'",
        "voterArea": r"Voter Area ([^\n]+?) Voter At",


        "gender": r"Gender([^\n]+?) Marital",
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
        
        "present_homeHoldingNo": r"Home/Holding No\s*([^P]+)Post Office",
        "present_villageRoadAdditional": r"Village/Road Additional\s*([^H]+)Home/HoldingNo",
        "present_mouzaMohollaAdditional": r"Village/Road\s*([^A]+)Additional Village/Road",
        "present_postOffice": r"Post Office\s*([^P]+)Postal Code",
        "present_postalCode": r"Postal Code\s*([^R]+)Region",
        "present_upozila": r"Upozila\s*([^U]+)Union/Ward",
        "present_cityCorporation": r"Union/Ward\s*([^M]+)Mouza/Moholla",
        "present_district": r"District\s*([^R]+)RMO",


    }

    permanentAddress= {

            "parmanent_homeHoldingNo": r"Home/Holding No\s*([^P]+)Post Office",
            "parmanent_villageRoadAdditional": r"Village/Road Additional\s*([^H]+)Home/HoldingNo",
            "parmanent_mouzaMohollaAdditional": r"Village/Road\s*([^A]+)Additional Village/Road",
            "parmanent_postOffice": r"Post Office\s*([^P]+)Postal Code",
            "parmanent_postalCode": r"Postal Code\s*([^R]+)Region",
            "parmanent_upozila": r"Upozila\s*([^U]+)Union/Ward",
            "parmanent_cityCorporation": r"Union/Ward\s*([^M]+)Mouza/Moholla",
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

    image_data = {}

    def clamp(value, min_value, max_value):
        """Helper function to ensure values are within a specified range."""
        return max(min_value, min(value, max_value))

    # Open the PDF using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]  # Get the first page
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





    data["image1_base64"] = image_data
    # Convert the data to JSON format
    json_data = json.dumps(data, ensure_ascii=False, indent=4)


    return json_data
    # Output the JSON data
    # print(json_data)

    # Optionally, save it to a file

    # with open("voter_info_new_1.json", "w", encoding="utf-8") as file:
        # file.write(json_data)



