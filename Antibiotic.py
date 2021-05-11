"""
Comparison of PATRIC ID's of reference file with other files.
Author : Subachandran
"""

"""importing Modules"""
import re  # Regex module
import os  # OS module to list files in directory

"""declaring reference file and folder name"""
folder_name = "usastrains"  # folder name or path of folder
comparison = "Trimethoprim and Sulfamethoxazole".lower()  # reference file
files = os.listdir(folder_name)  # listing all files under folder_name directory
ref = ""

"""looping all files in given folder to remove master and reference file."""
for i in files.copy():
    j = i.lower()  # converting file name to lower case
    if "master" in j:  # removing master file
        files.remove(i)
    elif re.match(".*" + comparison + ".*", j):  # removing reference file and storing that file name in ref  variable.
        ref = files.pop(files.index(i))

"""if reference file is not found, terminate program with alert message."""
if ref == "":
    print("Reference file doesn't exist in given folder!")
else:
    freq = {}  # declaring dictionary to store PATRIC ID of reference with details
    antibiotic = {}
    """reading reference file and storing PATRIC ID in keys of freq dictionary."""
    with open(os.path.join(folder_name, ref), "r") as file1:  # opening file in read mode
        for line in file1.readlines():  # reading file line by line
            line = line.split(",")  # splitting column in current line
            pat_id = line[4].strip("\"\'")  # removing "' in PATRIC ID if it presents
            if pat_id != "PATRIC ID":  # excluding header line
                freq[pat_id] = [0, []]  # declaring freq keys. 0 for count and [] for antibiotic names

    """reading other files and compare its PATRIC ID with reference file PATRIC ID"""
    for file in files:  # looping files in folder other than reference file
        antibiotic[os.path.splitext(file)[0]] = []
        with open(os.path.join(folder_name, file), "r") as file2:  # opening file in read mode
            for line in file2.readlines():  # reading file by line by line
                line = line.split(",")  # splitting column in current line
                pat_id = line[4].strip("\"\'")  # removing "' in PATRIC ID at ends if "' presents
                if pat_id != "PATRIC ID":  # excluding header line
                    if pat_id in freq.keys():  # checking current PATRIC ID in reference file PATRIC ID's
                        freq[pat_id][1].append(os.path.splitext(file)[0])  # updating file name in freq dictionary
                        freq[pat_id][0] += 1  # increasing count in freq dictionary
                        antibiotic[os.path.splitext(file)[0]].append(pat_id)

    def write_file(freq, path):
        """writing freq dictionary in new csv file"""
        with open(path, "w") as file3:  # opening output
            # file in w mode
            # write mode creates new file if it doesn't exists
            header = "PATRIC ID, FREQUENCY, ANTIBIOTICS NAMES,"
            file3.write(header + "\n")  # creating header
            for i in freq.keys():  # looping freq dictionary keys (PATRIC ID)
                file3.write("\"" + i + "\",")  # writing PATRIC ID in 1st column
                for j in freq[i]:  # looping values of freq dictionary(list of count and antibiotics name)
                    string1 = re.sub("'", "", str(j))  # after converting j into string, removing ' from j
                    string2 = "\"" + string1.strip("[]") + "\""  # after removing [] from ends, grouping string1 with "
                    # Reason: In csv if comma is detected it separates them into 2 columns. to avoid that we group them
                    # with " example: text1, text2 -> text1 is one column , text2 is another column "text1,
                    # text2" -> "text1, text2" are same column
                    file3.write(string2 + ",")  # separate column by comma
                file3.write("\n")  # separating row by \n

    write_file(freq, os.path.join(folder_name, "freq_of_" + comparison + "_strains.csv"))

