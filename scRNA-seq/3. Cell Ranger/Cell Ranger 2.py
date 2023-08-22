import os
import pandas as pd

df = pd.read_csv("/home/gh527/Downloads/filereport_read_run_PRJNA779978_tsv.txt", delimiter="\t") #read the CSV file into a DataFrame
print(df.columns)
print(df.head()) #display columns and preview the first few rows

sample_names_list = list(df["run_accession"]) #extract sample names from the DataFrame
samples_list = sample_names_list[:]

directory = "/media/usb/SILIN/yard/run_cellranger_count" #set the directory path

try:
    os.system("mkdir " + directory) #create the directory if it doesn't exist
except:
    pass

ref_link = "https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz" #link to 10x Genomics human reference
ref_file_name = ref_link.split("/")[-1] #extract reference file name from the link
ref_name = ref_file_name.split(".")[-3]

ref_path = directory + "/" + ref_file_name

if not os.path.exists(ref_path):
    os.system("wget -P " + directory + " " + ref_link) #downloading the reference to target directory
    os.system("tar -zxvf " + directory + "/" + ref_file_name + " -C " + directory) #decompressing the reference file into specific directory

os.system("cd " + directory) #change the working directory to the target directory

def cellranger_count(file_path): #function to perform cellranger count analysis
    dir_list = os.listdir(file_path)
    print(dir_list)

    for sample in dir_list:  #iterate through samples
        dir_subf = os.listdir(file_path + sample)
        print(dir_subf)

        for fastq_file in dir_subf: #iterate through fastq files in each sample
            fastq_path = file_path + "/" + sample + "/" + fastq_file
            print(fastq_path)

            lbl = sample
            print(lbl)
            reference = directory + "/" + ref_name  #set reference variable
            print(reference)

            cmd = "/home/gh527/cellranger-7.1.0/bin/cellranger count --id=" + lbl + " --transcriptome=" + reference + " --fastqs=" + fastq_path #+ " --sample=" + lbl #command for cellranger count
            print(cmd)

            os.system(cmd) #execute the cellranger count command

cellranger_count("/media/usb/SILIN/PRJNA779978/") #call the cellranger_count function on your specified path