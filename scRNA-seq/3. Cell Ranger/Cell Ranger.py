import os
import pandas as pd

df = pd.read_csv("/home/gh527/Downloads/filereport_read_run_PRJNA779978_tsv.txt", delimiter = "\t") #use delimiter for .txt files
print(df.columns)
print(df.head()) #preview document

sample_names_list = list(df["run_accession"]) #sample labels
samples_list = samples_list[0:] #selecting first sample to test code, before commensing with large scale download


directory = "/media/usb/SILIN/yard/run_cellranger_count"
reference = "/media/usb/SILIN/yard/run_cellranger_count/" + {reference_name}

try:
    os.system("mkdir " + directory) #making a directory to run the analysis in
except:
    pass

os.system("cd " + directory) #navigating to the newly created directory

def cellranger_count(file_path):
    dir_list = os.system("ls " + file_path)
    print(dir_list)

    for sample in dir_list:
        dir_subf = os.system("ls " + file_path + sample)
        print(dir_subf)

        for fastq_file in dir_subf:
            fastq_path = "/media/usb/SILIN/yard/run_cellranger_count" + "/" + fastq_file
            print(fastq_path)

    for i in range(0, len(samples_list)):

        lbl = sample_names_list[i]
        print(lbl) #double-check the sample name
        
    cmd = "cellranger count --id=sample_names_list \
                            --transcriptome=reference \
                            --fastqs=fastq_path \
                            --sample=lbl"
    
    os.system(cmd)

cellranger_count("/media/usb/SILIN/PRJNA779978/")


#cellranger count --id={OUTPUT_SAMPLE_NAME} \ #creates an output directory that is named using this id
#                 --transcriptome={DIRECTORY_WITH_REFERENCE} \ #path to the Cell Ranger-compatible transcriptome reference
#                 --fastqs={DIRECTORY_WITH_FASTQ_FILES} \ #path to the directory containing the FASTQ files
#                 --sample={NAME_OF_SAMPLE_IN_FASTQ_FILES} \ #specify which samples to use - works off of the sample id at the beginning of the FASTQ file name
#                 --localcores={NUMBER_OF_CPUS} \
#                 --localmem={RAM_MEMORY}