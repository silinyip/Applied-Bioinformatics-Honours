import os

os.system("cd /Users/HP/Downloads/TEST") #change the directory to Seagate
try:
    os.system("mkdir fastq") #maybe change this to PRJNA432551
except:
    pass

def sra_download(sra_text_file):
    #os.chdir(r"C:\Users\HP\Downloads\AB Tools\sratoolkit.3.0.6-win64\bin") #don't need to specify

    with open(sra_text_file) as file:
        sra_numbers = file.read().splitlines()
    
    for sra in sra_numbers:
        print("Currently downloading: " + sra)
        out = "/Users/HP/Downloads/TEST/sra/"
        prefetch = "prefetch --max-size 50000000 " + sra + " -O " + out + sra + '.sra'
        #prefetch = "prefetch --max-size 50000000 " + sra
        print("The command used was: " + prefetch)
        os.system(prefetch)

sra_download(r"C:\Users\HP\Downloads\1.txt") #change text file to respective names for each cell type

def fastq_download():
    os.system("cd /Users/HP/Seagate/SILIN/fastq") #change directory to Seagate
    #os.makedirs("PRJNA432551") #create a folder for each cell type - one at a time
    for sra in sra_numbers:
        print("Generating FASTQ for: " + sra)
        os.system("mkdir /Users/HP/Seagate/SILIN/fastq/"+ sra)
        outdir = "/Users/HP/Seagate/SILIN/fastq/" + sra
        fasterq_dump = f"fasterq-dump --outdir " + outdir + "--split-3 --threads 8 --skip-technical " + out
        print("The command used was: " + fasterq_dump)
        os.system(fasterq_dump)
    
    return

#sra_numbers = ["SRR25424443", "SRR25386374"]
sra_download(r"C:\Users\HP\Downloads\1.txt") #change text file to respective names for each cell type
fastq_download()