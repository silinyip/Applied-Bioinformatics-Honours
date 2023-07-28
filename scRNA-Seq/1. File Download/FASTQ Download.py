import os

os.chdir(r"C:\Users\HP\Seagate\SILIN") #change to required directory
try:
    os.makedirs("PRJNA432551")
except:
    pass

def sra_download(sra_text_file):
    #os.chdir(r"C:\Users\HP\Downloads\AB Tools\sratoolkit.3.0.6-win64\bin") - don't need to specify

    with open(sra_text_file) as file:
        sra_numbers = file.read().splitlines()

    for sra in sra_numbers:
        print("Currently downloading: " + sra)
        prefetch = "prefetch --max-size 50000000 " + sra
        print("The command used was: " + prefetch)
        os.system(prefetch)
    
    os.chdir(r"C:\Users\HP\Seagate\SILIN\PRJNA432551") #change to required directory
    #outdir = r"C:\Users\HP\Downloads\temp\fastq"
    for sra in sra_numbers:
        print("Generating FASTQ for: " + sra)
        os.makedirs(r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Normal_Tissue\SRA"+ sra[3:]) #create a folder for each cell type - one at a time
        outdir = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Normal_Tissue\SRA" + sra[3:]
        fasterq_dump = f"fasterq-dump --outdir {outdir} --split-3 --threads 8 --skip-technical " + sra
        print("The command used was: " + fasterq_dump)
        os.system(fasterq_dump)
    
    return

#sra_numbers = ["SRR25424443", "SRR25386374"]
#sra_download(sra_numbers)
sra_download(r"C:\Users\HP\Downloads\Dataset\Normal_Tissue.txt") #change text file to respective names for each cell type