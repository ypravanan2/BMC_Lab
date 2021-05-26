"""
--Separation of fasta sequences of genes of Acinetobacter Baumannii wrt length( as 169 & other)--
--Yatindrapravanan Narasimhan--
--27-Mar-21--
"""


def seq_len():
    from Bio import SeqIO  # to read and extract
    import csv  # to write
    import os  # to read and write multiple files of a folder_name

    path = 'C:/Users/user/OneDrive/Desktop/python/Thamo Sir/Pakistan/FASTA (1)'  # Change the text inside the '' as per your folder_name
    temp = path.split("/")
    out_dir1 = temp[-1]  # To create output folder_name (in line 21)
    out_d2 = []
    print(out_dir1)
    for i in range(0, len(temp)-1):
        od2 = temp[i] + '/'
        out_d2.append(od2)
    out_dir2 = "".join(out_d2)  # out_dir2 contains the path till folder_name (in line 21)

    in_dir = path + '//'  # for using a comparison instead of the direct name of the input folder_name (in line 23)
    path_wrt = out_dir2 + out_dir1 + '_Output'
    print(path_wrt)
    if not os.path.exists(path_wrt):  # Make the output directory when it doesn't exist
        os.mkdir(path_wrt)

    filenames = os.listdir(path)
    for n in filenames:
        filename_write = n[:-6:]  # Remove .fasta from listed file names, for naming files to write the info.
        filename_read = in_dir + n
        print(filename_read)
        #Reading fasta file and extracting info such as Id, Seq, and Length
        out_169, out_not_169 = [], []
        for record in SeqIO.parse(filename_read, 'fasta'):
            if len(record.seq) == 169:  # Storing info of sequences with seq.len. 169 in out_169
                Seq_169 = str(record.seq)
                Id_169 = str(record.id)
                out_169.append(Id_169)
                out_169.append(Seq_169)
            else:  # Storing info of sequences with various seq.len. other than 169 in out_not_169
                Seq = str(record.seq)
                Id = str(record.id)
                Len = str(len(record.seq))
                out_not_169.append(Id)
                out_not_169.append(Seq)
                out_not_169.append(Len)

        # Displaying primary info for the user
        if __name__ == '__main__':
            print("\n" + filename_write + ":")
            print("There are", int(len(out_169) / 2),
                  'sequences having seq. length = 169, and these are written in "' + filename_write + '_len_169.csv".')
            print("There are", int(len(out_not_169) / 3),
                  'sequences NOT having seq. length = 169, and these are written in "' + filename_write + '_len_not_169.csv".')

        # Writing the extracted info as a csv file
        with open(path_wrt + "/" + filename_write + '_len_169.csv', 'w') as output_yp:
            cols = ['ID', 'Sequence']
            writer = csv.writer(output_yp)
            writer.writerow(cols)
            for i in range(0, len(out_169), 2):
                writer.writerow(out_169[i:i + 2])

        with open(path_wrt + "/" + filename_write + '_len_not_169.csv', 'w') as output_yp:
            cols = ['ID', 'Sequence', 'Length']
            writer = csv.writer(output_yp)
            writer.writerow(cols)
            for i in range(0, len(out_not_169), 3):
                writer.writerow(out_not_169[i:i + 3])

seq_len()
