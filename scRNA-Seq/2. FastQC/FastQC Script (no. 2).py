import os
import glob

def fastqc(directory):
    os.chdir(directory)  # Change to the specified directory
    dirs_ = os.listdir(directory)
    dirs_.pop(0)

    for i in dirs_:
        os.chdir(os.path.join(directory, i))
        seq = [f for f in glob.glob("*.fastq.gz")]
        for file in seq:
            cmd = f"fastq -t 12 {os.path.join(directory, i, file)}"
            os.system(cmd)

# Call the function with the directory path
fastqc(r"C:\Users\HP\Downloads\AB Tools\FastQC>java -Xmx250m -classpath .;./sam-1.103.jar;./jbzip2-0.9.jar uk.ac.babraham.FastQC.FastQCApplication")
