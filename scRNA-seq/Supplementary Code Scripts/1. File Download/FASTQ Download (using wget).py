import os

os.chdir("/media/gh527/Seagate/SILIN")          #change to required directory
try:
    os.makedirs("PRJEB64127")          #name of the dataset
except:
    pass

#downloading FASTQ files using wget on Linux
def fastq_download(ftp_text_file):
    os.chdir("/media/gh527/Seagate/SILIN/PRJEB64127")

    with open(ftp_text_file) as file:          #opens file specified by the "ftp_text_file" variable and assigns it to the variable "file"
        ftp_link = file.read().splitlines()    #"file.read" reads the entire content of the file as a single string, "split.lines" then splits the string into a list of lines

    for ftp in ftp_link:
        print("Currently downloading: " + ftp)
        try:
            os.makedirs("/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + ftp[52:55])          #create a folder for each cell type - one at a time
        except:
            pass
        outf = "/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + ftp[52:55]
        data_download = "wget -P " + outf + " " + ftp          #wget Linus command
        os.system(data_download)
        print(data_download)

    return

fastq_download("media/gh527/Seagate/SILIN/Dataset/Neoplasm.txt")          #to download the normal tissues files, just replace "Neoplasm" with "Normal"


#unsuccessful attempts at renaming the downloaded files
#def rename_files():
    #file_extensions = [".fastq.gz"]
    #prefix = "F"
    #number = 0

    #for file in os.listdir("/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + ftp[52:55]):
        #filename, file_extension = os.path.splitext(file)
        #if file_extension in file_extensions:
            #new_filename = prefix + str(number) + file_extension 
            #os.rename("/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + ftp[52:55] + "/" + file, "/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + ftp[37:45] + "/" + new_filename)     #path of the file to be renamed (the text before the comma), and path for new name of the file
            #number += 1

    #return


#def rename_files():
    #file_extensions = [".fastq.gz"]
    #prefix = "F"
    #number = 0

    #with open("/media/gh527/Seagate/SILIN/2.txt") as file:
        #ftp_link = file.read().splitlines()

    #for ftp in ftp_link:
        #folder_part = ftp[52:55]
        #filename_part = ftp[37:45]

        #for file in os.listdir("/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + folder_part):
            #filename, file_extension = os.path.splitext(file)
            #if file_extension in file_extensions:
                #new_filename = f"{prefix}{number}{file_extension}"
                #os.rename(
                    #os.path.join("/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + folder_part, file),
                    #os.path.join("/media/gh527/Seagate/SILIN/PRJEB64127/EXT" + filename_part, new_filename)
                #)
                #number += 1

    #return