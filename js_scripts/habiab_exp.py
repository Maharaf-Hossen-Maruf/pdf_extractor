import re
import json

# The input text
text = """
Citizen

National ID

Pin

Status

Afis Status
Lock Flag
Voter No

Form No

SI No

Tag
Name(Bangla)
Name(English)
Date of Birth
Birth Place
Birth Other
Birth Registration
No

Father Name
Mother Name
Spouse Name
Gender

Marital
Occupation
Disability
Disability Other
Present Address

Permanent Address

Education

5538202481

19917511028000215

printed
NO_MATCH

N
750757000064
19269476

302

left_out

হাবিবা খাতুন
Habiba Khatun
1991-03-11
নোয়াখালা

19917511076012690

আবদুল হালিম
রেহানা আক্তার
আঙ্কার হোসেন
female

married

গৃহিনী

Division
RMO

Upozila
Mouza/Moholla

Ward For
Union
Porishod
Additional
Village/Road

Post Office
Region
Division
RMO

Upozila
Mouza/Moholla

Ward For
Union
Porishod
Additional
Village/Road

Post Office
Region
৮ম শ্রেণী

চট্টগ্রাম
পল্লী (1)

নাহারখিল

খিলপাড়া

চট্টগ্রাম
পল্লী (1)

চাটখিল

খিলপাড়া

District

City
Corporation

Or

Municipality
Union/Ward
Additional
Mouza/Moholla
Village/Road

Home/Holding
No

Postal Code

District

City
Corporation

Or

Municipality
Union/Ward
Additional
Mouza/Moholla
Village/Road

Home/Holding
No

Postal Code

“afm

Voter Documents

e VOTER FORM
« VOTER FORM

খিল পাড়া

নাহারখিল

কাসেম আলী
হাজী বাড়ি
(নতুন)
৩৮৭২

খিল পাড়া

নাহারখিল

কাসেম আলী
হাজী বাড়ি
(নতুন)
৩৮৭২


Education Other

Education Sub
Identification
Blood Group
TIN

Driving
Passport
Laptop ID
NID Father
NID Mother

7510__4391
19717511076000002
7511076661656

Nid Spouse

Voter No Father

Voter No Mother

Voter No Spouse

Phone

Mobile

Religion Islam
Religion Other

Death Date Of

Father

Death Date Of

Mother

Death Date Of

Spouse

No Finger 9
No Finger Print 0

Voter Area নাহারখীল(পশ্টিম) (750757)

Voter At permanent

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
    "spouseName": r"Spouse\n([^\n]*)",
    "address": r"Present Address\n(.*?)(?=\n[A-Z])",
}

# Extract data
data = {key: re.search(pattern, text).group(1).strip() if re.search(pattern, text) else "" for key, pattern in patterns.items()}

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
