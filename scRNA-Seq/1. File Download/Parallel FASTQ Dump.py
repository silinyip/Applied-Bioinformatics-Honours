import os

os.chdir(r"C:\Users\HP\Seagate\SILIN")  # Change to the required directory

try:
    os.makedirs("PRJNA432551")
except:
    pass

def sra_download(sra_text_file):
    with open(sra_text_file) as file:
        sra_numbers = file.read().splitlines()

    for sra in sra_numbers:
        print("Currently downloading: " + sra)
        prefetch = f"prefetch --max-size 60000000 {sra}"
        print("The command used was: " + prefetch)
        os.system(prefetch)
    
    os.chdir(r"C:\Users\HP\Seagate\SILIN\PRJNA432551")  # Change to the required directory
    
    for sra in sra_numbers:
        print("Generating FASTQ for: " + sra)
        try:
            os.makedirs(r"C:\Users\HP\Seagate\SILIN\PRJNA432551\1\SRA"+ sra[3:])
        except:
            pass
        outdir = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\1\SRA" + sra[3:]
        parallel_fastq_dump = f"parallel-fastq-dump --threads 8 --outdir {outdir} --skip-technical  --readids --read-filter pass --dumpbase --split-3 --clip --gzip " + sra
        print("The command used was: " + parallel_fastq_dump)
        os.system("sudo wsl")
        os.system("sudo conda activate parallel_fastq_dump")
        os.system(parallel_fastq_dump)
    
    return

sra_download(r"C:\Users\HP\Downloads\1.txt")  # Change text file to respective names for each cell type
