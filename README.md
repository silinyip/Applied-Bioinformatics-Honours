# Applied-Bioinformatics-Honours

## Python Introductory Course
Weekly tasks involving the use of Pandas, Numpy and Bash scripting. "Week 4" contains notebooks from a data science workshop which took place at UJ. These notebooks contained a lot of overlap with what I am expected to do. This Python Introductory Course served as preparation for my honours research project whereby various bioinformatics tools will be used to analyse cellular heterogeneity in normal vs. colorectal cancer tissue using single-cell RNA sequencing data.

## Single-Cell RNA Sequencing

### FASTQ Files Download
Sequence Read Archive (SRA) numbers of the PRJNA432551 dataset were organised into three text files: Normal Tissue, Primary Tumour, and Metastatic Tumour.
The "FASTQ Download (original script).py" script was used to download the data files deposited under this accession number from the EMBL-EBI website. This script made use of SRA Toolkit which allows direct access to SRA - a public repository for NGS data. Firstly, the `prefetch` command was used to download all the necessary files (namely SRA files). These SRA files are then converted to FASTQ format using the `fasterq-dump` command.
The parameters included in the "fasterq_dump` command were:
1) `--split-3` splits paired-end reads. First biological reads satisfying dumping conditions are placed in files *_1.fastq and *_2.fastq. If only one biological read is present it is placed in *.fastq.
2) `--threads` specifies the number of threads (parallel processes) that SRA toolkit can use for faster data retrieval.
3) `--skip-technical` is used to dump only biological reads, meaning the technical reads (such as the barcodes and primers) will not be downloaded.

The `fasterq-dump` command was used for the Normal Tissue, but the FASTQ files that were converted from SRA were unzipped. Thus, this was switched for the `fastq-dump` command which allows for the files to be zipped when converting.
The parameters included in the `fastq-dump` that were not present in the `fasterq-dump` command were:
1) `--gzip` compresses output using gzip.
2) `--readids` appends read id after spot id as "accession.spot.readid" on defline.
3) `--read-filter <[filter]>` splits into files by READ_FILTER value optionally filter by value: pass|reject|criteria|redacted.
4) `--dumpbase` formats sequence using base space (default for other than SOLiD).
5) `--clip` applies left and right clips since come of the sequences in the SRA contain tags that need to be removed.

`fasterq-dump` was opted for initially because it makes use of threads which speeds up the converting from SRA to FASTQ process faster, however, there is no gzip parameter meaning the files required too much space. Consequently, `fastq-dump` was used, albeit slower. An attempt was made to speed up the `fastq-dump` command by using the parallel `fastq-dump` wrapper. This tool speeds up the process by dividing the work into multiple threads. However, it is only functional in Linux or MacOS devices. The "Parallel FASTQ Dump.py" script was an attempt to run this tool in Windows which was unsuccessful. Thus, Windows Subsystem for Linux was installed on my Windows device which resulted in a successful run but the FASTQ file failed to save. Consequently, this approach was abandoned.

The PRJNA432551 dataset was later decided to be unsuitable for this project, so a new dataset deposited under the accession PRJEB64127 from the EMBL-EBI website was used. This new dataset does not have the SRA numbers available, only the FTP links. Thus, these links were downloaded as a TSV file from the EMBL-EBI website. The "Splitting PRJNA432551 FTP List (using pandas).py" script was used to split the "PRJNA432551.csv" file into the "split_data.csv"file. These links were then organised into two text files: Normal and Neoplasm.

The "FASTQ Download (using wget).py" script was used to download these files on the computer in GH527 which uses Linux. The "FASTQ Download (using iwr).py" script is the Windows version of the download script.

Once most of the FASTQ files have been downloaded, "FastQC Script (no. 2).py" was used to generate FastQC reports of each FASTQ file.

However, majority of the files from this dataset failed to generate FastQC reports. Consequently, the search for a new dataset was embarked upon. Finally, the dataset deposited under the accession PRJNA779978 was selected. This dataset was downloaded using the "fastq_download.py" script which incorporates the FASTQ download and FastQC generation processes in one script.

### FastQC


### MultiQC


### Cell Ranger


### Kallisto
