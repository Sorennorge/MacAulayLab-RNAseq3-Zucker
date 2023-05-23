# -*- coding: utf-8 -*-

### Add ajusted p-value to transporter tables ###

## Libraries ##

import os
import pandas as pd

## Function ##

def compute_pvalue_star(df):    
    if (df['Padj'] <= 0.001):
        return '***'
    elif (df['Padj'] > 0.001) & (df['Padj'] <= 0.01):
        return '**'
    elif (df['Padj'] > 0.01) & (df['Padj'] <= 0.05):
        return '*'
    else:
        return "Not significant"

## Folders ##

Folder1 = "Results/Zucker - Obese/Differentially expressed genes/Transport"
Folder2 = "Results/Zucker - Obese TT/Differentially expressed genes/Transport"

Folder3 = "Results/Zucker - Obese/Differentially expressed genes"
Folder4 = "Results/Zucker - Obese TT/Differentially expressed genes"

## Files ##

File1 = "Transport - count table - Zucker - Obese.xlsx"
File2 = "Transport - count table - Zucker - Obese TT.xlsx"

File3 = "DEseq2 - DE Genes - Zucker obese - version 2.xlsx"
File4 = "DEseq2 - DE Genes - Zucker obese TT - version 2.xlsx"

File5 ="Transport - count table - Zucker - Obese - Version 2.xlsx"
File6 = "Transport - count table - Zucker - Obese TT - Version 2.xlsx"

## Load data ##

df_obese = pd.read_excel(os.path.join(Folder1,File1))
df_obeseTT = pd.read_excel(os.path.join(Folder2,File2))

df_obese_pvalue = pd.read_excel(os.path.join(Folder3,File3))
df_obeseTT_pvalue = pd.read_excel(os.path.join(Folder4,File4))

df_obese_merged = pd.concat([df_obese.set_index("Ensembl ID"),df_obese_pvalue.set_index("Ensembl ID")['Padj']],axis=1,join="inner")
df_obese_merged['Significance'] = df_obese_merged.apply(compute_pvalue_star, axis = 1)
#df_obese_merged = df_obese_merged.reset_index()

df_obeseTT_merged = pd.concat([df_obeseTT.set_index("Ensembl ID"),df_obeseTT_pvalue.set_index("Ensembl ID")['Padj']],axis=1,join="inner")
df_obeseTT_merged['Significance'] = df_obeseTT_merged.apply(compute_pvalue_star, axis = 1)
#df_obeseTT_merged = df_obeseTT_merged.reset_index()

df_obese_merged.to_excel(os.path.join(Folder1,File5),sheet_name="Transport count table")
df_obeseTT_merged.to_excel(os.path.join(Folder2,File6),sheet_name="Transport count table")
