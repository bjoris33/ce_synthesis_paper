##############
# Author: Ben Joris
# Created: June 9th, 2021
# Purpose: Get # reads mapping/phylum for the bins
##############
import glob, pandas
from collections import defaultdict

tax_dict={}

with open("../mag_analysis/catbat_taxonomy.txt") as ce_catbat:
    for line in ce_catbat:
        if line.startswith("# bin"):
            continue
        else:
            if "(phylum)" in line:
                for i in line.split("\t"):
                    if "(phylum)" in i:
                        tax_dict[line.split("\t")[0].split(".")[0].split("_")[0]+"_"+line.split("\t")[0].split(".")[1]]=i.split()[0]
            else:
                tax_dict[line.split("\t")[0].split(".")[0].split("_")[0]+"_"+line.split("\t")[0].split(".")[1]]="N/A"


infcountdict=defaultdict(dict)
gencountdict=defaultdict(dict)
for file in glob.glob("../mag_analysis/stats_mapping/*.tsv"):
    sample_name=file.rsplit("/",1)[1].split(".")[0].rsplit("_",1)[1]
    with open(file) as mapfh:
        for line in mapfh:
            if line.startswith("*"):
                continue
            if "SRR313" in sample_name:
                infcountdict[tax_dict[line.split("\t")[0].rsplit("_",2)[0]]]=infcountdict.get(tax_dict[line.split("\t")[0].rsplit("_",2)[0]],0)+int(line.split("\t")[2])
            else:
                gencountdict[tax_dict[line.split("\t")[0].rsplit("_",2)[0]]]=gencountdict.get(tax_dict[line.split("\t")[0].rsplit("_",2)[0]],0)+int(line.split("\t")[2])
            
with open("../mag_analysis/inf_phylum_mag_mapping.tsv","w") as newfh:
    for k,v in infcountdict.items():
        newfh.write(k+"\t"+str(v)+"\n")
with open("../mag_analysis/gen_phylum_mag_mapping.tsv","w") as newfh:
    for k,v in gencountdict.items():
        newfh.write(k+"\t"+str(v)+"\n")        

tax_dict={}

with open("../ce_analysis/catbat_taxonomy.txt") as ce_catbat:
    for line in ce_catbat:
        if line.startswith("# bin"):
            continue
        else:
            if "(phylum)" in line:
                for i in line.split("\t"):
                    if "(phylum)" in i:
                        tax_dict[line.split("\t")[0].split(".")[0]]=i.split()[0]
            else:
                tax_dict[line.split("\t")[0].split(".")[0]]="N/A"


infcountdict=defaultdict(dict)
gencountdict=defaultdict(dict)
for file in glob.glob("../ce_analysis/stats_mapping/*.tsv"):
    sample_name=file.rsplit("/",1)[1].split(".")[0].rsplit("_",1)[1]
    with open(file) as mapfh:
        for line in mapfh:
            if line.startswith("*"):
                continue
            if "SRR313" in sample_name:
                infcountdict[tax_dict[line.split("\t")[0]]]=infcountdict.get(tax_dict[line.split("\t")[0]],0)+int(line.split("\t")[2])
            else:
                gencountdict[tax_dict[line.split("\t")[0]]]=gencountdict.get(tax_dict[line.split("\t")[0]],0)+int(line.split("\t")[2])
            
with open("../ce_analysis/inf_phylum_mag_mapping.tsv","w") as newfh:
    for k,v in infcountdict.items():
        newfh.write(k+"\t"+str(v)+"\n")
with open("../ce_analysis/gen_phylum_mag_mapping.tsv","w") as newfh:
    for k,v in gencountdict.items():
        newfh.write(k+"\t"+str(v)+"\n")        
