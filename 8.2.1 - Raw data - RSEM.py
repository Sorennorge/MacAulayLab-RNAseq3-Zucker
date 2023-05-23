# -*- coding: utf-8 -*-

### Convert all RSEM output files to csv, extracting TPM column ###

## Import libraries ##

import os
import pandas as pd

## Folders #
Folder1 = "Data/Raw data/Zucker rats - obese TT/RSEM"
Folder2 = "Data/Raw data/Zucker rats - obese TT/TPM"
os.makedirs(Folder2,exist_ok=True)
Folder3 = "Data/Count Tables/Zucker - Obese TT"
os.makedirs(Folder3,exist_ok=True)

## Files ##

File1 = "Count table - TPM - Zucker - Obese TT.csv"
File2 = "Reduced - TPM - Count table - Zucker - Obese TT.csv"

## for each sample file from RNAstar GeneCount -> Generate raw count file ## 
for i in range(1,5,1):
    # Initialize file names #
    file_name_in = "RSEM_Fat_{}.txt".format(i)
    file_name_out = "Sample_Fat_{}_TPM.csv".format(i)
    # Load data #
    df = pd.read_csv(os.path.join(Folder1,file_name_in),sep="\t")
    # Rename columns #
    df = df.rename(columns=({"gene_id":"Ensembl ID"}))
    # Save file #
    df[['Ensembl ID','TPM']].to_csv(os.path.join(Folder2,file_name_out),index=False,sep=";")
    ## Create count table ##
    # If first iteration -> Create Count table #
    if i == 1:
        df_count_table = df[['Ensembl ID','TPM']].rename(columns=({'TPM':'Obese TT 1 (TPM)'})).copy()
    # else append samples into count table #
    else:
        df_count_table = pd.merge(df_count_table, df[['Ensembl ID','TPM']].rename(columns=({'TPM':'Obese TT {} (TPM)'.format(i)})), on="Ensembl ID")

for i in range(1,5,1):
    # Initialize file names #
    file_name_in = "RSEM_Lean_{}.txt".format(i)
    file_name_out = "Sample_Lean_{}_TPM.csv".format(i)
    # Load data #
    df = pd.read_csv(os.path.join(Folder1,file_name_in),sep="\t")
    # Rename columns #
    df = df.rename(columns=({"gene_id":"Ensembl ID"}))
    # Save file #
    df[['Ensembl ID','TPM']].to_csv(os.path.join(Folder2,file_name_out),index=False,sep=";")
    ## Append to count table ##
    df_count_table = pd.merge(df_count_table, df[['Ensembl ID','TPM']].rename(columns=({'TPM':'Lean {} (TPM)'.format(i)})), on="Ensembl ID")

## reduce count table ##

# Remove rows with only zeroes #
df_count_table_reduced = df_count_table.set_index('Ensembl ID').loc[~(df_count_table.set_index('Ensembl ID')==0).all(axis=1)]

## Save count tables to file ##

# Count table #
df_count_table.to_csv(os.path.join(Folder3,File1),index=False,sep=";")

# Redued count table
df_count_table_reduced.to_csv(os.path.join(Folder3,File2),sep=";")