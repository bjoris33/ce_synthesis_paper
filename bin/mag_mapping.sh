#!/bin/bash
##############
# Author: Ben Joris
# Created: May 4th, 2021
# Purpose: Map reads to deduplicated, high-quality bins
##############

bowtie2-build ../mag_analysis/mapping/contigs.fa ../mag_analysis/mapping/btdb

for fwd in $(ls ../infant/data/reads/processed/*_1.fastq.gz);do
    sample_name=`basename $fwd _1.fastq.gz`
    echo $sample_name
    rev=../infant/data/reads/processed/${sample_name}_2.fastq.gz
    echo $rev
    bowtie2 -p 20 -1 $fwd -2 $rev -x ../mag_analysis/mapping/btdb --no-unal --no-mixed --no-discordant -S ../mag_analysis/mapping/${sample_name}.sam
    samtools view -bS ../mag_analysis/mapping/${sample_name}.sam > ../mag_analysis/mapping/${sample_name}.bam
    samtools sort -o ../mag_analysis/mapping/sorted_${sample_name}.bam ../mag_analysis/mapping/${sample_name}.bam
    samtools index ../mag_analysis/mapping/sorted_${sample_name}.bam
done

for fwd in $(ls ../adult_na/data/reads/processed/*_1.fastq.gz);do
    sample_name=`basename $fwd _1.fastq.gz`
    echo $sample_name
    rev=../adult_na/data/reads/processed/${sample_name}_2.fastq.gz
    echo $rev
    bowtie2 -p 20 -1 $fwd -2 $rev -x ../mag_analysis/mapping/btdb --no-unal --no-mixed --no-discordant -S ../mag_analysis/mapping/${sample_name}.sam
    samtools view -bS ../mag_analysis/mapping/${sample_name}.sam > ../mag_analysis/mapping/${sample_name}.bam
    samtools sort -o ../mag_analysis/mapping/sorted_${sample_name}.bam ../mag_analysis/mapping/${sample_name}.bam
    samtools index ../mag_analysis/mapping/sorted_${sample_name}.bam
done