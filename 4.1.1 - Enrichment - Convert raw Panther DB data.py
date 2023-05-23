# -*- coding: utf-8 -*-

### Panther DB - Convert raw data to data tables ###

## Requires downloaded table of protein classes (piechart) from pantherdb.org ##

## Libraries ##

import os
import pandas as pd

## Folders ##

Folder1 = "Data/Panther DB/Zucker - Obese/Raw data"
Folder2 = "Data/Panther DB/Zucker - Obese/Clean data"
os.makedirs(Folder2)

## Files ##

File1 = "Enrichment analysis.txt"
File2 = "Enrichement data.xlsx"

## Load data ##

df = pd.read_csv(os.path.join(Folder1,File1),sep='\t',header=None)
df = df.rename(columns=({1:"Protein classes",2:"Count"}))

## remove id identifier from protein calsses
df["Protein classes"] = df["Protein classes"].apply(lambda x: x.split(" (")[0])
df["Protein classes"] = df["Protein classes"].apply(lambda x: x[0].upper()+x[1:])

## Setup dataframe ##
df = df[['Protein classes','Count']]

## Replace unclassified with correct annotations ##
df['Protein classes'] = df['Protein classes'].replace(["No PANTHER category is assigned"],"Unclassified")

## Make list of all entries besides unclassified ##
Protein_class_list = df['Protein classes'].tolist()
Protein_class_list.remove("Unclassified")

## Split data into all entries and unclassified ##
df_unclassifed = df[~df['Protein classes'].isin(Protein_class_list)]
df_all = df[df['Protein classes'].isin(Protein_class_list)]

## Sort by count ##
df_all = df_all.sort_values(by=['Count'],ascending=False,ignore_index=True)
## Create dataframe with "others", which is entries below a cutoff of (in this instance) 4 ##
df_others = df_all[df_all.Count < 4]
# Sum other counts #
Others_sum = df_others['Count'].sum()
## Create dataframe with the sum of others ##
df_others_sum = pd.DataFrame({'Protein classes':"Others",'Count':Others_sum},index=[0])

## Remove others from dataframe ##
df_all_exlude_others = df_all[df_all.Count > 4]

## concatenate sorted dataframe with others and unclassified ##
df_all_sorted = pd.concat([df_all_exlude_others, df_others_sum, df_unclassifed], ignore_index=True)

## Save dataframe to file for enrichement plot ##
df_all_sorted.to_excel(os.path.join(Folder2,File2),sheet_name="Enrichment data",index=False)

