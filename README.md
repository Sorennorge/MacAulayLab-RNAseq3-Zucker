# MacAulayLab - Obese Zucker rats with testosterone treatment #
The work and scripts are done by the MacAulay Lab.\
All programs used are free and open-source.
In the interest of open science and reproducibility, all data and source code used in our research is provided here.\
Feel free to copy and use code, but please cite:\
(coming soon) \
*Remember* rewrite file_names and folder_names suitable for your pipeline.\

## The RNAseq and Analysis follows these steps:
## Raw data analysis - Library Build, Mapping and Quantification ##
The analysis uses RNA STAR for mapping and RSEM for TPM quantification.
### RNA-STAR and RSEM Library build and indexing ###

0.1.1 - RNA_STAR_Indexing.sh \
0.2.1 - RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###

0.1.2 -RNA_STAR_Analysis.sh \
0.2.2 - RSEM_Analysis.sh

# Zucker rats (Obese vs lean) #
## Create count tables and reduce for RNA star ##

1.1.1 - Raw data GeneCounts.py

## Create count tables and reduce for RSEM (TPM) ##

1.2.1 - Raw data RSEM.py

## Differential expression analysis with DEseq2 ##

2.1.1 - DE Analysis Zucker Obese.R

## Volcano plot ##

2.2.1 - DE Analysis Volcano.R

## Heatmap plot ##

2.3.1 - DE Analysis Heatmap.R

## Piechart of differentially expressed genes in percentage ##

2.4.1 - Pie chart - Differentially expressed genes.py

## Update lookup DE tables ##

3.1.1 - Update lookup DE tables.py

## Go term enrichement analysis - protein coding genes ##

4.1.1 - Enrichment - Convert raw Panther DB data.py
4.1.2 - Enrichment - Plot.py

## Transport analysis ##

5.1.1 - Enrichment - Transport analysis - Convert raw data.py 
5.1.2 - Enrichment - Transport analysis - subcellular location.py
5.1.3 - Enrichment - Transport analysis - Generate count tables

# Testosterone treated Zucker rats (Obese TT vs lean (VEH)) #

## Create count tables and reduce for RNA star ##

8.1.1 - Raw data - GeneCounts.py

## Create count tables and reduce for RSEM (TPM) ##

8.2.1 - Raw data - RSEM.py

## Differential expression analysis with DEseq2 ##

9.1.1 - DE Analysis - Zucker Obese TT.R

## Volcano plot ##

9.2.1 - DE Analysis - Volcano - Obese TT.R

## Heatmap plot ##

9.3.1 - DE Analysis - Heatmap - Obese TT.R

## Piechart of differentially expressed genes in percentage ##

9.4.1 - Pie chart - Differentially expressed genes.py

## Update lookup DE tables ##

10.1.1 - Update lookup DE tables - Obese TT.py

## Go term enrichement analysis - protein coding genes ##

11.1.1 - Enrichment - Convert raw Panther DB data.py
11.1.2 - Enrichment - Plot.py

## Transport analysis ##

12.1.1 - Enrichment - Transport analysis - Convert raw data.py 
12.1.2 - Enrichment - Transport analysis - subcellular location.py
12.1.3 - Enrichment - Transport analysis - Generate count tables

## Calculate adjusted p-value for transport ##

13.1.1 - Add adjusted pvalue to transporter tables.py

## Create supplementary tables ##

14.1.1 - Create supplementary tables
