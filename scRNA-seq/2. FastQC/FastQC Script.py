#import os

#os.chdir(r"C:\Users\HP\Seagate\SILIN\PRJNA432551") #change to required directory

#def fastqc_analysis(fastqc_file_path):
 #   fastqc_command = r"C:\Users\HP\Downloads\AB Tools\FastQC>java -Xmx250m -classpath .;./sam-1.103.jar;./jbzip2-0.9.jar uk.ac.babraham.FastQC.FastQCApplication"


#import os

#def fastqc_analysis(fastq_file_path):

    #with open(sra_text_file) as file:
     #   sra_numbers = file.read().splitlines()

    #fastqc_command = r'C:\Users\HP\Downloads\AB Tools\FastQC\java -Xmx250m -classpath .;./sam-1.103.jar;./jbzip2-0.9.jar uk.ac.babraham.FastQC.FastQCApplication'
    #command = fastqc_command + ' ' + fastq_file_path

    #exit_code = os.system(command)

    #if exit_code == 0:
     #   print("Analysis complete for", fastq_file_path)
    #else:
     #   print("Error occurred during FastQC analysis")

# Example usage:
#fastq_file_path = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Normal_Tissue\SRA" + sra[3:]
#fastqc_analysis(fastq_file_path)




#import os

#def fastqc_analysis(fastq_file_path):
 #   fastqc_command = r'C:\Users\HP\Downloads\AB Tools\FastQC\java -Xmx250m -classpath .;./sam-1.103.jar;./jbzip2-0.9.jar uk.ac.babraham.FastQC.FastQCApplication'
  #  command = fastqc_command + ' ' + fastq_file_path

   # exit_code = os.system(command)

    #if exit_code == 0:
     #   print("Analysis complete for", fastq_file_path)
    #else:
     #   print("Error occurred during FastQC analysis")

#def analyze_fastq_files(directory_path):
 #   fastq_files = [file for file in os.listdir(directory_path) if file.lower().endswith('.fq') or file.lower().endswith('.fastq')]
  #  for fastq_file in fastq_files:
   #     fastq_file_path = os.path.join(directory_path, fastq_file)
    #    fastqc_analysis(fastq_file_path)

# Example usage:
#directory_path = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Normal_Tissue"
#analyze_fastq_files(directory_path)





import os

def fastqc_analysis(fastq_file_path, output_dir):
    fastqc_command = r'C:\Users\HP\Downloads\AB Tools\FastQC\java -Xmx250m -classpath .;./sam-1.103.jar;./jbzip2-0.9.jar uk.ac.babraham.FastQC.FastQCApplication'
    command = f'{fastqc_command} --outdir "{output_dir}" {fastq_file_path}'

    exit_code = os.system(command)

    if exit_code == 0:
        print("Analysis complete for", fastq_file_path)
    else:
        print("Error occurred during FastQC analysis")

def analyze_fastq_files(directory_path, output_dir):
    fastq_files = [file for file in os.listdir(directory_path) if file.lower().endswith('.fq') or file.lower().endswith('.fastq')]
    for fastq_file in fastq_files:
        fastq_file_path = os.path.join(directory_path, fastq_file)
        fastqc_analysis(fastq_file_path, output_dir)

directory_path = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Normal_Tissue"
output_dir = r"C:\Users\HP\Seagate\SILIN\PRJNA432551\Normal_Tissue"
analyze_fastq_files(directory_path, output_dir)
