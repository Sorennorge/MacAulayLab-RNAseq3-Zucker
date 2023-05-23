# -*- coding: utf-8 -*-

### Enrichement plot ###

## Libraries ##

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Folders ##

Folder1 = "Data/Panther DB/Zucker - Obese/Clean data"
Folder2 = "Results/Zucker - Obese/Enrichment"
os.makedirs(Folder2,exist_ok=True)

## Files ##

File1 = "Enrichement data.xlsx"
File2 = "Enrichement plot.png"
File3 = "Enrichement plot clean.pdf"

## Load data ##

df = pd.read_excel(os.path.join(Folder1,File1))

df_data = df['Count']
df_labels = df['Protein classes']

## Set color scheme ##
n=len(df_labels)
colors = sns.color_palette('blend:#7F7F7F,#F2F2F2',n_colors=n)

## Plot with percentage and labels ##
plt.figure(figsize=(20,20))
plt.pie(df_data, 
        labels = df_labels, 
        colors = colors, 
        autopct='%.0f%%',
        textprops={'fontsize': 34},
        wedgeprops = {"edgecolor":"black",'linewidth': 3},
        counterclock=False,
        startangle=90,
        pctdistance=0.9,
        labeldistance=1.2)
plt.savefig(os.path.join(Folder2,File2),dpi=1200,bbox_inches='tight',transparent=True)
plt.show()

## Plot clean version ##
plt.figure(figsize=(20,20))
plt.pie(df_data, 
        #labels = df_labels, 
        colors = colors, 
        #autopct='%.0f%%',
        textprops={'fontsize': 34},
        wedgeprops = {"edgecolor":"black",'linewidth': 5},
        counterclock=False,
        startangle=90,
        pctdistance=0.9,
        labeldistance=1.2)
plt.savefig(os.path.join(Folder2,File3),dpi=1200,bbox_inches='tight',transparent=True)
plt.show()