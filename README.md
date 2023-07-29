# Applied-Bioinformatics-Honours

## Python Introductory Course
Weekly tasks involving the use of Pandas, Numpy and Bash scripting. This serves as preparation for my honours research project whereby various bioinformatics tools will be used to analyse cellular heterogeneity in normal vs. colorectal cancer tissue using single-cell RNA sequencing data.

## Single-Cell RNA Sequencing

### Files Download
A Python script was used to download files from the EMBL-EBI website. Firstly, the `prefetch` command was used to download all the necessary files (such as the SRA files). These SRA files are then converted to FASTQ format using the `fasterq-dump` command.
Several parameters were included in the "fasterq_dump" line of code:
1) The `--split-3` command is used to split for mate-pairs. First biological reads satisfying dumping conditions are placed in files *_1.fastq and *_2.fastq. If only one biological read is present it is placed in *.fastq.
2) `--threads` specifies the number of threads (parallel processes) that SRA toolkit can use for faster data retrieval.
3) `--skip-technical` is used to dump only biological reads, meaning the technical reads (such as the barcodes and primers) will not be downloaded.
