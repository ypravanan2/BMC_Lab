"""
--Separation of fasta sequences of genes of Acinetobacter Baumannii wrt length( as 169 & other)--
--Authors : Yatindrapravanan Narasimhan & Subachandran JK--
"""
import Ab_169_length
import Antibiotic as AB

Freq_dict = AB.freq.copy()
Antibiotic = AB.antibiotic.copy()
Ids = [str(j) for i in Ab_169_length.Id_Seq for j in i.keys()]
Seq = [str(j) for i in Ab_169_length.Id_Seq for j in i.values()]
Seq_dict = dict(zip(Ids, Seq))
length = len(Freq_dict.keys())
for i in list(Freq_dict.keys()).copy():
    if i not in Ids:
        del Freq_dict[i]
for i in list(Seq_dict.keys()):
    if i not in Freq_dict.keys():
        del Seq_dict[i]
Sequences = Seq_dict.values()

print(len(Freq_dict.keys()))
print(len(set(Sequences)))

for i in list(Antibiotic.keys()).copy():  # printing antibiotic wise
    for j in Antibiotic[i]:
        if j not in Freq_dict.keys():
            del Antibiotic[i][Antibiotic[i].index(j)]

Antibiotic_dict = {}
for i in list(Antibiotic.keys()).copy():
    count = len(Antibiotic[i])
    Antibiotic_dict[i] = count

with open("TMP-SMA_Antibiotic-wise_USA.csv", "w+") as yp_subi:
    head = "ANTIBIOTIC_NAME, COUNT"
    yp_subi.write(head + "\n")
    for i in Antibiotic_dict.keys():
        yp_subi.write("\"" + i + "\",\"" + str(Antibiotic_dict[i]) + "\"" + "\n")

AB.write_file(Freq_dict, "C:/Users/user/OneDrive/Desktop/python/Thamo Sir/Pakistan/169_TMP-SMA_USA.csv")

