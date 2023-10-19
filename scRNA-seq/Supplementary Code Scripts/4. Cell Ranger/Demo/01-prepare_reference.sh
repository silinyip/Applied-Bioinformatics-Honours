#!/bin/bash

# change to directory with the FASTA and GTF files
cd Data/reference/

# run mkref
cellranger mkref \
  --nthreads=8 \
  --genome=cellranger_index \
  --fasta=Homo_sapiens.GRCh38.dna.chromosome.21.fa \
  --genes=Homo_sapiens.GRCh38.104.chr21.gtf

# If we save this script in our scripts folder as 01-prepare_reference.sh, we could then run it from the terminal with:
# $ bash scripts/01-prepare_reference.sh