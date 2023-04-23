##############
# Author: Ben Joris
# Created: May 20th, 2021 
# Purpose: Aggregate the taxonomy output from CATBAT into tables for comparative analysis
##############

inf_phy={}
gen_phy={}
inf_class={}
gen_class={}
with open("../ce_analysis/catbat_taxonomy.txt") as ce_catbat:
    for line in ce_catbat:
        if line.startswith("# bin"):
            continue
        else:
            if "(class)" in line:
                for i in line.split("\t"):
                    if "(class)" in i:
                        if "infant_" in line:
                            inf_class[i.split()[0]]=inf_class.get(i.split()[0],0)+1
                        else:
                            gen_class[i.split()[0]]=gen_class.get(i.split()[0],0)+1
                    if "(phylum)" in i:
                        if "infant_" in line:
                            inf_phy[i.split()[0]]=inf_phy.get(i.split()[0],0)+1
                        else:
                            gen_phy[i.split()[0]]=gen_phy.get(i.split()[0],0)+1
            elif "(phylum)" in line:
                for i in line.split("\t"):
                    if "(phylum)" in i:
                        if "infant_" in line:
                            inf_phy[i.split()[0]]=inf_phy.get(i.split()[0],0)+1
                        else:
                            gen_phy[i.split()[0]]=gen_phy.get(i.split()[0],0)+1
            else:
                if "adult_" in line:
                    gen_phy["N/A"]=gen_phy.get("N/A",0)+1
                    gen_class["N/A"]=gen_class.get("N/A",0)+1
                if "infant_" in line:
                    inf_phy["N/A"]=inf_phy.get("N/A",0)+1
                    inf_class["N/A"]=inf_class.get("N/A",0)+1
                    
            
with open("../ce_analysis/catbat_inf_phy.tsv","w") as infphy:
    for k,v in inf_phy.items():
        infphy.write(k+"\t"+str(v)+"\n")
        
with open("../ce_analysis/catbat_inf_class.tsv","w") as infclass:
    for k,v in inf_class.items():
        infclass.write(k+"\t"+str(v)+"\n")
        
with open("../ce_analysis/catbat_gen_phy.tsv","w") as genphy:
    for k,v in gen_phy.items():
        genphy.write(k+"\t"+str(v)+"\n")
        
with open("../ce_analysis/catbat_gen_class.tsv","w") as genclass:
    for k,v in gen_class.items():
        genclass.write(k+"\t"+str(v)+"\n")
            
            
inf_phy={}
gen_phy={}
inf_class={}
gen_class={}
with open("../mag_analysis/catbat_taxonomy.txt") as ce_catbat:
    for line in ce_catbat:
        if line.startswith("# bin"):
            continue
        else:
            if "(class)" in line:
                for i in line.split("\t"):
                    if "(class)" in i:
                        if "SRR313" in line:
                            inf_class[i.split()[0]]=inf_class.get(i.split()[0],0)+1
                        else:
                            gen_class[i.split()[0]]=gen_class.get(i.split()[0],0)+1
                    if "(phylum)" in i:
                        if "SRR313" in line:
                            inf_phy[i.split()[0]]=inf_phy.get(i.split()[0],0)+1
                        else:
                            gen_phy[i.split()[0]]=gen_phy.get(i.split()[0],0)+1
            elif "(phylum)" in line:
                for i in line.split("\t"):
                    if "(phylum)" in i:
                        if "SRR313" in line:
                            inf_phy[i.split()[0]]=inf_phy.get(i.split()[0],0)+1
                        else:
                            gen_phy[i.split()[0]]=gen_phy.get(i.split()[0],0)+1
            else:
                if "SRR56" in line:
                    gen_phy["N/A"]=gen_phy.get("N/A",0)+1
                    gen_class["N/A"]=gen_class.get("N/A",0)+1
                if "SRR313" in line:
                    inf_phy["N/A"]=inf_phy.get("N/A",0)+1
                    inf_class["N/A"]=inf_class.get("N/A",0)+1
                    
            
with open("../mag_analysis/catbat_inf_phy.tsv","w") as infphy:
    for k,v in inf_phy.items():
        infphy.write(k+"\t"+str(v)+"\n")
        
with open("../mag_analysis/catbat_inf_class.tsv","w") as infclass:
    for k,v in inf_class.items():
        infclass.write(k+"\t"+str(v)+"\n")
        
with open("../mag_analysis/catbat_gen_phy.tsv","w") as genphy:
    for k,v in gen_phy.items():
        genphy.write(k+"\t"+str(v)+"\n")
        
with open("../mag_analysis/catbat_gen_class.tsv","w") as genclass:
    for k,v in gen_class.items():
        genclass.write(k+"\t"+str(v)+"\n")
            