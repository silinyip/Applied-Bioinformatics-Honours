import os
import pandas as pd

df = pd.read_csv("/home/gh527/Downloads/filereport_read_run_PRJNA779978_tsv.txt", delimiter="\t") #read the CSV file into a DataFrame
print(df.columns)
print(df.head()) #display columns and preview the first few rows

sample_names_list = list(df["run_accession"]) #extract sample names from the DataFrame
samples_list = sample_names_list[:]

directory = "C:\\Users\\HP\Downloads\\Kallisto" #set the directory path

try:
    os.system("mkdir " + directory) #create the directory if it doesn't exist
except:
    pass

ref_dir = "C:\\Users\\HP\\Downloads\\Kallisto\\Reference\\"
ref_path = "C:\\Users\\HP\\Downloads\\Kallisto\\Reference\\gencode.v44.transcripts.fa.gz"
t2g = "C:\\Users\\HP\\Downloads\\Kallisto\\Reference\\t2g.txt"
gtf = "C:\\Users\\HP\\Seagate\\SILIN\\yard\\run_cellranger_count\\refdata-gex-GRCh38-2020-A.tar.gz"

def kallisto_bustools(file_path):

    kb_ref = "kb ref -i " + ref_path + " -g " + t2g + " -f1 " + ref_dir + "cdna.fa" + ref_path + gtf #kb-ref command
    os.system(kb_ref)

    dir_list = os.listdir(file_path)
    print(dir_list)

    for sample in dir_list:  #iterate through samples
        dir_subf = os.listdir(file_path + sample)
        print(dir_subf)

        for fastq_file in dir_subf: #iterate through fastq files in each sample
            fastq_path = file_path + "/" + sample + "/" + fastq_file
            print(fastq_path)

            kb_count = "kb count -i " + ref_path + " -g " + t2g + " -x 10xv3 " + "-t 2 " + "-o " + directory + " " + fastq_path #kb-count command

            os.system(kb_count)

kallisto_bustools("C:\\Users\\HP\\Seagate\\SILIN\\PRJNA779978\\")


#kb ref -i transcriptome.idx -g transcripts_to_genes.txt -f1 cdna.fa dna.primary_assembly.fa.gz gtf.gz
#kb count -i index.idx -g t2g.txt -x 10xv2 --h5ad -t 2 read_1.fastq.gz read_2.fastq.gz





import os
import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Seagate\\SILIN\\filereport_read_run_PRJNA779978_tsv.txt", delimiter="\t")
sample_names_list = list(df["run_accession"])

directory = "C:\\Users\\HP\\Downloads\\Kallisto" #output directory path

try:
    os.system("mkdir " + directory) #create the directory if it doesn't exist
except:
    pass

#define paths to various reference files and directories
ref_dir = "C:\\Users\\HP\\Downloads\\Kallisto\\Reference\\"
ref_path = "C:\\Users\\HP\\Downloads\\Kallisto\\Reference\\gencode.v44.transcripts.fa.gz"
t2g = "C:\\Users\\HP\\Downloads\\Kallisto\\Reference\\t2g.txt"
gtf = "C:\\Users\\HP\\Seagate\\SILIN\\yard\\run_cellranger_count\\refdata-gex-GRCh38-2020-A.tar.gz"

def kallisto_bustools(file_path):
    kb_ref = ("kb ref -i " + ref_path + " -g " + t2g + " -f1 " + ref_dir + "cdna.fa " + ref_path + " " + gtf)  # kb-ref command
    os.system(kb_ref) #execute kb_ref command

    dir_list = os.listdir(file_path)
    print(dir_list)

    for sample in dir_list: #iterate through samples
        dir_subf = os.listdir(file_path + sample)
        print(dir_subf)

        for fastq_file in dir_subf: #iterate through fastq files in each sample
            fastq_path = os.path.join(file_path, sample, fastq_file)
            print(fastq_path)

            kb_count = ("kb count -i " + ref_path + " -g " + t2g + " -x 10xv3 -t 2 -o " + directory + " " + fastq_path)  # kb-count command
            os.system(kb_count) #execute kb_count command

kallisto_bustools("/home/gh527/Seagate/SILIN/PRJNA779978/")
