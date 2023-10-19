import anndata
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scanpy as sc

matplotlib.rcParams.update({"font.size": 12})

adata = anndata.read("C:\\Users\\HP\\Downloads\\Kallisto\\SAMN23098192\\counts_unfiltered\\adata.h5ad") #output: cells x genes

sc.pp.pca(adata)

fig, ax = plt.subplots(figsize = (10, 7))
ax.scatter(adata.obsm["X_pca"][:, 0], adata.obsm["X_pca"][:, 1], alpha = 0.5)