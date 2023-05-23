# -*- coding: utf-8 -*-

### Pie chart - Differentially expressed genes ###

## Libraries ##

import os
import pandas as pd
import matplotlib.pyplot as plt

## Folders ##

Folder1 = "Results/Zucker - Obese TT/Differentially expressed genes"
Folder2 = "Results/Zucker - Obese TT/Differentially expressed genes/Pie chart"
os.makedirs(Folder2,exist_ok=True)

## Files ##

File1 = "DEseq2 all Genes Zucker obese TT.csv"
File2 = "Piechart - Differentially expressed genes - Zucker Obese TT.pdf"

## Load data ##
df = pd.read_csv(os.path.join(Folder1,File1),sep=";",decimal=",")

#df = df.dropna()
## Get number of genes DE /Total ##
Number_of_genes_total = df.shape[0]
Number_of_genes_DE = df[df['padj'] <= 0.05].shape[0]

## Variables -> Percentage ##
Percentage_DE = round((Number_of_genes_DE/Number_of_genes_total)*100,1)
Percentage_all = 100-Percentage_DE

## Create labels ##
Labels = ['Differentially expressed ({}%)'.format(Percentage_DE),"Not differentially expressed ({}%)".format(Percentage_all)]

## Create color array ##
colors = ["#D9D9D9","#BFBFBF"]

plt.figure(figsize=(10,10))
plt.pie([Number_of_genes_DE,Number_of_genes_total], 
        #labels = Labels, 
        colors = colors,explode=[0.25,0.0],
        textprops={'fontsize': 30},wedgeprops = {"edgecolor":"black",'linewidth': 2},
        counterclock=False,startangle=15,pctdistance=0.8,labeldistance=1.1)
plt.savefig(os.path.join(Folder2,File2),dpi=3200,bbox_inches='tight')
#plt.show()
