#!/bin/bash

# make output directory
mkdir -p results/cellranger

# change into that directory
cd results/cellranger

# run cellranger count (maximum CPUs 8; maximum RAM 24GB)
cellranger count --id=ETV6_RUNX1_rep1 \
                 --transcriptome=../../Data/reference/cellranger_index \
                 --fastqs=../../Data/reads/ \
                 --sample=SRR9264343 \
                 --localcores=8 \
                 --localmem=24

# If we save this script in our scripts folder as 02-cellranger.sh, we could then run it from the terminal with:
# $ bash scripts/02-cellranger.sh