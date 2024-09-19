# Clean the data and write it to a new file

import re

# The input text
text = """
--- Page 1 ---
Citizen
National ID
1466015698
Pin
19821910956204667
Status
printed
Afis Status
NO_MATCH
Lock Flag
N
Voter No
191530204667
Form No
3204667
Sl No
155
Tag
old
Name(Bangla)
মোঃ আবদুর রাজ্জাক
Name(English)
Md Abdur Razzak
Date of Birth
1982-09-01
Birth Place
কুমিল্লা
Birth Other
Birth Registration
No
Father Name
মোঃ আঃ মালেক
Mother Name
আমেনা বেগম
Spouse Name
রওশন আরা
Gender
male
Marital
married
Occupation
বেসরকারী চাকুরী
Disability
Disability Other
Present Address
Division
চট্টগ্রাম
District
কুমিল্লা
RMO
পল্লী (1)
City
Corporation
Or
Municipality
Upozila
বরুড়া
Union/Ward
ঝলম
Mouza/Moholla
Additional
Mouza/Moholla
ঝলম
Ward For
Union
Porishod
1
Village/Road
Additional
Village/Road
বিলপুকুরিয়া
Home/Holding
No
প্রধানিয়া বাড়ী
Post Office
ঝলম
Postal Code
3560
Region
কুমিল্লা
Permanent Address
Division
চট্টগ্রাম
District
কুমিল্লা
RMO
পল্লী (1)
City
Corporation
Or
Municipality
Upozila
বরুড়া
Union/Ward
Mouza/Moholla
Additional
Mouza/Moholla
ঝলম
Ward For
Union
Porishod
1
Village/Road
Additional
Village/Road
বিলপুকুরিয়া
Home/Holding
No
প্রধানিয়া বাড়ী
Post Office
ঝলম
Postal Code
3560
Region
কুমিল্লা
Education
উচ্চ মাধ্যমিক
Education Other
Education Sub
Smart Card Info
Voter Documents
No Documents Available

--- Page 2 ---
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
01818656516
Mobile
Religion
Islam
Religion Other
Death Date Of
Father
Death Date Of
Mother
Death Date Of
Spouse
No Finger
0
No Finger Print
0
Voter Area
বিল পুকুরিয়া (191530)
Voter At
present


"""

# Remove newlines and extra spaces, keeping only a single space between words
cleaned_text = re.sub(r'\s+', ' ', text).strip()

# Save the cleaned text to a file
output_file_path = "cleaned_new_1.txt"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(cleaned_text)

output_file_path
