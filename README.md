# Applied-Bioinformatics-Honours

## Python Introductory Course
Weekly tasks involving the use of Pandas, Numpy and Bash scripting. "Week 4" contains notebooks from a data science workshop which took place at UJ. These notebooks contained a lot of overlap with what I am expected to do. This Python Introductory Course served as preparation for my honours research project whereby various bioinformatics tools will be used to analyse cellular heterogeneity in normal vs. colorectal cancer tissue using single-cell RNA sequencing data.

## Single-Cell RNA Sequencing

### 1. FASTQ Files Download & 2. FastQC
#### PRJNA432551 (Dataset 1)
Sequence Read Archive (SRA) numbers of the PRJNA432551 dataset were organised into three text files: Normal Tissue, Primary Tumour, and Metastatic Tumour.
This [script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Supplementary%20Code%20Scripts/1.%20File%20Download/FASTQ%20Download%20(original%20script).py) was used to download the data files deposited under this accession number from the EMBL-EBI website. This script made use of SRA Toolkit which allows direct access to SRA - a public repository for NGS data. Firstly, the `prefetch` command was used to download all the necessary files (namely SRA files). These SRA files are then converted to FASTQ format using the `fasterq-dump` command.
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

`fasterq-dump` was opted for initially because it makes use of threads which speeds up the converting from SRA to FASTQ process faster, however, there is no gzip parameter meaning the files required too much space. Consequently, `fastq-dump` was used, albeit slower. An attempt was made to speed up the `fastq-dump` command by using the parallel `fastq-dump` wrapper. This tool speeds up the process by dividing the work into multiple threads. However, it is only functional in Linux or MacOS devices. The ["Parallel FASTQ Dump" script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Supplementary%20Code%20Scripts/1.%20File%20Download/Parallel%20FASTQ%20Dump.py) was an attempt to run this tool in Windows which was unsuccessful. Thus, Windows Subsystem for Linux was installed on my Windows device which resulted in a successful run but the FASTQ file failed to save. Consequently, this approach was abandoned.

#### PRJEB64127 (Dataset 2)
The PRJNA432551 dataset was later decided to be unsuitable for this project as it used STRT-seq instead of the 10x Genomics technology, so a new dataset deposited under the accession PRJEB64127 from the EMBL-EBI website was used. This new dataset does not have the SRA numbers available, only the FTP links. Thus, these links were downloaded as a TSV file from the EMBL-EBI website. This [script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Supplementary%20Code%20Scripts/1.%20File%20Download/Splitting%20PRJEB64127%20FTP%20List%20(using%20pandas).py) was used to split the "PRJNA432551.csv" file into the "split_data.csv"file. These links were then organised into two text files: Normal and Neoplasm.

The ["FASTQ Download (using wget)"](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Supplementary%20Code%20Scripts/1.%20File%20Download/FASTQ%20Download%20(using%20wget).py) script was used to download these files on the computer in GH527 which uses Linux. The "FASTQ Download (using iwr).py" script is the Windows version of the download script.

Once most of the FASTQ files have been downloaded, this [FastQC script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Supplementary%20Code%20Scripts/2.%20FastQC/FastQC%20Script%202.py) was used to generate FastQC reports of each FASTQ file.

However, majority of the files from this dataset failed to generate FastQC reports. Consequently, the search for a new dataset was embarked upon. 

#### PRJNA779978 (Dataset 3)
Finally, the dataset deposited under the accession PRJNA779978 was selected. This dataset consists of left and right-sided colorectal cancer samples. This dataset was downloaded using this [script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Final%20Code%20Scripts/Script%201%20-%20FASTQ%20Download%20%26%20FastQC.py) which incorporates the FASTQ download and FastQC generation processes in one script. These reports were summarised into one report using a [MultiQC script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Final%20Code%20Scripts/Script%202%20-%20MultiQC.py) in a Windows system to allow for easier analysis.

Only 2/6 samples were used in this project due to time constraints. Furthermore, not all the files used in this project were able to generate FastQC reports. Ideally, the files used in the downstream analyses should be those that were able to generate FastQC reports but, once again, due to time constraints, instructions were given to use even the files that failed to generate FastQC reports.
| Patient     | Sample Accession | Run Accession | FastQC Generated |
|-------------|------------------|---------------|------------------|
| Left CRC 1  | SAMN23098192     | SRR16931960   | Both reads       |
|             |                  | SRR16931961   |                  |
|             |                  | SRR16931966   | Read 1           |
|             |                  | SRR16931967   |                  |
| Right CRC 1 | SAMN23098196     | SRR16931983   | Read 1           |
|             |                  | SRR16931981   | Read 2           |
|             |                  | SRR16931982   |                  |
|             |                  | SRR16931984   |                  |
|             |                  | SRR16931987   |                  |
|             |                  | SRR16931985   | Read 2           |

MultiQC was then used to combine all the FastQC reports generated for this dataset into one report for easier analysis.

### 3. Cell Ranger
Cell Ranger is the standard tool for 10x Genomics data so Cell Ranger was initially selected to perform alignment. Cell Ranger was downloaded on the computer in GH527 as it only runs on a Linux system. This [script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Supplementary%20Code%20Scripts/4.%20Cell%20Ranger/Cell%20Ranger%202.py) was used. The `cellranger count` command was used in this script which takes FASTQ files and performs alignment. The [10x Genomics reference sequence](https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz), available from the 10x Genomics website, was used. However, when this script was run, several errors were encountered. Cell Ranger was unable to locate the downloaded FASTQ files. Furthermore, Cell Ranger relies on the computationally intensive alignment tool, STAR. Thus, the Cell Ranger approach was abandoned due to the failure to locate the downloaded FASTQ files and the lack of facilities to run this computationally intensive tool.

### 4. Kallisto
Hence, Kallisto, a faster and less computationally intensive alignment tool, was opted for. Kallisto is compatible with all the operating systems. For this project, Kallisto was installed on the GH527 computer. Firstly, a transcriptome index using the [_Homo sapiens_ Ensembl transcriptome](https://github.com/pachterlab/kallisto-transcriptome-indices/releases) was built in the Linux command line. This [script](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Final%20Code%20Scripts/Script%203%20-%20Kallisto.py) was used to align the two samples to the reference transcriptome. This script consisted of kb|python commands - a package which wraps the kallisto|bustools workflow for scRNA-seq into two simple commands. The kb-python commands are: `kb ref` and `kb count`. Since a reference transcriptome has been built already in the Linux command line, `kb ref` was ommited from this script as this command is used to build a reference. Thus, only `kb count` was used in the script. The `kb count` command aligns the FASTQ files to the reference sequence and generates various files containing important information pertaining to the quality of the alignment.

### 5. Normalisation and Clustering
Finally, normalisation and clustering were performed for the [left](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Final%20Code%20Scripts/Script%204%20-%20Left%20CRC.ipynb) and [right](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Final%20Code%20Scripts/Script%205%20-%20Right%20CRC.ipynb)-sided colorectal cancer samples as well as [both samples](https://github.com/silinyip/Applied-Bioinformatics-Honours/blob/master/scRNA-seq/Final%20Code%20Scripts/Script%206%20-%20Both%20Samples.ipynb) combined. Before this can be done, modules and libraries must be imported. Thereafter, further quality control was performed which essentially filters out low quality cells. The total-count was then normalised to 10,000 reads per cell so that counts become comparable among cells. Highly-variable genes were identified. This was important as highly variable genes are often used in downstream analysis steps such as dimensionality reduction and clustering. Next, principle component analysis (PCA) was performed to reduce the dimensionality of the data and the individual principle components (PC) were visualised to investigate the contribution of each individual PC to the total variance in the data. Lastly, the Uniform Manifold Approximation and Projection (UMAP) plots were generated to allow for visualisation of the different cell populations present in the two samples.
