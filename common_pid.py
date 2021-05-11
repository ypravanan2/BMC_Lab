import os
import re

# Creating a folder_name for Output
path = r"C:\Users\user\OneDrive\Desktop\python\Thamo Sir\USA Suceptible Strains"
files = os.listdir(path)
if not os.path.isdir("Output"):
    os.mkdir("Output")
file1 = open("USA_Master list.csv", "r")
file1_lines = file1.readlines()
file1_id = []

# Collecting Patric ID from Master file
for i in file1_lines:
    line = i.split(",")
    if re.match("^\"", line[4]):  # removing " at start and end
        line[4] = str(line[4].strip("\""))
    if line[4] != 'PATRIC ID':  # appending id's to a list
        file1_id.append(line[4])

# Checking Patric ID of antibiotics with Master file
for file_name in files:
    file_name_alone = file_name[:-4:]  # removing extensions
    file2 = open("USA Suceptible Strains//" + file_name, "r")
    new_file = open("Output//" + file_name_alone + "_common_strains.csv", "a")  # new file for common strains
    new_file2 = open("Output//" + file_name_alone + "_uncommon_strains.csv", "a")  # new file for uncommon strains
    file2_lines = file2.readlines()
    for li in file2_lines:
        line = li.split(",")
        patric_id = line[4]
        if patric_id != "PATRIC ID":
            if re.match("^\"", patric_id):  # removing " at start and end
                patric_id = str(patric_id.strip("\""))
            if patric_id in file1_id:  # Checking with Master file
                new_file.write(li)
            else:
                new_file2.write(li)
        else:
            new_file.write(patric_id)
            new_file2.write(patric_id)
    file2.close()
