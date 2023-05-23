# -*- coding: utf-8 -*-

### Transport analysis ### 

## Libraries ##

import os
import pandas as pd

## Folders ##

## Folders ##


Folder1 = "Data/Panther DB/Zucker - Obese/Clean data"
Folder2 = "Data/Count Tables/Zucker - Obese"
Folder3 = "Results/Zucker - Obese/Differentially expressed genes/Transport"
os.makedirs(Folder3,exist_ok=True)

## Files ##

File1 = "Enrichement Transporters version 2.xlsx"
File2 = "Reduced - TPM - Count table - Zucker - Obese.csv"
File3 = "Transport - count table - Zucker - Obese.xlsx"

## Load data ##

df = pd.read_excel(os.path.join(Folder1,File1))
df_CT = pd.read_csv(os.path.join(Folder2,File2),sep=";")

## rename columns ##

df_CT = df_CT.rename(columns=({"Sample 11 (TPM)":"Lean 1",
                       "Sample 12 (TPM)":"Lean 2",
                       "Sample 13 (TPM)":"Lean 3",
                       "Sample 14 (TPM)":"Lean 4",
                       "Sample 15 (TPM)":"Lean 5",
                       "Sample 16 (TPM)":"Lean 6",
                       "Sample 17 (TPM)":"Obese 1",
                       "Sample 18 (TPM)":"Obese 2",
                       "Sample 19 (TPM)":"Obese 3",
                       "Sample 20 (TPM)":"Obese 4",
                       "Sample 21 (TPM)":"Obese 5",
                       "Sample 22 (TPM)":"Obese 6"}))

df = df.set_index("Ensembl ID").copy()
df_CT = df_CT.set_index("Ensembl ID").copy()

merged_df = pd.concat([df,df_CT],axis=1,join="inner")


merged_df.to_excel(os.path.join(Folder3,File3),sheet_name="Transport count table")

