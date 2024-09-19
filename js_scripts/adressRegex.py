import re
import json

# The input text
text = """
বাংলাদেশ নির্বাচন কমিশন জাতীয় পরিচয় নিবন্ধন অনুবিভাগ নির্বাচন কমিশন সচিবালয়, আগারগীও, ঢাকা-১২০৭। রিপোর্টের ধরনঃ ভোটার তথ্য রিপোর্ট তারিখঃ ০৬-০৯-২০২৪ ১৭:৩৬:৪৩ National ID 5082303487 Pin 19802695432989341 Status printed Afis Status NO_MATCH Lock Flag N Death Voter No 261187989341 Form No 1989341 SI No 5097 Tag old Name(Bangla) মোঃ সোহেল Name(English) Md. Shohel Date of Birth 1980-03-02 Birth Place কুমিল্লা Birth Other Birth Registration No Father Name মোঃ হোসাইন আহমেদ Mother Name সালেহা বেগম Spouse Name Gender male Marital unmarried Occupation ব্যবসা Disability Disability Other Present Address Division ঢাকা District ঢাকা RMO 9 City Corporation Or ঢাকা দক্ষিণ সিটি Municipality কর্পোরেশন Upozila মতিঝিল Union/Ward ওয়ার্ড নং-০৯ Mouza/Moholla Additional আরামবাগ Mouza/Moholla Ward For Union 0 Village/Road Porishod Additional Home/HoldingNo ১৭৩/১,আরামবাগ Village/Road Post Office জিপিও Postal Code 1000 Region ঢাকা Permanent Address 11019107 চট্টগ্রাম District কুমিল্লা RMO City Corporation Or Municipality Upozila লাকসাম Union/Ward মুদাফফরগঞ্জ দক্ষিণ Mouza/Moholla Additional Mouza/Moholla Ward For Union 5 Village/Road Porishod Additional নাকজাটিয়া Home/HoldingNo Village/Road Post Office সিরাং বাজার Postal Code Region কুমিল্লা Education ৮ম শ্রেণী Education Other Education Sub Identification Blood Group TIN Driving Passport NID Father NID Mother Nid Spouse Voter No Father Voter No Mother Voter No Spouse Phone Mobile Religion Islam Religion Other Death Date Of Father Death Date Of Mother Death Date Of Spouse No Finger 0 No Finger Print 0 Voter Area 'আরামবাগ(261187) Voter At present Photo Signature No Available Voter Documents"""

# text ="""National ID 3750017133 Pin 19942696635000623 Status printed Afis Status NO_MATCH Lock Flag N Death Voter No 261404001161 Form No 24316562 9৭০ 3236 Tag voter_2013 Name(Bangla) মোঃ মিলন হাওলাদার Name(English) MD. MILON HOWLADAR Date of Birth 1994-12-31 Birth Place ঢাকা Birth Other Birth Registration No Father Name মোঃ আশ্রাফ আলী Mother Name মোসাঃ তহমিনা বেগম Spouse Name Gender male Marital unmarried Occupation শ্রমিক Disability Disability Other Present Address Division ঢাকা District ঢাকা RMO 9 City Corporation Or ঢাকা উত্তর সিটি Municipality কর্পোরেশন Upozila রমনা Union/Ward ওয়ার্ড ন-৩৫ Mouza/Moholla Additional - Mouza/Moholla Ward For Union Village/Road Porishod Additional পাগলা মাজার Home/HoldingNo ২৩৬ Village/Road Post Office শান্তিনগর টি এস ও Postal Code ১২১৭ Region ঢাকা Permanent Address __ {Division বরিশাল District বরগুনা RMO 1 City Corporation Or Municipality Upozila বরগুনা সদর Union/Ward বুড়িরচর Mouza/Moholla Additional - Mouza/Moholla Ward For Union 6 Village/Road Porishod Additional বুড়ির চর Home/HoldingNo - Village/Road Post Office চালতা কাউনিয়া Postal Code ৮৭০০ Region বরিশাল Education ৮ম শ্রেণী Education Other Education Sub Identification Blood Group TIN Driving Passport NID Father 2696654293950 NID Mother 2696654293951 Nid Spouse Voter No Father Voter No Mother Voter No Spouse Phone Mobile 01724639798 Religion Islam Religion Other Death Date Of Father Death Date Of Mother Death Date Of Spouse No Finger 0 No Finger Print 0 Voter Area উত্তর নয়াটোলা ১ম ভাগ(পশ্চিম অংশ) (261404) Voter At present Photo Signature Voter Documents: VOTER_FORM VOTER_FORM"""

# Patterns for Present and Permanent Addresses
patterns = {
    "presentAddress": {
        "homeHoldingNo": r"Home/HoldingNo\s*([^V]+)Village/Road",
        "villageRoadAdditional": r"Village/Road Porishod Additional\s*([^H]+)Home/HoldingNo",
        "mouzaMohollaAdditional": r"Mouza/Moholla Additional\s*([^M]+)Mouza/Moholla Ward",
        "postOffice": r"Post Office\s*([^M]+)Postal Code",
        "postalCode": r"Postal Code\s*([^R]+)Region",
        "upozila": r"Upozila\s*([^U]+)Union/Ward",
        "cityCorporation": r"City Corporation Or\s*([^M]+)Municipality",
        "district": r"District\s*([^R]+)RMO",
        
    },
    "permanentAddress": {
        "homeHoldingNo": r"Home/HoldingNo\s*([^V]+)Village/Road",
        "villageRoadAdditional": r"Village/Road Porishod Additional\s*([^H]+)Home/HoldingNo",
        "mouzaMohollaAdditional": r"Mouza/Moholla Additional\s*([^M]+)Mouza/Moholla Ward",
        "postOffice": r"Post Office\s*([^M]+)Postal Code",
        "postalCode": r"Postal Code\s*([^R]+)Region",
        "upozila": r"Upozila\s*([^U]+)Union/Ward",
        "cityCorporation": r"City Corporation Or\s*([^M]+)Municipality",
        "district": r"District\s*([^R]+)RMO",
    }
}

# Function to extract fields based on patterns
def extract_address(text, patterns):
    address_data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        address_data[key] = match.group(1).strip() if match else None
    return address_data

# Parmanent Adress
def parmanent_address(text, patterns):
    address_data = {}
    for key, pattern in patterns.items():
        match = re.findall(pattern, text)
        address_data[key] = match[-1].strip() if match else None
    return address_data

# Extracting present and permanent addresses
present_address = extract_address(text, patterns["presentAddress"])
permanent_address = parmanent_address(text, patterns["permanentAddress"])

# Combine the results into a single dictionary
result = {
    "presentAddress": present_address,
    "permanentAddress": permanent_address
}

# Define output file path
output_file_path = 'address_output.json'

# Write the result to a JSON file
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# Output file path for reference
output_file_path
