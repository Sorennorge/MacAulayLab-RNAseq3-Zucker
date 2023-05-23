# -*- coding: utf-8 -*-

#### Collect all genes for supplementary tables ####

## Import libraries ##

import os
import pandas as pd

## Functions ##

mean_decimals = 0
sem_decimals = 0

def Pvalue_annotation(df):
    if df['Pvalue'] <= 0.001:
        return '< 0.001'
    elif df['Pvalue'] <= 0.01:
        return '< 0.01'
    elif df['Pvalue'] <= 0.05:
        return '< 0.05'
    else:
        pass
    
def Padj_annotation(df):
    if df['Padj'] <= 0.001:
        return '< 0.001'
    elif df['Padj'] <= 0.01:
        return '< 0.01'
    elif df['Padj'] <= 0.05:
        return '< 0.05'
    else:
        pass
## Obese and Obese TT -> Lean ##    
def TPM_values_mean_lean(df):
    if df['Mean (Lean)'] < 1.0:
        return '< 1'
    elif df['Mean (Lean)'] >= 1.0:
        value = round(df['Mean (Lean)'],mean_decimals)
        return value
    else:
        pass

def TPM_values_sem_lean(df):
    if df['SEM (Lean)'] < 1.0:
        return '< 1'
    elif df['SEM (Lean)'] >= 1.0:
        value = round(df['SEM (Lean)'],sem_decimals)
        return value
    else:
        pass


## Obese ##
def TPM_values_mean_obese(df):
    if df['Mean (Obese)'] < 1.0:
        return '< 1'
    elif df['Mean (Obese)'] >= 1.0:
        value = round(df['Mean (Obese)'],mean_decimals)
        return value
    else:
        pass

def TPM_values_sem_obese(df):
    if df['SEM (Obese)'] < 1.0:
        return '< 1'
    elif df['SEM (Obese)'] >= 1.0:
        value = round(df['SEM (Obese)'],sem_decimals)
        return value
    else:
        pass
## Obese TT ##
def TPM_values_mean_obeseTT(df):
    if df['Mean (Obese TT)'] < 1.0:
        return '< 1'
    elif df['Mean (Obese TT)'] >= 1.0:
        value = round(df['Mean (Obese TT)'],mean_decimals)
        return value
    else:
        pass

def TPM_values_sem_obeseTT(df):
    if df['SEM (Obese TT)'] < 1.0:
        return '< 1'
    elif df['SEM (Obese TT)'] >= 1.0:
        value = round(df['SEM (Obese TT)'],sem_decimals)
        return value
    else:
        pass
        
## Folders ##

# Obese #
Folder_obese = "Results/Zucker - Obese/Differentially expressed genes"
Folder_obese_CT = "Data/Count Tables/Zucker - Obese"
Folder_obese_Transport = "Results/Zucker - Obese/Differentially expressed genes/Transport"

# Obese TT #
Folder_obeseTT_CT = "Data/Count Tables/Zucker - Obese TT"
Folder_obeseTT = "Results/Zucker - Obese TT/Differentially expressed genes"
Folder_obeseTT_Transport = "Results/Zucker - Obese TT/Differentially expressed genes/Transport"

# Output folder #
Folder_out = "Results/Supplementary Tables"
os.makedirs(Folder_out,exist_ok=True)

## Files ##

# Input - Obese #
File_obese_all = "DEseq2 - All Genes -  Zucker obese - version 2.xlsx"
File_obese_DE = "DEseq2 - DE Genes - Zucker obese - version 2.xlsx"
File_obese_CT = "Count table - TPM - Zucker - Obese.csv"
File_obese_Transport = "Transport - count table - Zucker - Obese - Version 2.xlsx"

# Input - Obese TT #
File_obeseTT_all = "DEseq2 - All Genes -  Zucker obese TT - version 2.xlsx"
File_obeseTT_DE = "DEseq2 - DE Genes - Zucker obese TT - version 2.xlsx"
File_obeseTT_CT = "Count table - TPM - Zucker - Obese TT.csv"
File_obeseTT_Transport = "Transport - count table - Zucker - Obese TT - Version 2.xlsx"

# Output - Obese #
File_Addition_2 = "Additional file 2.xlsx"
# Output - Obese TT #
File_Addition_4 = "Additional file 4.xlsx"

## Load data ##

## Additional file 2 ##
# Obese all #
df_obese_all = pd.read_excel(os.path.join(Folder_obese,File_obese_all))
df_obese_all = df_obese_all[['Ensembl ID','Gene']]
# Obese DE #
df_obese_DE = pd.read_excel(os.path.join(Folder_obese,File_obese_DE))

# Obese count table #
df_obese_CT = pd.read_csv(os.path.join(Folder_obese_CT,File_obese_CT),sep=";",decimal=".")
df_obese_CT['Mean (Lean)'] = df_obese_CT[['Sample 11 (TPM)',
                                          'Sample 12 (TPM)',
                                          'Sample 13 (TPM)',
                                          'Sample 14 (TPM)',
                                          'Sample 15 (TPM)',
                                          'Sample 16 (TPM)']].mean(axis=1)

df_obese_CT['SEM (Lean)'] = df_obese_CT[['Sample 11 (TPM)',
                                          'Sample 12 (TPM)',
                                          'Sample 13 (TPM)',
                                          'Sample 14 (TPM)',
                                          'Sample 15 (TPM)',
                                          'Sample 16 (TPM)']].sem(axis=1,ddof=1)


df_obese_CT['Mean (Obese)'] = df_obese_CT[['Sample 17 (TPM)',
                                          'Sample 18 (TPM)',
                                          'Sample 19 (TPM)',
                                          'Sample 20 (TPM)',
                                          'Sample 21 (TPM)',
                                          'Sample 22 (TPM)']].mean(axis=1)

df_obese_CT['SEM (Obese)'] = df_obese_CT[['Sample 17 (TPM)',
                                          'Sample 18 (TPM)',
                                          'Sample 19 (TPM)',
                                          'Sample 20 (TPM)',
                                          'Sample 21 (TPM)',
                                          'Sample 22 (TPM)']].sem(axis=1,ddof=1)
# Transport #

df_obese_transport = pd.read_excel(os.path.join(Folder_obese_Transport,File_obese_Transport))

## Modify Obese - additional file 2 - sheet 1 ##
# Add mean and SEM from Obese count table #
df_obese_CT_mod = df_obese_CT[['Ensembl ID','Mean (Lean)','SEM (Lean)','Mean (Obese)','SEM (Obese)']]
# Set index to Ensembl ID
df_obese_CT_mod = df_obese_CT_mod.set_index("Ensembl ID")

# Merge obese all with count table values (mean and SEM)
df_obese_all_mod = pd.concat([df_obese_all.set_index("Ensembl ID"),df_obese_CT_mod],axis=1,join="inner")

# Reset index and sort after Mean (Lean) #
df_obese_all_mod = df_obese_all_mod.reset_index()
df_obese_all_mod = df_obese_all_mod.sort_values(by=['Mean (Lean)'],ascending=False,ignore_index=True)

# Modify annotation of TPM (less than 1)
df_obese_all_mod['Mean (Lean)'] = df_obese_all_mod.apply(TPM_values_mean_lean,axis=1)
df_obese_all_mod['SEM (Lean)'] = df_obese_all_mod.apply(TPM_values_sem_lean,axis=1)
df_obese_all_mod['Mean (Obese)'] = df_obese_all_mod.apply(TPM_values_mean_obese,axis=1)
df_obese_all_mod['SEM (Obese)'] = df_obese_all_mod.apply(TPM_values_sem_obese,axis=1)
# Fill "nan" values with "N/A" gene names #
df_obese_all_mod['Gene'] = df_obese_all_mod['Gene'].fillna("N/A")
## Modify Obese DE - additional file 2 - sheet 2 ##
# Sort by Log2FC #
df_obese_DE = df_obese_DE.sort_values(by=['Log2FC'],ascending=False,ignore_index=True)
# Rename columns #
df_obese_DE = df_obese_DE.rename(columns=( {'BaseMean (DEseq2)' : 'BaseMean'} ))
# Round BaseMean and Log2FC #
df_obese_DE['BaseMean'] = df_obese_DE['BaseMean'].round(0)
df_obese_DE['Log2FC'] = df_obese_DE['Log2FC'].round(2)
df_obese_DE['Log2FC'] = df_obese_DE['Log2FC'].apply('{0:.2f}'.format)
# Add new annotation to pvalue and adjusted p-value #
df_obese_DE['Pvalue'] = df_obese_DE.apply(Pvalue_annotation,axis=1)
df_obese_DE['Padj'] = df_obese_DE.apply(Padj_annotation,axis=1)

## Modify Obese Transport - additional file 2 - sheet 3 ##

## Add mean and SEM #
df_obese_transport['Mean (Lean)'] = df_obese_transport[['Lean 1',
                                          'Lean 2',
                                          'Lean 3',
                                          'Lean 4',
                                          'Lean 5',
                                          'Lean 6']].mean(axis=1)

df_obese_transport['SEM (Lean)'] = df_obese_transport[['Lean 1',
                                          'Lean 2',
                                          'Lean 3',
                                          'Lean 4',
                                          'Lean 5',
                                          'Lean 6']].sem(axis=1,ddof=1)


df_obese_transport['Mean (Obese)'] = df_obese_transport[['Obese 1',
                                          'Obese 2',
                                          'Obese 3',
                                          'Obese 4',
                                          'Obese 5',
                                          'Obese 6']].mean(axis=1)

df_obese_transport['SEM (Obese)'] = df_obese_transport[['Obese 1',
                                          'Obese 2',
                                          'Obese 3',
                                          'Obese 4',
                                          'Obese 5',
                                          'Obese 6']].sem(axis=1,ddof=1)

# Create modified transport dataframe #

df_obese_transport_mod = df_obese_transport[['Ensembl ID',
                                             'Gene',
                                             'Alias',
                                             'Mean (Lean)',
                                             'SEM (Lean)',
                                             'Mean (Obese)',
                                             'SEM (Obese)',
                                             'Padj']].copy()

# Modify annotation of TPM (less than 1)
df_obese_transport_mod['Mean (Lean)'] = df_obese_transport_mod['Mean (Lean)'].round(2).apply('{0:.2f}'.format)
df_obese_transport_mod['SEM (Lean)'] = df_obese_transport_mod['SEM (Lean)'].round(2).apply('{0:.2f}'.format)
df_obese_transport_mod['Mean (Obese)'] = df_obese_transport_mod['Mean (Obese)'].round(2).apply('{0:.2f}'.format)
df_obese_transport_mod['SEM (Obese)'] = df_obese_transport_mod['SEM (Obese)'].round(2).apply('{0:.2f}'.format)
# mod gene names #
df_obese_transport_mod['Gene'] = df_obese_transport_mod['Gene'].str.upper()
# modify pvalue #
df_obese_transport_mod['Padj'] = df_obese_transport_mod.apply(Padj_annotation,axis=1)

## Last check if any null values are in DFs for additional file 2 ##
print("Obese check -> NaN values")
print(df_obese_all_mod.isnull().any())
print(df_obese_DE.isnull().any())
print(df_obese_transport_mod.isnull().any())

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer2 = pd.ExcelWriter(os.path.join(Folder_out,File_Addition_2), engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df_obese_all_mod.to_excel(writer2, sheet_name='All genes',index=False)
df_obese_DE.to_excel(writer2, sheet_name='Differentially expressed genes',index=False)
df_obese_transport_mod.to_excel(writer2, sheet_name='Transporters',index=False)

# Close the Pandas Excel writer and output the Excel file.
writer2.close()

## Additional file 4 ##
## Load data  -> Obese TT ##
# Obese TT all ##
df_obeseTT_all = pd.read_excel(os.path.join(Folder_obeseTT,File_obeseTT_all))
df_obeseTT_all = df_obeseTT_all[['Ensembl ID','Gene']]

# Obese TT DE #
df_obeseTT_DE = pd.read_excel(os.path.join(Folder_obeseTT,File_obeseTT_DE))


# Obese_TT count table ##
df_obeseTT_CT = pd.read_csv(os.path.join(Folder_obeseTT_CT,File_obeseTT_CT),sep=";",decimal=".")
df_obeseTT_CT['Mean (Lean)'] = df_obeseTT_CT[['Lean 1 (TPM)',
                                          'Lean 2 (TPM)',
                                          'Lean 3 (TPM)',
                                          'Lean 4 (TPM)']].mean(axis=1)

df_obeseTT_CT['SEM (Lean)'] = df_obeseTT_CT[['Lean 1 (TPM)',
                                          'Lean 2 (TPM)',
                                          'Lean 3 (TPM)',
                                          'Lean 4 (TPM)']].sem(axis=1,ddof=1)


df_obeseTT_CT['Mean (Obese TT)'] = df_obeseTT_CT[['Obese TT 1 (TPM)',
                                          'Obese TT 2 (TPM)',
                                          'Obese TT 3 (TPM)',
                                          'Obese TT 4 (TPM)']].mean(axis=1)

df_obeseTT_CT['SEM (Obese TT)'] = df_obeseTT_CT[['Obese TT 1 (TPM)',
                                          'Obese TT 2 (TPM)',
                                          'Obese TT 3 (TPM)',
                                          'Obese TT 4 (TPM)']].sem(axis=1,ddof=1)
# Transport #
df_obeseTT_transport = pd.read_excel(os.path.join(Folder_obeseTT_Transport,File_obeseTT_Transport))

## Modify Obese TT - Additional file 4 ##

# Add mean and SEM from Obese count table #
df_obeseTT_CT_mod = df_obeseTT_CT[['Ensembl ID','Mean (Lean)','SEM (Lean)','Mean (Obese TT)','SEM (Obese TT)']]
# Set index to Ensembl ID
df_obeseTT_CT_mod = df_obeseTT_CT_mod.set_index("Ensembl ID")

# Merge obese TT all with count table values (mean and SEM)
df_obeseTT_all_mod = pd.concat([df_obeseTT_all.set_index("Ensembl ID"),df_obeseTT_CT_mod],axis=1,join="inner")

# Reset index and sort after Mean (Lean) #
df_obeseTT_all_mod = df_obeseTT_all_mod.reset_index()
df_obeseTT_all_mod = df_obeseTT_all_mod.sort_values(by=['Mean (Lean)'],ascending=False,ignore_index=True)

# Modify annotation of TPM (less than 1)
df_obeseTT_all_mod['Mean (Lean)'] = df_obeseTT_all_mod.apply(TPM_values_mean_lean,axis=1)
df_obeseTT_all_mod['SEM (Lean)'] = df_obeseTT_all_mod.apply(TPM_values_sem_lean,axis=1)
df_obeseTT_all_mod['Mean (Obese TT)'] = df_obeseTT_all_mod.apply(TPM_values_mean_obeseTT,axis=1)
df_obeseTT_all_mod['SEM (Obese TT)'] = df_obeseTT_all_mod.apply(TPM_values_sem_obeseTT,axis=1)
# Fill "nan" values with "N/A" gene names #
df_obeseTT_all_mod['Gene'] = df_obeseTT_all_mod['Gene'].fillna("N/A")

## Modify Obese TT DE - additional file 4 - sheet 2 ##
# Sort by Log2FC #
df_obeseTT_DE = df_obeseTT_DE.sort_values(by=['Log2FC'],ascending=False,ignore_index=True)
# Rename columns #
df_obeseTT_DE = df_obeseTT_DE.rename(columns=( {'BaseMean (DEseq2)' : 'BaseMean'} ))
# Round BaseMean and Log2FC #
df_obeseTT_DE['BaseMean'] = df_obeseTT_DE['BaseMean'].round(0)
df_obeseTT_DE['Log2FC'] = df_obeseTT_DE['Log2FC'].round(2)
df_obeseTT_DE['Log2FC'] = df_obeseTT_DE['Log2FC'].apply('{0:.2f}'.format)
# Add new annotation to pvalue and adjusted p-value #
df_obeseTT_DE['Pvalue'] = df_obeseTT_DE.apply(Pvalue_annotation,axis=1)
df_obeseTT_DE['Padj'] = df_obeseTT_DE.apply(Padj_annotation,axis=1)

## Modify Obese Transport - additional file 4 - sheet 3 ##

## Add mean and SEM #
df_obeseTT_transport['Mean (Lean)'] = df_obeseTT_transport[['Lean 1 (TPM)',
                                          'Lean 2 (TPM)',
                                          'Lean 3 (TPM)',
                                          'Lean 4 (TPM)']].mean(axis=1)

df_obeseTT_transport['SEM (Lean)'] = df_obeseTT_transport[['Lean 1 (TPM)',
                                          'Lean 2 (TPM)',
                                          'Lean 3 (TPM)',
                                          'Lean 4 (TPM)']].sem(axis=1,ddof=1)


df_obeseTT_transport['Mean (Obese TT)'] = df_obeseTT_transport[['Obese TT 1 (TPM)',
                                          'Obese TT 2 (TPM)',
                                          'Obese TT 3 (TPM)',
                                          'Obese TT 4 (TPM)']].mean(axis=1)

df_obeseTT_transport['SEM (Obese TT)'] = df_obeseTT_transport[['Obese TT 1 (TPM)',
                                          'Obese TT 2 (TPM)',
                                          'Obese TT 3 (TPM)',
                                          'Obese TT 4 (TPM)']].sem(axis=1,ddof=1)

# Create modified transport dataframe #

df_obeseTT_transport_mod = df_obeseTT_transport[['Ensembl ID',
                                             'Gene',
                                             'Alias',
                                             'Mean (Lean)',
                                             'SEM (Lean)',
                                             'Mean (Obese TT)',
                                             'SEM (Obese TT)',
                                             'Padj']].copy()


# Modify annotation of TPM (less than 1)
df_obeseTT_transport_mod['Mean (Lean)'] = df_obeseTT_transport_mod['Mean (Lean)'].round(2).apply('{0:.2f}'.format)
df_obeseTT_transport_mod['SEM (Lean)'] = df_obeseTT_transport_mod['SEM (Lean)'].round(2).apply('{0:.2f}'.format)
df_obeseTT_transport_mod['Mean (Obese TT)'] = df_obeseTT_transport_mod['Mean (Obese TT)'].round(2).apply('{0:.2f}'.format)
df_obeseTT_transport_mod['SEM (Obese TT)'] = df_obeseTT_transport_mod['SEM (Obese TT)'].round(2).apply('{0:.2f}'.format)
# mod gene names #
df_obeseTT_transport_mod['Gene'] = df_obeseTT_transport_mod['Gene'].str.upper()
# modify pvalue #
df_obeseTT_transport_mod['Padj'] = df_obeseTT_transport_mod.apply(Padj_annotation,axis=1)
## Last check if any null values are in DFs for additional file 4 ##
print("Obese TT check -> NaN values")
print(df_obeseTT_all_mod.isnull().any())
print(df_obeseTT_DE.isnull().any())
print(df_obeseTT_transport_mod.isnull().any())

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer4 = pd.ExcelWriter(os.path.join(Folder_out,File_Addition_4), engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df_obeseTT_all_mod.to_excel(writer4, sheet_name='All genes',index=False)
df_obeseTT_DE.to_excel(writer4, sheet_name='Differentially expressed genes',index=False)
df_obeseTT_transport_mod.to_excel(writer4, sheet_name='Transporters',index=False)

# Close the Pandas Excel writer and output the Excel file.
writer4.close()