import os

os.chdir(r"C:\Users\HP\Seagate\SILIN") #change to required directory
try:
    os.makedirs("PRJEB64127")
except:
    pass

def fastq_download(ftp_text_file):
    os.chdir(r"C:\Users\HP\Seagate\SILIN\PRJEB64127")

    with open(ftp_text_file) as file:
        ftp_link = file.read().splitlines()

    for ftp in ftp_link:
        print("Currently downloading: " + ftp)
        try:
            os.makedirs(r"C:\Users\HP\Seagate\SILIN\PRJEB64127\EXT"+ ftp[52:55]) #create a folder for each cell type - one at a time
        except:
            pass
        outf = r"C:\Users\HP\Seagate\SILIN\PRJEB64127\EXT"+ ftp[52:55]
        iwr = f"iwr -outf {outf} " + ftp
        os.system(iwr)

        #return


#def rename_files():
    file_extensions = [".fastq.gz"]
    prefix = "F"
    number = 0

    for file in os.listdir(r"C:\Users\HP\Seagate\SILIN\PRJEB64127\EXT"+ ftp[52:55]):
        filename, file_extension = os.path.splitext(file)
        if file_extension in file_extensions:
            new_filename = prefix + str(number) + file_extension 
            os.rename(r"C:\Users\HP\Seagate\SILIN\PRJEB64127\EXT"+ ftp[52:55] + "/" + file, r"C:\Users\HP\Seagate\SILIN\PRJEB64127\ERR"+ ftp[37:45] + "/" + new_filename)     #path of the file to be renamed (the text before the comma), and path for new name of the file
            number += 1

    return

fastq_download(r"C:\Users\HP\Downloads\2.txt")