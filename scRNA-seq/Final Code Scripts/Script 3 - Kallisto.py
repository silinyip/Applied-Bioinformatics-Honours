import os
import pandas as pd


df = pd.read_csv("/home/gh527/Downloads/filereport_read_run_PRJNA779978_tsv.txt", delimiter="\t") #read data from a CSV file into a DataFrame
sample_names_list = list(df["run_accession"]) #extract a list of sample names from the DataFrame


#define paths for various directories and files
kb_directory = "/media/usb/SILIN/Kallisto"  #uutput directory path
fastq_dirs = "/media/usb/SILIN/PRJNA779978/"  #path to FASTQ files
ref_dirs = "/home/gh527/Downloads/kallisto_index/transcriptome.idx"  #path to reference transcriptome
#outdir = "/media/usb/SILIN/Kallisto"  #output directory for aligning all the samples at once - so one output file
t2g = "/media/usb/SILIN/Kallisto/Reference/t2g.txt"  #path to t2g file downloaded from a repository
read1 = "_1"  #read 1 files
read2 = "_2"  #read 2 files


try: #try to create the output directory if it doesn't exist
    os.makedirs(kb_directory)
except FileExistsError:
    pass


def kb_count(file_path): #function to perform the kb count operation
    dir_list = os.listdir(file_path) #get the list of items (subdirectories and files) in the given directory
    print(dir_list)

    for sample in dir_list: #iterate through each item in the directory list
        dir_subf = os.listdir(file_path + sample) #get the list of items in the subdirectory corresponding to a sample
        print(dir_subf)

        outdir = "/media/usb/SILIN/Kallisto/" + sample #create an output directory for each sample - so aligning each sample separately

        #initialize variables to store FASTQ file paths for read 1 and read 2
        fastq_path1 = None
        fastq_path2 = None

        for fastq_file in dir_subf: #iterate through each file in the subdirectory
            if fastq_file[11:13] == read1: #check if the file corresponds to read 1
                fastq_path1 = file_path + "/" + sample + "/" + fastq_file
                print(fastq_path1)
            elif fastq_file[11:13] == read2: #check if the file corresponds to read 2
                fastq_path2 = file_path + "/" + sample + "/" + fastq_file
                print(fastq_path2)

        if fastq_path1 and fastq_path2: #check if both read 1 and read 2 FASTQ files are found
            #construct the kb count command
            kb_count_command = ("kb count -i " + ref_dirs + " -g " + t2g + " -x 10xv3 --h5ad --overwrite -t 2 -o " + outdir + " " + fastq_path1 + " " + fastq_path2)
            os.system(kb_count_command) #execute the kb count command

kb_count("/media/usb/SILIN/PRJNA779978/") #call the kb_count function with the specified directory containing FASTQ files
