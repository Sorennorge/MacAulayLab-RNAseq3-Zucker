# -*- coding: utf-8 -*-

### Transport analysis ### 

## Libraries ##

import os
import pandas as pd

## Folders ##

## Folders ##


Folder1 = "Data/Panther DB/Zucker - Obese TT/Clean data"
Folder2 = "Data/Count Tables/Zucker - Obese TT"
Folder3 = "Results/Zucker - Obese TT/Differentially expressed genes/Transport"
os.makedirs(Folder3,exist_ok=True)

## Files ##

File1 = "Enrichement Transporters - Obese TT - version 2.xlsx"
File2 = "Reduced - TPM - Count table - Zucker - Obese TT.csv"
File3 = "Transport - count table - Zucker - Obese TT.xlsx"

## Load data ##

df = pd.read_excel(os.path.join(Folder1,File1))
df_CT = pd.read_csv(os.path.join(Folder2,File2),sep=";")

## create copies with Ensembl ID as index ##
df = df.set_index("Ensembl ID").copy()
df_CT = df_CT.set_index("Ensembl ID").copy()

## Merge the dataframes ##
merged_df = pd.concat([df,df_CT],axis=1,join="inner")

## Save Transport count table to file ##
merged_df.to_excel(os.path.join(Folder3,File3),sheet_name="Transport count table")