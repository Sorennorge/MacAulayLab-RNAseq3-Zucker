### If DEseq2 needs to be insalled ###
#if (!requireNamespace("BiocManager", quietly = TRUE))
#  install.packages("BiocManager")
#BiocManager::install("DESeq2", version = "3.14")

library("DESeq2")
library("ggplot2")
library("pheatmap")
library("RColorBrewer")

## set working directory ##
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

## Folders ##
Folder1 = "Data/Count Tables/Zucker - Obese TT"
Folder2 = "Results/Zucker - Obese TT/Heatmap"
dir.create(file.path(Folder2),recursive = TRUE, showWarnings = FALSE)

## Files ##

File1 = "Count table - Zucker - Obese TT.csv"
File2 = "Heatmap - Obese TT.png"

### load data ###
data <- read.table(file.path(Folder1,File1), header=T, sep=";", stringsAsFactors=F, row.names=1)

## create condition / treatment ##
sample_info <- data.frame(condition = factor(c(rep("Zucker_Lean",4),c(rep("Zucker_Obese_TT", 4)))),row.names = factor(colnames(data)))

## create DE dataset in DESeq2 ##

DESeq.ds <- DESeqDataSetFromMatrix(countData = round(data), colData = sample_info, design = ~ condition)
DESeq.ds <- DESeq.ds[rowSums(counts(DESeq.ds)) > 0 , ]
colData(DESeq.ds)$condition <- relevel(colData(DESeq.ds)$condition, "Zucker_Lean")
DESeq.ds <- estimateSizeFactors(DESeq.ds)
counts.sf_normalized <- counts(DESeq.ds, normalized = TRUE)

## Create rlog and log norm counts ##
DESeq.rlog <- rlog(DESeq.ds, blind = TRUE )
rlog.norm.counts <- assay(DESeq.rlog)
log.norm.counts <- log2(counts.sf_normalized +1)

### Differential expression analysis with DESeq2 ##
colData(DESeq.ds)$treatment <- relevel(colData(DESeq.ds)$condition, "Zucker_Obese_TT")
DESeq.ds <- DESeq(DESeq.ds)
DGE.results <- results(DESeq.ds, independentFiltering = TRUE, alpha = 0.05)
summary(DGE.results)

DGE.results.sorted <- DGE.results[order(-DGE.results$log2FoldChange), ]
DGEgenes <- rownames(subset(DGE.results.sorted, padj < 0.05))

heatmat_DGEgenes <- log.norm.counts[DGEgenes,]

### Set a color palette
heat_colors <- brewer.pal(10, "RdYlBu")

### Run pheatmap

p<-pheatmap(heatmat_DGEgenes, 
         color = rev(heat_colors),
         cluster_rows = F,
         cluster_cols = F,
         show_rownames = F,
         show_colnames = F,
         border_color = "black", 
         fontsize = 10, 
         scale = "row", 
         fontsize_row = 10, 
         height = 20)
p

## Save plot to file ##

ggsave(file.path(Folder2,File2),plot=p,width=6,height=4,units=c("in"),dpi=1200)
## Get the Zscores of the matrix ##

scale_rows = function(x){
  m = apply(x, 1, mean, na.rm = T)
  s = apply(x, 1, sd, na.rm = T)
  return((x - m) / s)
}
zscores <- scale_rows(heatmat_DGEgenes)
