import os

os.chdir(r"C:\Users\HP\Seagate\SILIN") #change to required directory
try:
    os.makedirs("PRJNA432551")
except:
    pass

def sra_download(sra_text_file):
    #os.chdir(r"C:\Users\HP\Downloads\AB Tools\sratoolkit.3.0.6-win64\bin")     #don't need to specify

    with open(sra_text_file) as file:
        sra_numbers = file.read().splitlines()

    for sra in sra_numbers:
        print("Currently downloading: " + sra)
        prefetch = "prefetch --max-size 60000000 " + sra
        print("The command used was: " + prefetch)
        os.system(prefetch)
    
    os.chdir(r"C:\Users\HP\Seagate\SILIN\PRJNA432551") #change to required directory
    
    for sra in sra_numbers:
        print("Generating FASTQ for: " + sra)
        try:
            os.makedirs(r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Primary_Tumour\SRA"+ sra[3:]) #create a folder for each cell type - one at a time
        except:
            pass
        outdir = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Primary_Tumour\SRA" + sra[3:]
        #fasterq_dump = f"fasterq-dump --outdir {outdir} --split-3 --threads 8 --skip-technical " + sra     #this gives unzipped files which were too large so I switched to fastq-dump
        fastq_dump = f"fastq-dump --outdir {outdir} --gzip --skip-technical  --readids --read-filter pass --dumpbase --split-3 --clip " + sra
        print("The command used was: " + fastq_dump)
        os.system(fastq_dump)
    
    return

sra_download(r"C:\Users\HP\Downloads\Dataset\Primary_Tumour.txt") #change text file to respective names for each cell type