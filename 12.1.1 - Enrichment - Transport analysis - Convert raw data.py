# -*- coding: utf-8 -*-

### Transport analysis ### 

## Libraries ##

import os
import pandas as pd

## Folders ##

## Folders ##

Folder1 = "Data/Panther DB/Zucker - Obese/Raw data"
Folder2 = "Results/Zucker - Obese/Differentially expressed genes"
Folder3 = "Data/Metadata/Biomart"
Folder4 = "Data/Panther DB/Zucker - Obese/Clean data"
os.makedirs(Folder4,exist_ok=True)

## Files ##

File1 = "Transporter list.txt"
File2 = "DEseq2 - DE Genes - Zucker obese - version 2.xlsx"
File3 = "Protein and Uniprot biomart.txt"
File4 = "Enrichement Transporters.xlsx"

## Load data ##

df1 = pd.read_csv(os.path.join(Folder1,File1),sep="\t",header=None)
transport_list = df1[1].tolist()
transport_uniport = df1.set_index(0)[1].to_dict()

df2 = pd.read_excel(os.path.join(Folder2,File2))
DE_dict = df2.set_index('Gene')['Ensembl ID'].to_dict()

df3 = pd.read_csv(os.path.join(Folder3,File3),sep=",")

col_names = df3.columns.tolist()
uniprot_to_ensembl = df3.set_index(col_names[3])[col_names[0]].to_dict()

Transport_dict = {}

for key in transport_list:
    if key not in DE_dict:
        if key == 'AABR07026986':
            pass
            # Is a LincRNA
        else:
            for prot_key in transport_uniport:
                if key == transport_uniport[prot_key]:
                    uniprot_id = prot_key.split("=")
                    uniprot_id = uniprot_id[2]
                    print(prot_key,key,uniprot_id,uniprot_to_ensembl[uniprot_id])
    else:
        Transport_dict[DE_dict[key]] = key

df4 = pd.DataFrame.from_dict(Transport_dict,orient='index').reset_index().rename(columns=({"index":"Ensembl ID",0:"Gene"}))

df4.to_excel(os.path.join(Folder4,File4),index=False)