library(EGAnet)
vv_clus_fl <- bootEGA(
  vviq_fl[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

vv_clus_pl1 <- bootEGA(
  vviq_pl_1[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

vv_clus_pl2 <- bootEGA(
  vviq_pl_2[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_pl <- bootEGA(
  vviq_pl[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_flpl <- bootEGA(
  vviq_flpl[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

vv_clus_g12_i <- bootEGA(
  vviq_g12_i[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_g12qt_i <- bootEGA(
  vviq_g12qt_i[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_g27_i <- bootEGA(
  vviq_g27_i[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_g27qt_i <- bootEGA(
  vviq_g27qt_i[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_ll70_i <- bootEGA(
  vviq_ll70_i[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_llsc_i <- bootEGA(
  vviq_llsc_i[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)



vv_clus_g12_c <- bootEGA(
  vviq_g12_c[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_g12qt_c <- bootEGA(
  vviq_g12qt_c[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_g27_c <- bootEGA(
  vviq_g27_c[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

vv_clus_g27qt_c <- bootEGA(
  vviq_g27qt_c[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_ll70_c <- bootEGA(
  vviq_ll70_c[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
vv_clus_llsc_c <- bootEGA(
  vviq_llsc_c[,vviq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

####################################

ps_clus_fl <- bootEGA(
  psiq_fl[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

ps_clus_uk <- bootEGA(
  psiq_uk[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

ps_clus_ukfl <- bootEGA(
  psiq_ukfl[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)


ps_clus_g12_i <- bootEGA(
  psiq_g12_i[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_g12qt_i <- bootEGA(
  psiq_g12qt_i[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_g27_i <- bootEGA(
  psiq_g27_i[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_g27qt_i <- bootEGA(
  psiq_g27qt_i[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_ll70_i <- bootEGA(
  psiq_ll70_i[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_llsc_i <- bootEGA(
  psiq_llsc_i[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)



ps_clus_g12_c <- bootEGA(
  psiq_g12_c[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_g12qt_c <- bootEGA(
  psiq_g12qt_c[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_g27_c <- bootEGA(
  psiq_g27_c[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_g27qt_c <- bootEGA(
  psiq_g27qt_c[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_ll70_c <- bootEGA(
  psiq_ll70_c[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)
ps_clus_llsc_c <- bootEGA(
  psiq_llsc_c[,psiq_col_idx],
  corr = "spearman",
  model = "glasso",
  algorithm = "walktrap",
  uni.method = "LE",
  iter = 5000,
  type = "resampling",
  ncores=8,
  EGA.type = "EGA",
  seed = 444,
  plot.typicalStructure=TRUE
)

clusters_vv_eg <- data.frame(fl = vv_clus_fl$EGA$wc)
clusters_vv_eg$pl1 <- vv_clus_pl1$EGA$wc
clusters_vv_eg$pl2 <- vv_clus_pl2$EGA$wc
clusters_vv_eg$pl <- vv_clus_pl$EGA$wc
clusters_vv_eg$flpl <- vv_clus_flpl$EGA$wc

clusters_vv_eg$g12_i <- vv_clus_g12_i$EGA$wc
clusters_vv_eg$g12qt_i <- vv_clus_g12qt_i$EGA$wc
clusters_vv_eg$g27_i <- vv_clus_g27_i$EGA$wc
clusters_vv_eg$g27qt_i <- vv_clus_g27qt_i$EGA$wc
clusters_vv_eg$ll70_i <- vv_clus_ll70_i$EGA$wc
clusters_vv_eg$llsc_i <- vv_clus_llsc_i$EGA$wc

clusters_vv_eg$g12_c <- vv_clus_g12_c$EGA$wc
clusters_vv_eg$g12qt_c <- vv_clus_g12qt_c$EGA$wc
clusters_vv_eg$g27_c <- vv_clus_g27_c$EGA$wc
clusters_vv_eg$g27qt_c <- vv_clus_g27qt_c$EGA$wc
clusters_vv_eg$ll70_c <- vv_clus_ll70_c$EGA$wc
clusters_vv_eg$llsc_c <- vv_clus_llsc_c$EGA$wc
write.csv(clusters_vv_eg, "data/processed/clusters_vv_eg.csv")


clusters_ps_eg <- data.frame(fl = ps_clus_fl$EGA$wc)
clusters_ps_eg$uk <- ps_clus_uk$EGA$wc
clusters_ps_eg$ukfl <- ps_clus_ukfl$EGA$wc

clusters_ps_eg$g12_i <- ps_clus_g12_i$EGA$wc
clusters_ps_eg$g12qt_i <- ps_clus_g12qt_i$EGA$wc
clusters_ps_eg$g27_i <- ps_clus_g27_i$EGA$wc
clusters_ps_eg$g27qt_i <- ps_clus_g27qt_i$EGA$wc
clusters_ps_eg$ll70_i <- ps_clus_ll70_i$EGA$wc
clusters_ps_eg$llsc_i <- ps_clus_llsc_i$EGA$wc

clusters_ps_eg$g12_c <- ps_clus_g12_c$EGA$wc
clusters_ps_eg$g12qt_c <- ps_clus_g12qt_c$EGA$wc
clusters_ps_eg$g27_c <- ps_clus_g27_c$EGA$wc
clusters_ps_eg$g27qt_c <- ps_clus_g27qt_c$EGA$wc
clusters_ps_eg$ll70_c <- ps_clus_ll70_c$EGA$wc
clusters_ps_eg$llsc_c <- ps_clus_llsc_c$EGA$wc
write.csv(clusters_ps_eg, "data/processed/clusters_ps_eg.csv")



