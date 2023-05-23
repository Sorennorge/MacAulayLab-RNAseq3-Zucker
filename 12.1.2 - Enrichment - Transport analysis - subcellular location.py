# -*- coding: utf-8 -*-

### Subcellular location of transporters ###

## Libraries ##

import os
import pandas as pd

## Folders ##

Folder1 = "Data/Panther DB/Zucker - Obese/Clean data"

## Files ##

File1 = "Enrichement Transporters.xlsx"
File2 = "Subcellular location of transporters.csv"

File3 = "Enrichement Transporters - Subcellular loc.xlsx"

## Load data ##

df1 = pd.read_excel(os.path.join(Folder1,File1))
df2 = pd.read_csv(os.path.join(Folder1,File2))

col_names = df2.columns.tolist()

df2 = df2.drop([col_names[11],col_names[12],col_names[14],col_names[15]],axis=1)

col_compartments = {}
for key in col_names:
    if "compartment" in key:
        temp_key = key.split("::")
        col_compartments[key] = temp_key[1].capitalize()
        
for key in col_compartments:
    df2 = df2.rename(columns=({'{}'.format(key):'{}'.format(col_compartments[key])}))

df2 = df2.fillna(value=0.0)
df2 = df2.set_index("query term")

merged_df = pd.concat([df1.set_index("Gene"),df2],axis=1,join="inner").reset_index().rename(columns=({"index":"Gene"}))
bob = merged_df.shape[1]

## Rearrange column order ##
col_order = [1,0]
for i in range(2,merged_df.shape[1],1):
    col_order.append(i)

merged_df = merged_df.iloc[:, col_order]

## Save dataframe to file ##

merged_df.to_excel(os.path.join(Folder1,File3),index=False)