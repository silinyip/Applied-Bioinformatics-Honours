import os
import pandas as pd

df = pd.read_csv("/home/gh527/Downloads/filereport_read_run_PRJNA779978_tsv.txt", delimiter="\t")
sample_names_list = list(df["run_accession"])

kb_directory = "/media/usb/SILIN/Kallisto" #output directory path
fastq_dirs = "/media/usb/SILIN/PRJNA779978/" #path to FASTQ files
ref_dirs = "/home/gh527/Downloads/kallisto_index/transcriptome.idx" # path to reference transcriptome
outdir = "/media/usb/SILIN/Kallisto" #output directory

try:
    os.system("mkdir " + kb_directory) #create the directory if it doesn't exist
except:
    pass

#sample_id = ""

#fastqs = ""

outdir = "/media/usb/SILIN/Kallisto" #output directory

ref_path = "/home/gh527/Downloads/kallisto_index/transcriptome.idx" #path to reference transcriptome
t2g = "/media/usb/SILIN/Kallisto/Reference/t2g.txt" #path to t2g file downloaded from https://github.com/pachterlab/kallisto-transcriptome-indices/releases

read1 = "_1"
read2 = "_2"

def kb_count(file_path):
    dir_list = os.listdir(file_path)
    print(dir_list)

    for sample in dir_list: #iterate through samples
        dir_subf = os.listdir(file_path + sample)
        print(dir_subf)
        sample_id = dir_subf

        #for fastq_file in dir_subf: #iterate through fastq files in each sample
            #fastq_path = file_path + "/" + sample + "/" + fastq_file
            #print(fastq_path)

        for fastq_file in dir_subf:
            if fastq_file[12:14] == read1:
                fastq_path1 = file_path + "/" + sample + "/" + fastq_file
                print (fastq_path1)
            elif fastq_file[12:14] == read2:
                fastq_path2 = file_path + "/" + sample + "/" + fastq_file
                print(fastq_path2)

            kb_count = ("kb count -i " + ref_dirs + " -g " + t2g + " -x 10xv3 --h5ad -t 2 -o " + outdir + " " + fastq_path1 + " " + fastq_path2)  # kb-count command
            os.system(kb_count) #execute kb_count command

kb_count("/media/usb/SILIN/PRJNA779978/")

#kb_count = "kb count -i " + ref_path + " -g " + t2g + " -x 10xv3 --h5ad -t 2 -o " + outdir + " " + fastq_path  # kb-count command

#for fastq_file in dir_subf:
    #if fastq_file[12:14] == read1:
        #fastq_path1 = file_path + "/" + sample + "/" + fastq_file
        #print (fastq_path1)
    #elif fastq_file[12:14] == read2:
        #fastq_path2 = file_path + "/" + sample + "/" + fastq_file
        #print(fastq_path2)