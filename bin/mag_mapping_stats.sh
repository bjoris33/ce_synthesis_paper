#!/bin/bash
##############
# Author: Ben Joris
# Created: May 6th, 2021
# Purpose: Loop through sorted and indexed BAM files to output the mapping stats for the bins
##############


for i in $(ls ../mag_analysis/mapping/sorted*.bam); do
    bn=`basename $i .bam`
    samtools idxstats $i > ../mag_analysis/stats_mapping/${bn}.tsv
done