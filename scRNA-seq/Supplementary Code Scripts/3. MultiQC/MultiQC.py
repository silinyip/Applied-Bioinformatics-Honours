import os

def multiqc(directory_path):
    outdir = "C:\\Users\\HP\\Downloads\\FastQC"
    cmd = ("multiqc " + directory_path + " -o " + outdir)
    os.system(cmd)

multiqc("C:\\Users\\HP\\Downloads\\FastQC")