import re
import json

# The input text
text = """
বাংলাদেশ নির্বাচন কমিশন
জাতীয় পরিচয় নিবন্ধন অনুবিভাগ
নির্বাচন কমিশন সচিবালয়, আগারগীও, ঢাকা-১২০৭।

রিপোর্টের ধরনঃ ভোটার তথ্য রিপোর্ট
তারিখঃ ০৬-০৯-২০২৪ ১৭:৩৬:৪৩

National ID 5082303487
Pin 19802695432989341
Status printed

Afis Status NO_MATCH
Lock Flag N

Death

Voter No 261187989341
Form No 1989341

SI No 5097

Tag old
Name(Bangla) মোঃ সোহেল
Name(English) Md. Shohel
Date of Birth 1980-03-02
Birth Place কুমিল্লা

Birth Other
Birth Registration No

Father Name

মোঃ হোসাইন আহমেদ

Mother Name সালেহা বেগম

Spouse

Gender male

Marital unmarried

Occupation ব্যবসা

Disability

Disability Other

Present Address Division ঢাকা District ঢাকা
RMO 9 City Corporation Or ঢাকা দক্ষিণ সিটি

Municipality কর্পোরেশন
Upozila মতিঝিল Union/Ward ওয়ার্ড নং-০৯
Mouza/Moholla Additional আরামবাগ
Mouza/Moholla

Ward For Union 0 Village/Road
Porishod
Additional Home/HoldingNo ১৭৩/১,আরামবাগ
Village/Road
Post Office জিপিও Postal Code 1000
Region ঢাকা

Permanent Address 11019107 চট্টগ্রাম District কুমিল্লা

RMO

City Corporation Or

Municipality
Upozila লাকসাম Union/Ward মুদাফফরগঞ্জ দক্ষিণ
Mouza/Moholla Additional
Mouza/Moholla
Ward For Union 5 Village/Road
Porishod
Additional নাকজাটিয়া Home/HoldingNo
Village/Road
Post Office সিরাং বাজার Postal Code
Region কুমিল্লা
Education ৮ম শ্রেণী

Education Other

Education Sub

Identification

Blood Group

TIN

Driving

Passport

NID Father

NID Mother

Nid Spouse
Voter No Father

Voter No Mother

Voter No Spouse

Phone

Mobile

Religion

Islam

Religion Other

Death Date Of Father 

Death Date Of Mother

Death Date Of
Spouse

No Finger

0

No Finger Print

0

Voter Area

'আরামবাগ(261187)

Voter At

present



Photo

Signature

No Available Voter Documents
"""

# Define regex patterns
patterns = {
    "nid": r"National ID (\d+)",
    "pin": r"Pin (\d+)",
    "voterNo": r"Voter No (\d+)",
    "formNum": r"Form No (\d+)",
    "nameEnglish": r"Name\(English\) ([^\n]+)",
    "dateOfBirth": r"Date of Birth (\d{4}-\d{2}-\d{2})",
    "bloodGroup": r"Blood Group\n([^\n]*)",
    "mobile": r"Mobile\n([^\n]*)",
    "marital": r"Marital ([^\n]+)",
    "religion": r"Religion\n([^\n]*)",
    "voterAt": r"Voter At\n([^\n]*)",
    "voterArea": r"Voter Area\n'([^\n]+)",
    "gender": r"Gender ([^\n]+)",
    "nameBangla": r"Name\(Bangla\) ([^\n]+)",
    "birthPlace": r"Birth Place ([^\n]+)",
    "fatherName": r"Father Name\n\n([^\n]+)",
    "motherName": r"Mother Name ([^\n]+)",
    "spouseName": r"Spouse\n([^\n]*)",  # Updated pattern for Spouse
    "address": r"Present Address\n(.*?)(?=\n[A-Z])",
}

# Extract data
data = {key: re.search(pattern, text).group(1).strip() if re.search(pattern, text) else "" for key, pattern in patterns.items()}

# Check for empty spouseName and handle it
if not data["spouseName"]:
    data["spouseName"] = None

# Format the address separately
present_address = re.search(patterns['address'], text, re.DOTALL)
if present_address:
    address_lines = present_address.group(1).strip().split('\n')
    address = ', '.join([line.strip() for line in address_lines])
else:
    address = ""

# Add address to the extracted data
data["address"] = address

# Convert to JSON format
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Save JSON data to a text file
with open('voter_info.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
