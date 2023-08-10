# Applied-Bioinformatics-Honours

## Python Introductory Course
Weekly tasks involving the use of Pandas, Numpy and Bash scripting. This serves as preparation for my honours research project whereby various bioinformatics tools will be used to analyse cellular heterogeneity in normal vs. colorectal cancer tissue using single-cell RNA sequencing data.

## Single-Cell RNA Sequencing

### Files Download
SRA numbers of the PRJNA432551 dataset were organised into three text files: Normal Tissue, Primary Tumour, and Metastatic Tumour.
The "FASTQ Download (original script).py" script was used to download the data files deposited under this accession number from the EMBL-EBI website. Firstly, the `prefetch` command was used to download all the necessary files (namely SRA files). These SRA files are then converted to FASTQ format using the `fasterq-dump` command.
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

`fasterq-dump` was opted for initially because it makes use of threads which speeds up the converting from SRA to FASTQ process faster, however, there is no gzip parameter meaning the files required too much space. Consequently, `fastq-dump` was used, albeit slower.

The PRJNA432551 dataset was later decided to be unsuitable for this project, so a new dataset deposited under the accession PRJEB64127 from the EMBL-EBI website was used. This new dataset does not have the SRA numbers available, only the FTP links. Thus, these links were organised into two text files: Normal and Neoplasm.

The "FASTQ Download (using wget).py" script was used to download these files in Linux on the computer in GH527. The "FASTQ Download (using iwr).py" script is the Windows version of the download script.
