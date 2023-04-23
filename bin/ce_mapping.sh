#!/bin/bash
##############
# Author: Ben Joris
# Created: June 9th, 2021
# Purpose: Map reads to the conjugative systems and generate mapping stats for them
##############

bowtie2-build ../ce_analysis/anvio/contigs.fa ../ce_analysis/mapping/btdb

for fwd in $(ls ../infant/data/reads/processed/*_1.fastq.gz);do
    sample_name=`basename $fwd _1.fastq.gz`
    echo $sample_name
    rev=../infant/data/reads/processed/${sample_name}_2.fastq.gz
    echo $rev
    bowtie2 -p 20 -1 $fwd -2 $rev -x ../ce_analysis/mapping/btdb --no-unal --no-mixed --no-discordant -S ../ce_analysis/mapping/${sample_name}.sam
    samtools view -bS ../ce_analysis/mapping/${sample_name}.sam > ../ce_analysis/mapping/${sample_name}.bam
    samtools sort -o ../ce_analysis/mapping/sorted_${sample_name}.bam ../ce_analysis/mapping/${sample_name}.bam
    samtools index ../ce_analysis/mapping/sorted_${sample_name}.bam
done

for fwd in $(ls ../adult_na/data/reads/processed/*_1.fastq.gz);do
    sample_name=`basename $fwd _1.fastq.gz`
    echo $sample_name
    rev=../adult_na/data/reads/processed/${sample_name}_2.fastq.gz
    echo $rev
    bowtie2 -p 20 -1 $fwd -2 $rev -x ../ce_analysis/mapping/btdb --no-unal --no-mixed --no-discordant -S ../ce_analysis/mapping/${sample_name}.sam
    samtools view -bS ../ce_analysis/mapping/${sample_name}.sam > ../ce_analysis/mapping/${sample_name}.bam
    samtools sort -o ../ce_analysis/mapping/sorted_${sample_name}.bam ../ce_analysis/mapping/${sample_name}.bam
    samtools index ../ce_analysis/mapping/sorted_${sample_name}.bam
done

mkdir ../ce_analysis/stats_mapping

for i in $(ls ../ce_analysis/mapping/sorted*.bam); do
    bn=`basename $i .bam`
    samtools idxstats $i > ../ce_analysis/stats_mapping/${bn}.tsv
done