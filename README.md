# imagine_world_model

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

[Under Submission] Internal World Models as Imagination Networks in Cognitive Agents

## Project Organization
__Note:__ The releavant files are provided with notes with them below after "<-".
```
.
├── data <- NOT ON GITHUB. GET THIS FOLDER FROM OSF AND UNZIP.
├── docs 
│   ├── docs
│   ├── mkdocs.yml
│   └── README.md
├── env_conda_imaginenet.yml            <- Python conda environment file for the project.
├── imagine                             <- Local project library for utility.
│   ├── __init__.py
│   ├── __pycache__
│   ├── config.py                       <- provides access project related directory paths.
│   ├── funpair_corr_analysis.py        <- functions for centrality correlational analysis.
│   └── sim_data.py                     <- functions to tabulate AI data and perform popuation diversity sampling for simulations.
├── Makefile
├── models                              <- Network analysis files.
│   ├── 1_datasets.R                    <- Sets up variables and loads data in R workspace and random seed. Always run this first to run other network analysis. Change the Working directory to use. 
│   ├── 2_networkimg_spearman_cstab.R   <- Estimates the networks, stores the centrality and CS coefficeint values.
│   ├── 3_clusters_net.R                <- Estimates network clusters and stores them.
│   ├── clustering_img                  <- RProject folder for clustering analysis.
│   ├── networkimg_ebg                  <- RProject folder for network estimates analysis.
│   └── r_project_network_and_cluster.zip <- Zip file of the clustering_img and networkimg_ebg and Available on OSF.
├── notebooks
│   ├── network_analysis_centrality_corr.ipynb <- Perform centrality correlations and plot heatmaps with multiple comparisons.
│   ├── network_analysis_cscoeff_and_clustering.ipynb <- View CS coefficent from centrality estimate, view clusters data and calculate and plot clustering alignment using ARI (adjusted rand score).
│   ├── population_diversity_sampling_merge_human.ipynb <- Create population divesity sampling dataset for AI simulations and combine data for network analysis.
│   ├── total_vivdness_score_analysis.ipynb <- analyze total vividness score using KS test between groups.
│   ├── view_centrality_corr_data.ipynb     <- view correlations csv with formatting.
│   └── wrangle_data_ai.ipynb               <- Clean the AI data for use.
├── pyproject.toml
├── README.md
├── reports
│   ├── figures                             <- contains figures in svg format.
│   └── tables.pptx

```

--------

