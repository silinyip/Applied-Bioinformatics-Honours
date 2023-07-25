import os

os.chdir(r"C:\Users\HP\Downloads\temp")
os.makedirs("fastq")

def sra_download(sra_numbers):
    os.chdir(r"C:\Users\HP\Downloads\AB Tools\sratoolkit.3.0.6-win64\bin")

    for sra in sra_numbers:
        print("Currently downloading: " + sra)
        prefetch = "prefetch " + sra
        print("The command used was: " + prefetch)
        os.system(prefetch)
    
    os.chdir(r"C:\Users\HP\Downloads\temp\fastq")
    outdir = r"C:\Users\HP\Downloads\temp\fastq"
    for sra in sra_numbers:
        print("Generating FASTQ for: " + sra)
        fasterq_dump = f"fasterq-dump --outdir {outdir} --split-3 --threads 8 --skip-technical " + sra
        print("The command used was: " + fasterq_dump)
        os.system(fasterq_dump)
    
    return

sra_numbers = ["SRR25386374", "SRR25386377"]
sra_download(sra_numbers)