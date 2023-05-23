# -*- coding: utf-8 -*-

### Modify DE lookup tables ###

## Libraries ##

import os
import pandas as pd

## Folders ##

Folder1 = "Results/Zucker - Obese/Differentially expressed genes"
Folder2 = "Data/Metadata/Biomart"

## Files ##

# input files #
File1 = "DEseq2 all Genes Zucker obese.csv"
File2 = "DEseq2 DE Genes Zucker obese.csv"

# Biomart file from Ensembl with ensembl id and gene symbol #
File3 = "BioMart_Rnor6.0.txt"

# Output files #
File4 = "DEseq2 - All Genes -  Zucker obese - version 2.xlsx"
File5 = "DEseq2 - DE Genes - Zucker obese - version 2.xlsx"

## Load data ##

# All genes #
df1 = pd.read_csv(os.path.join(Folder1,File1),sep=";",decimal=",")
df1 = df1.rename(columns=({'Unnamed: 0':"Ensembl ID",'baseMean':"BaseMean (DEseq2)",'log2FoldChange':"Log2FC",'pvalue':"Pvalue",'padj':"Padj"}))
df1 = df1[['Ensembl ID','BaseMean (DEseq2)','Log2FC','Pvalue','Padj']]

# DE genes #
df2 = pd.read_csv(os.path.join(Folder1,File2),sep=";",decimal=",")
df2 = df2.rename(columns=({'Unnamed: 0':"Ensembl ID",'baseMean':"BaseMean (DEseq2)",'log2FoldChange':"Log2FC",'pvalue':"Pvalue",'padj':"Padj"}))
df2 = df2[['Ensembl ID','BaseMean (DEseq2)','Log2FC','Pvalue','Padj']]


#Load gene infomation #
df_gene = pd.read_csv(os.path.join(Folder2,File3),sep=",")
df_gene = df_gene.rename(columns=({'Gene stable ID':"Ensembl ID",'Gene name':'Gene'}))
Gene_mapping_dict = df_gene.set_index('Ensembl ID')['Gene'].to_dict()

## Modify dataframe #
# All genes #
df1['Gene'] = df1['Ensembl ID'].map(Gene_mapping_dict)
gene_column = df1.pop('Gene')
df1.insert(1,'Gene',gene_column)
# DE genes #
df2['Gene'] = df2['Ensembl ID'].map(Gene_mapping_dict)
gene_column = df2.pop('Gene')
df2.insert(1,'Gene',gene_column)

## Save dataframes ##

df1.to_excel(os.path.join(Folder1,File4),sheet_name="All genes",index=False)
df2.to_excel(os.path.join(Folder1,File5),sheet_name="DE genes",index=False)