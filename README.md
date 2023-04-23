# Supplementary Computational Methods for "Functionalizing uncharacterized conjugative systems from metagenomic data for targeted delivery of Cas9"

## Table of contents

This Readme will have the workflow below the TOC

Bin folder contains scripts used within the project


In this Readme, you will find the workflow necessary for recapitulating the workflow I used to generate the bioinformatic results in the paper. Unfortunately, these methods span back over four years, and involve a number of disjointed processes, so there is no master script for running the methodology. Additionally, the process of annotating the genome set using the UniRef90 is lengthy, so I suggest testing it on a subset.

System information:

I ran these processes on a Linux server with aIntel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz processor and 256GB of RAM.

Run in a conda environment with the following programs installed:
- bowtie2
- anvi'o
- metaSPAdes
- bowtie2
- SRA toolkit
- Trimmomatic
- Prodigal
- Diamond
- metabat2
- checkm
- PlasFlow
- dRep
- MOB suite
- CAT/BAT (with databases installed)

**Note, there's a high chance that not all programs can be resolved in same environment.  I used separate environments for anvi'o and MOB Suite/PlasFlow than the other prgrams**

Installed outside conda environment:
- dedupe (used in scripts for downloading and processing reads, change install location in scripts)
- kaiju (need to edit location of kaiju install and nodes files)

## Step-by-Step Workflow (run from bin folder)

### Section 1: Download and annotate the gut genome database

**STEP 1:**
`./genome_download.sh`

* downloads the genomes from EBI FTP site via wget
* genomes from: https://doi.org/10.1038/s41586-019-0965-1
* reformats the fasta headers to replace tab whitespace with underscores
* downloads taxonomy table to extend information in fasta headers
* extends fasta headers with taxonomy info and saves to `../genomes` folder

**STEP 2:**
`./genome_annotation.sh`

**NOTE:** Prodigal and Diamond must be in PATH to run script as is, otherwise, call install location on your workstation
* the script first predicts the open reading frames using Prodigal
* the UniRef90 database must be downloaded and placed in `../uniref` (relative to bin)
* script replaces white space with a colon to avoid truncation with Diamond
* Diamond db is made using the UniRef90 database
* Open reading frames are aligned against UniRef90 database with BLASTP module of Diamond
* max 10 matches with a bitscore higher than 30 will be output to `../diamond_output`

### Section 2: Identify Conjugative Systems using annotations

`./conj_db_master.sh`
* I apologize in advance for the naming conventions
* will run a suite of `.sh`/`.py` scripts
* identifies potential conjugative systems based on word search strategies for relaxases and T4SS/T4CP annotations, outputs of .faa.contigs (.m8 annotations), .faa.orfs.fa (protein sequences), .fa.DNA.fa (DNA sequences) in `../conjugative_contigs/`
* finds the most frequent/best annotations for each ORF and outputs to `../conjugative_contigs/*.txt`
* gets the lengths of conjugative contigs, output in `../summary_data/contiglengths` and `../summary_data/`
* gets frequencies of all gene annotations across all the genomes, output in `../summary_data/geneFreq.txt`
* gets frequencies of conjugative protein annotations on identified contigs, output in `../summary_data/conjCount.txt` and `../summary_data/conjCountsAndLengths.txt`
* outputs .tsv files of the annotations for each identified contig, highlighting conjugative proteins, output in `../annotation_tables/`
* extracts regions containing conjugative systems from the contigs. This is explicitly to avoid potential issues of measuring average mapping frequencies of contigs containing integrative and conjugative elements (ICEs). Output to `../conjugative_systems`

# Section 3: Population mapping to identified conjugative systems
**Run in environment with anvi'o installed and requires SRA toolkit for fasterq-dump**
**`pop_mapping_dl.sh` needs to be edited beforehand**
`./pop_mapping_master.sh`
* combines all extracted DNA sequences containing conjugative systems into `../population_mapping/unformated_contigs.fa`
* reformats fasta file to be compliant with downstream programs and retains a record of the format change, `../population_mapping/contigs.fa`, `../population_mapping/name_change.txt`
* bowtie2 database is built from `../population_mapping/contigs.fa` and output in `../population_mapping/`
* anvi'o contigs database is created in `../population_mapping/`
* reads are downloaded based on information in `pop_mapping_samples.txt`, processed, and output in `../population_mapping/reads/`
* processed reads are mapped to bowtie2 database, SAM files are converted to BAM files and sorted/indexed
* anvi'o profiles are generated for each sample, output in `../population_mapping/profiles/`
* anvi'o profiles merged and output in `../population_mapping/MERGED`
* adds country data and taxonomic data to the anvi'o profile

**At this point, an equivalent to the population mapping anvi'o circular phylogram is viewable**

# Section 4: PlasFlow and MOB suite
* `PlasFlow.py --input contigs.fa --output plasflow_predictions.tsv` ran on set of full contigs (not extracted operons) for the genome set contigs
* before `mob_typer` can be used, each contig must be separated, `separate_contigs.py` was used, full contigs file must be saved as `../genome_set_conj/contigs.fa`
* `run_mob_typer.sh` to run MOB suite, `combine_mob_typer.sh` to combine into one table
