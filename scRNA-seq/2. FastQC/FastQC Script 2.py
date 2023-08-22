import os
#import glob

directory = "/media/gh527/Seagate/SILIN/PRJEB64127/Neoplasm/"          #change "Neoplasm" to specified directory
dir_list = os.listdir(directory)

def fastqc():
    #os.chdir("/media/gh527/Seagate/SILIN/PRJEB64127/Neoplasm/EXT" +ftp[52:55])  # Change to the specified directory
    #dir_list = os.listdir(directory)
    #dirs.pop(0)

    for i in dir_list:
        dir_ext = os.listdir(directory + i)
        for file in dir_ext:
            ext = "fastqc /media/gh527/Seagate/SILIN/PRJEB64127/Neoplasm/" + i + "/" + file
            os.system(ext)
    
    return

fastqc()



        #os.chdir(os.path.join(directory, i))
        #seq = [f for f in glob.glob("*.fastq.gz")]
        #for file in seq:
            #cmd = f"fastqc -t 12 {os.path.join(directory, i, file)}"
            #os.system(cmd)

# Call the function with the directory path
#fastqc("~/Downloads/fastqc_v0.11.9/FastQC/fastqc")