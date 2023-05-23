### If DEseq2 needs to be insalled ###
#if (!requireNamespace("BiocManager", quietly = TRUE))
#  install.packages("BiocManager")
#BiocManager::install("DESeq2", version = "3.14")

library("DESeq2")
library("ggplot2")
library("tidyr")

## set working directory ##
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

## Folders ##
Folder1 = "Data/Count Tables/Zucker - Obese"
Folder2 = "Results/Zucker - Obese/Volcano"
dir.create(file.path(Folder2),recursive = TRUE, showWarnings = FALSE)

## Files ##

File1 = "Count table - Zucker - Obese.csv"
File2 = "Volcano plot - Obese.png"

### load data ###
data <- read.table(file.path(Folder1,File1), header=T, sep=";", stringsAsFactors=F, row.names=1)

## create condition / treatment ##
sample_info <- data.frame(condition = factor(c(rep("Zucker_Lean",6),c(rep("Zucker_Obese", 6)))),row.names = factor(colnames(data)))

## create DE dataset in DESeq2 ##

DESeq.ds <- DESeqDataSetFromMatrix(countData = round(data), colData = sample_info, design = ~ condition)

## DESeq.ds
DESeq.ds <- DESeq.ds[rowSums(counts(DESeq.ds)) > 0 , ]
colData(DESeq.ds)$condition <- relevel(colData(DESeq.ds)$condition, "Zucker_Lean")

### Differential expression analysis with DESeq2 ##
colData(DESeq.ds)$treatment <- relevel(colData(DESeq.ds)$condition, "Zucker_Obese")
DESeq.ds <- DESeq(DESeq.ds)
DGE.results <- results(DESeq.ds, independentFiltering = TRUE, alpha = 0.05)

## Sort data and add color scheme (A,B,C) to the genes ##
DGE.results.sorted <- DGE.results[order(DGE.results$log2FoldChange), ]
# A -> not differential expressed #
DGE.results.sorted$diffexpressed <- "A"
# B -> differential expressed (up) #
DGE.results.sorted$diffexpressed[DGE.results.sorted$log2FoldChange > 0.0 & DGE.results.sorted$padj < 0.05] <- "B"
# C -> differential expressed (down) #
DGE.results.sorted$diffexpressed[DGE.results.sorted$log2FoldChange < 0.0 & DGE.results.sorted$padj < 0.05] <- "C"

## Sort the data so the differential expressed is on top ##
data_volcano <- data.frame(x = DGE.results.sorted$log2FoldChange, y = -log(DGE.results.sorted$padj,10), diff = DGE.results.sorted$diffexpressed)
data_volcano.sorted = data_volcano[order(data_volcano$diff), ]
data_volcano.sorted = data_volcano.sorted[!is.na(data_volcano.sorted$y),]

## Choose color scheme ##
mycolors <- c("deepskyblue2", "firebrick2", "grey70")
names(mycolors) <- c("C", "B", "A")

## GGplot ##
p <- ggplot(data_volcano.sorted, aes(x,y,colour=diff)) + 
  geom_vline(xintercept=c(0),linetype = "dashed" ,col="grey50") +
  geom_hline(yintercept=-log10(0.05),linetype = "dashed", col="grey50")+
  geom_hline(yintercept=-log10(1),linetype = "dashed", col="grey50")+
  geom_point(aes(colour=diff, fill=diff),size=2,shape=21,colour = "black",stroke = 0.25) +
  theme_bw()+
  theme(panel.grid.major = element_blank(),panel.grid.minor = element_blank())+
  scale_fill_manual(values = mycolors) +
  scale_x_continuous(name="Log2 fold change",limits=c(-3, 3.1),breaks=seq(-3,3,1)) +
  scale_y_continuous(name="-Log10 adjusted p-value",limits = c(0,8),breaks = seq(0,8, 1)) +
  theme(legend.position="none")

## Plot volcano ##
p

## Save image ##
ggsave(file.path(Folder2,File2),plot=p,width=10,height=10,units=c("cm"),dpi=1200)
