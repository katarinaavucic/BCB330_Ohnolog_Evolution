# BCB330_Ohnolog_Evolution

## Investigating Evolution of Ohnologs in Solanum lycopersicum through Protein and Gene Expression Data Analysis Using Protein Language Models

### Author:
Katarina A. Vucic  
Department of Cell and Systems Biology, University of Toronto  
BCB330: Special Project in Bioinformatics and Computational Biology  
Dr. Jesse Gillis  
April 5, 2024  

---

### Introduction:
This repository contains code related to the paper "Investigating Evolution of Ohnologs in Solanum lycopersicum through Protein and Gene Expression Data Analysis Using Protein Language Models" authored by Katarina A. Vucic. The paper explores the evolutionary dynamics of ohnologs (genes originating from whole genome duplication events) in Solanum lycopersicum (tomato), Solanum tuberosum (potato), and Zea mays (maize) through protein sequence analysis, coexpression patterns, and expression correlation across tissues. The study employs machine learning techniques, specifically Protein Language Models (pLMs), to analyze protein and gene expression data and elucidate the mechanisms driving the divergence of duplicated genes.

---

### Data Accessibility:
Proteomes for tomato, potato, and maize were used to generate the protein embeddings. Protein sequences for tomato are internal, unpublished lab data from the lab’s current collaboration with Zach Lippman, and contain 34112 genes. Protein sequences for potato were retrieved from the Potato Genome Sequencing Consortium (Potato Genome Sequencing Consortium, 2011), and contain 39134 genes. Protein sequences for maize were retrieved from UniProt proteomes (UniProt Consortium, 2018), and contain 39228 genes. 
Whole genome duplicate pairs were acquired from the Plant Genome Duplication Database (Lee et al., 2012). Tomato has 2780 pairs, potato has 2558, and maize has 8958.
Coexpression data for tomato and maize were retrieved from CoCoCoNet (Lee et al., 2020) for the coexpression analysis. These are gene by gene matrices with size 22287 genes and 46727 genes, respectively.
Expression data for the analysis on expression correlation in tomato was retrieved from internal, unpublished lab data from the lab’s current collaboration with Zach Lippman. It is a gene by tissue matrix with 34109 genes and 52 tissues. 

---

### Code Usage:

#### Generate Embeddings:
1. Run run_extract.sh to execute extract_embeddings.py in order to generate the protein embeddings for a given species.
2. Execute combine_plant_embeddings.py to combine all protein embedding files for a given species.

#### Protein Sequence Similarity Ranking:
3. Run run_dist.sh for generate_dist_matrix.py to produce the protein sequence distance matrix.
4. Run run_generate.sh for each generate_comparison_df_*.py to generate the protein sequence ranks for each species.

#### Coexpression Ranking:
5. Run run_coexp.sh for each generate_coexp_ranks_*.py to generate the coexpression ranks for each species.

#### Expression Correlation Across Tissues:
6. Run run_generate.sh for generate_expression_correlation.py to generate the expression correlation across tissues in tomato.

#### Miscellaneous:
7. Run run_get_ids.sh for get_uniprot_ids.py to retrieve the ids for any species to allow for easier mapping across assemblies.
8. Run run_get_ids.sh for create_conversion_df.maize to convert between assemblies.

---

### References
Lee, J., Shah, M., Ballouz, S., Crow, M., & Gillis, J. (2020). CoCoCoNet: conserved and comparative co-expression across a diverse set of species. Nucleic Acids Research, 48(W1), W566–W571. https://doi.org/10.1093/nar/gkaa348
Lee, T.-H., Tang, H., Wang, X., & Paterson, A. H. (2012). PGDD: a database of gene and genome duplication in plants. Nucleic Acids Research, 41(D1), D1152–D1158. https://doi.org/10.1093/nar/gks1104
Potato Genome Sequencing Consortium. (2011). Genome sequence and analysis of the tuber crop potato. Nature, 475(7355), 189–195. https://doi.org/10.1038/nature10158
UniProt Consortium, T. (2018). UniProt: the universal protein knowledgebase. Nucleic Acids Research, 46(5), 2699–2699. https://doi.org/10.1093/nar/gky092
