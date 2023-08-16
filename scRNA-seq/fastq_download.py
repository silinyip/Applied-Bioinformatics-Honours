
#Written by: Lebohang Mashatola sc-RNA Seq Data Download using ftp

import os
import pandas as pd

df = pd.read_csv("/home/gh527/Downloads/filereport_read_run_PRJNA779978_tsv.txt", delimiter = "\t") #use delimiter for .txt files
print(df.columns)
print(df.head()) #preview document

samples_list = list(df["fastq_ftp"]) #sample ftp-links
sample_names_list = list(df["sample_accession"]) #sample labels
samples_list = samples_list[:5] #selecting first sample to test code, before commensing with large scale download

try:
    os.makedirs("/media/usb/SILIN/PRJNA779978") #avoid using os.chdir, type entire directory    

except:
    pass

def downloadfastq(samples_input):

    for i in range(0, len(samples_list)):

        samples = samples_list[i].split(";")  #i is a list of 3 samples that must be downloaded

        lbl = sample_names_list[i] 
        print(lbl) #double-check the sample name
        os.system("mkdir /media/usb/SILIN/PRJNA779978/" + lbl) #make directory for each sample
        
        for link in samples:
            
            print(link) #double-check the download link
            
            download_command = "wget -P /media/usb/SILIN/PRJNA779978/" + lbl + " " + link
            print(download_command) #double check wget command

            os.system(download_command) #execute


def run_fastqc(file_path):
    
    dir_list = os.listdir(file_path)
    print(dir_list) #check the filing system before you proceed
    dir_list.pop(0) #may/may not be necessary 

    for sample in dir_list:
        dir_ext = os.listdir(file_path + sample)  #list samples in each subfolder
        os.system("mkdir " + file_path + sample + "/QC") 
        
        for fastq_file in dir_ext:

            ext = "fastqc " + file_path + sample + "/" + fastq_file + " -o " + file_path + sample + "/QC" #write down the command
            print(ext) #check command prior to executing
            
            os.system(ext) #execute 


    
downloadfastq(samples_list) #All Files
run_fastqc("/media/usb/SILIN/PRJNA779978/")



    

