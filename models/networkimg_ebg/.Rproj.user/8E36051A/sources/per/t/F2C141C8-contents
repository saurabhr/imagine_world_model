library(tidyverse)
library(qgraph)
setwd("/Users/saurabh.ranjan/Documents/2020_2025_reality_monitoring_dissertation/E/imagine")
set.seed(444)

all_vviq_data <- read_csv("data/processed/all_vviq_groups.csv")
all_psiq_data <- read_csv("data/processed/all_psiq_groups.csv")

vviq_context <- rep(c('A','B','C','D','E','F','G','H'),each = 4)
psiq_context <- rep(c("App","So","Sm","Ta","To","Bo","Fe"),each = 3)

vviq_col_idx <- c(3:34)
psiq_col_idx <- c(4:24)

###############################
vviq_fl <- filter(all_vviq_data,groups=="FL")
vviq_pl_1 <- filter(all_vviq_data,groups=="PL-1")
vviq_pl_2 <- filter(all_vviq_data,groups=="PL-2")
vviq_pl <- filter(all_vviq_data,groups=="PL")
vviq_flpl <- bind_rows(vviq_fl,vviq_pl)

###############################

vviq_g12_i <- filter(all_vviq_data,groups=="gemma3:12b_independent")
vviq_g12qt_i <- filter(all_vviq_data,groups=="gemma3:12b-it-qat_independent")
vviq_g27_i <- filter(all_vviq_data,groups=="gemma3:27b_independent")
vviq_g27qt_i <- filter(all_vviq_data,groups=="gemma3:27b-it-qat_independent")
vviq_ll70_i <- filter(all_vviq_data,groups=="llama3.3:70b_independent")
vviq_llsc_i <- filter(all_vviq_data,groups=="llama4:scout_independent" )

###############################
vviq_g12_c <- filter(all_vviq_data,groups=="gemma3:12b_cumulative")
vviq_g12qt_c <- filter(all_vviq_data,groups=="gemma3:12b-it-qat_cumulative")
vviq_g27_c <- filter(all_vviq_data,groups=="gemma3:27b_cumulative")
vviq_g27qt_c <- filter(all_vviq_data,groups=="gemma3:27b-it-qat_cumulative")
vviq_ll70_c <- filter(all_vviq_data,groups=="llama3.3:70b_cumulative")
vviq_llsc_c <- filter(all_vviq_data,groups=="llama4:scout_cumulative")

###############################
psiq_fl <- filter(all_psiq_data,groups=="FL")
psiq_uk <- filter(all_psiq_data,groups=="UK")
psiq_ukfl <- filter(all_psiq_data,groups=="FL+UK")

###############################
psiq_g12_i <- filter(all_psiq_data,groups=="gemma3:12b_independent")
psiq_g12qt_i <- filter(all_psiq_data,groups=="gemma3:12b-it-qat_independent")
psiq_g27_i <- filter(all_psiq_data,groups=="gemma3:27b_independent")
psiq_g27qt_i <- filter(all_psiq_data,groups=="gemma3:27b-it-qat_independent")

psiq_ll70_i <- filter(all_psiq_data,groups=="llama3.3:70b_independent")
psiq_llsc_i <- filter(all_psiq_data,groups=="llama4:scout_independent")

###############################
psiq_g12_c <- filter(all_psiq_data,groups=="gemma3:12b_cumulative")
psiq_g12qt_c <- filter(all_psiq_data,groups=="gemma3:12b-it-qat_cumulative")
psiq_g27_c <- filter(all_psiq_data,groups=="gemma3:27b_cumulative")
psiq_g27qt_c <- filter(all_psiq_data,groups== "gemma3:27b-it-qat_cumulative")

psiq_ll70_c <- filter(all_psiq_data,groups=="llama3.3:70b_cumulative")
psiq_llsc_c <- filter(all_psiq_data,groups=="llama4:scout_cumulative")

###############################################################
