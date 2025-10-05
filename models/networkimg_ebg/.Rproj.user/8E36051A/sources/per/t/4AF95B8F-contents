library(bootnet)
library(qgraph)
nboot <- 5000
net_estimsate <- "EBICglasso"
corMethod <- "spearman"
ncase <- 500

##############
bt_sp_eg_vv_fl <- estimateNetwork(vviq_fl[, vviq_col_idx],
                                default = net_estimsate,
                                corMethod = corMethod
)
bt_sp_eg_vv_fl_casdrp <- bootnet(bt_sp_eg_vv_fl, # case dropping
                               nBoots = nboot,
                               caseN = ncase,
                               type = "case",
                               nCores = 8,
                               statistics = c(
                                 "strength",
                                 "expectedInfluence",
                                 "betweenness",
                                 "closeness"
                               )
)
corStab_sp_eg_vv_fl <- corStability(bt_sp_eg_vv_fl_casdrp)

#pdf(file="reports/figures/svg/vv_fl_plot.pdf", paper = "a4r")
#vv_fl_plot <- plot(bt_sp_eg_vv_fl,groups = vviq_context,palette = "pastel")
#dev.off()
##############
bt_sp_eg_vv_pl1 <- estimateNetwork(vviq_pl_1[, vviq_col_idx],
                                 default = net_estimsate,
                                 corMethod = corMethod
)
bt_sp_eg_vv_pl1_casdrp <- bootnet(bt_sp_eg_vv_pl1, # case dropping
                                nBoots = nboot,
                                caseN = ncase,
                                type = "case",
                                nCores = 8,
                                statistics = c(
                                  "strength",
                                  "expectedInfluence",
                                  "betweenness",
                                  "closeness"
                                )
)
corStab_sp_eg_vv_pl1 <- corStability(bt_sp_eg_vv_pl1_casdrp)



##############
bt_sp_eg_vv_pl2 <- estimateNetwork(vviq_pl_2[, vviq_col_idx],
                                 default = net_estimsate,
                                 corMethod = corMethod
)
bt_sp_eg_vv_pl2_casdrp <- bootnet(bt_sp_eg_vv_pl2, # case dropping
                                nBoots = nboot,
                                caseN = ncase,
                                type = "case",
                                nCores = 8,
                                statistics = c(
                                  "strength",
                                  "expectedInfluence",
                                  "betweenness",
                                  "closeness"
                                )
)
corStab_sp_eg_vv_pl2 <- corStability(bt_sp_eg_vv_pl2_casdrp)

##############
bt_sp_eg_vv_pl <- estimateNetwork(vviq_pl[, vviq_col_idx],
                                default = net_estimsate,
                                corMethod = corMethod
)
bt_sp_eg_vv_pl_casdrp <- bootnet(bt_sp_eg_vv_pl, # case dropping
                               nBoots = nboot,
                               caseN = ncase,
                               type = "case",
                               nCores = 8,
                               statistics = c(
                                 "strength",
                                 "expectedInfluence",
                                 "betweenness",
                                 "closeness"
                               )
)
corStab_sp_eg_vv_pl <- corStability(bt_sp_eg_vv_pl_casdrp)

##############
bt_sp_eg_vv_flpl <- estimateNetwork(vviq_flpl[, vviq_col_idx],
                                  default = net_estimsate,
                                  corMethod = corMethod
)
bt_sp_eg_vv_flpl_casdrp <- bootnet(bt_sp_eg_vv_flpl, # case dropping
                                 nBoots = nboot,
                                 caseN = ncase,
                                 type = "case",
                                 nCores = 8,
                                 statistics = c(
                                   "strength",
                                   "expectedInfluence",
                                   "betweenness",
                                   "closeness"
                                 )
)
corStab_sp_eg_vv_flpl <- corStability(bt_sp_eg_vv_flpl_casdrp)

###############################################################
# PCOR Centrality VVIQ LLM INDEPENDENT TASK
###############################################################

bt_sp_eg_vv_g12_i <- estimateNetwork(vviq_g12_i[, vviq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_vv_g12_i_casdrp <- bootnet(bt_sp_eg_vv_g12_i, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_vv_g12_i <- corStability(bt_sp_eg_vv_g12_i_casdrp)

##############
bt_sp_eg_vv_g12qt_i <- estimateNetwork(vviq_g12qt_i[, vviq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_vv_g12qt_i_casdrp <- bootnet(bt_sp_eg_vv_g12qt_i, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_vv_g12qt_i <- corStability(bt_sp_eg_vv_g12qt_i_casdrp)

##############
bt_sp_eg_vv_g27_i <- estimateNetwork(vviq_g27_i[, vviq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_vv_g27_i_casdrp <- bootnet(bt_sp_eg_vv_g27_i, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_vv_g27_i <- corStability(bt_sp_eg_vv_g27_i_casdrp)

##############
bt_sp_eg_vv_g27qt_i <- estimateNetwork(vviq_g27qt_i[, vviq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_vv_g27qt_i_casdrp <- bootnet(bt_sp_eg_vv_g27qt_i, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_vv_g27qt_i <- corStability(bt_sp_eg_vv_g27qt_i_casdrp)

##############
bt_sp_eg_vv_ll70_i <- estimateNetwork(vviq_ll70_i[, vviq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_vv_ll70_i_casdrp <- bootnet(bt_sp_eg_vv_ll70_i, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_vv_ll70_i <- corStability(bt_sp_eg_vv_ll70_i_casdrp)

##############
bt_sp_eg_vv_llsc_i <- estimateNetwork(vviq_llsc_i[, vviq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_vv_llsc_i_casdrp <- bootnet(bt_sp_eg_vv_llsc_i, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_vv_llsc_i <- corStability(bt_sp_eg_vv_llsc_i_casdrp)

###############################################################
# PCOR Centrality VVIQ LLM CUMULATIVE TASK
###############################################################

bt_sp_eg_vv_g12_c <- estimateNetwork(vviq_g12_c[, vviq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_vv_g12_c_casdrp <- bootnet(bt_sp_eg_vv_g12_c, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_vv_g12_c <- corStability(bt_sp_eg_vv_g12_c_casdrp)

##############
bt_sp_eg_vv_g12qt_c <- estimateNetwork(vviq_g12qt_c[, vviq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_vv_g12qt_c_casdrp <- bootnet(bt_sp_eg_vv_g12qt_c, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_vv_g12qt_c <- corStability(bt_sp_eg_vv_g12qt_c_casdrp)


##############
bt_sp_eg_vv_g27_c <- estimateNetwork(vviq_g27_c[, vviq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_vv_g27_c_casdrp <- bootnet(bt_sp_eg_vv_g27_c, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_vv_g27_c <- corStability(bt_sp_eg_vv_g27_c_casdrp)


##############
bt_sp_eg_vv_g27qt_c <- estimateNetwork(vviq_g27qt_c[, vviq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_vv_g27qt_c_casdrp <- bootnet(bt_sp_eg_vv_g27qt_c, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_vv_g27qt_c <- corStability(bt_sp_eg_vv_g27qt_c_casdrp)


##############
bt_sp_eg_vv_ll70_c <- estimateNetwork(vviq_ll70_c[, vviq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_vv_ll70_c_casdrp <- bootnet(bt_sp_eg_vv_ll70_c, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_vv_ll70_c <- corStability(bt_sp_eg_vv_ll70_c_casdrp)


##############
bt_sp_eg_vv_llsc_c <- estimateNetwork(vviq_llsc_c[, vviq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_vv_llsc_c_casdrp <- bootnet(bt_sp_eg_vv_llsc_c, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_vv_llsc_c <- corStability(bt_sp_eg_vv_llsc_c_casdrp)



###############################################################
# PCOR Centrality PSIQ HUMANS
###############################################################

bt_sp_eg_ps_fl <- estimateNetwork(psiq_fl[, psiq_col_idx],
                                default = net_estimsate,
                                corMethod = corMethod
)
bt_sp_eg_ps_fl_casdrp <- bootnet(bt_sp_eg_ps_fl, # case dropping
                               nBoots = nboot,
                               caseN = ncase,
                               type = "case",
                               nCores = 8,
                               statistics = c(
                                 "strength",
                                 "expectedInfluence",
                                 "betweenness",
                                 "closeness"
                               )
)
corStab_sp_eg_ps_fl <- corStability(bt_sp_eg_ps_fl_casdrp)


##############
bt_sp_eg_ps_uk <- estimateNetwork(psiq_uk[, psiq_col_idx],
                                default = net_estimsate,
                                corMethod = corMethod
)
bt_sp_eg_ps_uk_casdrp <- bootnet(bt_sp_eg_ps_uk, # case dropping
                               nBoots = nboot,
                               caseN = ncase,
                               type = "case",
                               nCores = 8,
                               statistics = c(
                                 "strength",
                                 "expectedInfluence",
                                 "betweenness",
                                 "closeness"
                               )
)
corStab_sp_eg_ps_uk <- corStability(bt_sp_eg_ps_uk_casdrp)


##############
bt_sp_eg_ps_ukfl <- estimateNetwork(psiq_ukfl[, psiq_col_idx],
                                  default = net_estimsate,
                                  corMethod = corMethod
)
bt_sp_eg_ps_ukfl_casdrp <- bootnet(bt_sp_eg_ps_ukfl, # case dropping
                                 nBoots = nboot,
                                 caseN = ncase,
                                 type = "case",
                                 nCores = 8,
                                 statistics = c(
                                   "strength",
                                   "expectedInfluence",
                                   "betweenness",
                                   "closeness"
                                 )
)
corStab_sp_eg_ps_ukfl <- corStability(bt_sp_eg_ps_ukfl_casdrp)



###############################################################
# PCOR Centrality PSIQ LLM INDEPENDENT TASK
###############################################################

bt_sp_eg_ps_g12_i <- estimateNetwork(psiq_g12_i[, psiq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_ps_g12_i_casdrp <- bootnet(bt_sp_eg_ps_g12_i, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_ps_g12_i <- corStability(bt_sp_eg_ps_g12_i_casdrp)

##############

bt_sp_eg_ps_g12qt_i <- estimateNetwork(psiq_g12qt_i[, psiq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_ps_g12qt_i_casdrp <- bootnet(bt_sp_eg_ps_g12qt_i, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_ps_g12qt_i <- corStability(bt_sp_eg_ps_g12qt_i_casdrp)

##############

bt_sp_eg_ps_g27_i <- estimateNetwork(psiq_g27_i[, psiq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_ps_g27_i_casdrp <- bootnet(bt_sp_eg_ps_g27_i, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_ps_g27_i <- corStability(bt_sp_eg_ps_g27_i_casdrp)


##############
bt_sp_eg_ps_g27qt_i <- estimateNetwork(psiq_g27qt_i[, psiq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_ps_g27qt_i_casdrp <- bootnet(bt_sp_eg_ps_g27qt_i, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_ps_g27qt_i <- corStability(bt_sp_eg_ps_g27qt_i_casdrp)

##############
bt_sp_eg_ps_ll70_i <- estimateNetwork(psiq_ll70_i[, psiq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_ps_ll70_i_casdrp <- bootnet(bt_sp_eg_ps_ll70_i, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_ps_ll70_i <- corStability(bt_sp_eg_ps_ll70_i_casdrp)


##############
bt_sp_eg_ps_llsc_i <- estimateNetwork(psiq_llsc_i[, psiq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_ps_llsc_i_casdrp <- bootnet(bt_sp_eg_ps_llsc_i, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_ps_llsc_i <- corStability(bt_sp_eg_ps_llsc_i_casdrp)



###############################################################
# PCOR Centrality PSIQ LLM CUMULATIVE TASK
###############################################################


bt_sp_eg_ps_g12_c <- estimateNetwork(psiq_g12_c[, psiq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_ps_g12_c_casdrp <- bootnet(bt_sp_eg_ps_g12_c, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_ps_g12_c <- corStability(bt_sp_eg_ps_g12_c_casdrp)


##############
bt_sp_eg_ps_g12qt_c <- estimateNetwork(psiq_g12qt_c[, psiq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_ps_g12qt_c_casdrp <- bootnet(bt_sp_eg_ps_g12qt_c, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_ps_g12qt_c <- corStability(bt_sp_eg_ps_g12qt_c_casdrp)
##############

bt_sp_eg_ps_g27_c <- estimateNetwork(psiq_g27_c[, psiq_col_idx],
                                   default = net_estimsate,
                                   corMethod = corMethod
)
bt_sp_eg_ps_g27_c_casdrp <- bootnet(bt_sp_eg_ps_g27_c, # case dropping
                                  nBoots = nboot,
                                  caseN = ncase,
                                  type = "case",
                                  nCores = 8,
                                  statistics = c(
                                    "strength",
                                    "expectedInfluence",
                                    "betweenness",
                                    "closeness"
                                  )
)
corStab_sp_eg_ps_g27_c <- corStability(bt_sp_eg_ps_g27_c_casdrp)

##############

bt_sp_eg_ps_g27qt_c <- estimateNetwork(psiq_g27qt_c[, psiq_col_idx],
                                     default = net_estimsate,
                                     corMethod = corMethod
)
bt_sp_eg_ps_g27qt_c_casdrp <- bootnet(bt_sp_eg_ps_g27qt_c, # case dropping
                                    nBoots = nboot,
                                    caseN = ncase,
                                    type = "case",
                                    nCores = 8,
                                    statistics = c(
                                      "strength",
                                      "expectedInfluence",
                                      "betweenness",
                                      "closeness"
                                    )
)
corStab_sp_eg_ps_g27qt_c <- corStability(bt_sp_eg_ps_g27qt_c_casdrp)

##############

bt_sp_eg_ps_ll70_c <- estimateNetwork(psiq_ll70_c[, psiq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_ps_ll70_c_casdrp <- bootnet(bt_sp_eg_ps_ll70_c, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_ps_ll70_c <- corStability(bt_sp_eg_ps_ll70_c_casdrp)

##############

bt_sp_eg_ps_llsc_c <- estimateNetwork(psiq_llsc_c[, psiq_col_idx],
                                    default = net_estimsate,
                                    corMethod = corMethod
)
bt_sp_eg_ps_llsc_c_casdrp <- bootnet(bt_sp_eg_ps_llsc_c, # case dropping
                                   nBoots = nboot,
                                   caseN = ncase,
                                   type = "case",
                                   nCores = 8,
                                   statistics = c(
                                     "strength",
                                     "expectedInfluence",
                                     "betweenness",
                                     "closeness"
                                   )
)
corStab_sp_eg_ps_llsc_c <- corStability(bt_sp_eg_ps_llsc_c_casdrp)

vv_avg_layout <- averageLayout(bt_sp_eg_vv_fl,
                               bt_sp_eg_vv_pl1,
                               bt_sp_eg_vv_pl2,
                               bt_sp_eg_vv_pl,
                               bt_sp_eg_vv_flpl,
                               bt_sp_eg_vv_g12_i,
                               bt_sp_eg_vv_g12qt_i,
                               bt_sp_eg_vv_g27_i,
                               bt_sp_eg_vv_g27qt_i,
                               bt_sp_eg_vv_ll70_i,
                               bt_sp_eg_vv_llsc_i,
                               bt_sp_eg_vv_g12_c,
                               bt_sp_eg_vv_g12qt_c,
                               bt_sp_eg_vv_g27_c,
                               bt_sp_eg_vv_g27qt_c,
                               bt_sp_eg_vv_ll70_c,
                               bt_sp_eg_vv_llsc_c)

ps_avg_layout <- averageLayout(bt_sp_eg_ps_fl,
                               bt_sp_eg_ps_uk,
                               bt_sp_eg_ps_ukfl,
                               bt_sp_eg_ps_g12_i,
                               bt_sp_eg_ps_g12qt_i,
                               bt_sp_eg_ps_g27_i,
                               bt_sp_eg_ps_g27qt_i,
                               bt_sp_eg_ps_ll70_i,
                               bt_sp_eg_ps_llsc_i,
                               bt_sp_eg_ps_g12_c,
                               bt_sp_eg_ps_g12qt_c,
                               bt_sp_eg_ps_g27_c,
                               bt_sp_eg_ps_g27qt_c,
                               bt_sp_eg_ps_ll70_c,
                               bt_sp_eg_ps_llsc_c)

filetype <- "pdf"
#qgraph(bt_sp_eg_ps_fl$graph, layout = ps_avg_layout,groups = psiq_context, title = "Graph 1 with avg layout")
#qgraph(bt_sp_eg_ps_g27qt_i$graph, layout = ps_avg_layout,groups = psiq_context, title = "Graph 1 with avg layout")
#qgraph(bt_sp_eg_ps_g27qt_i$graph,groups = psiq_context,layout="spring")

qgraph(bt_sp_eg_vv_fl$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_fl", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_fl",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_pl1$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_pl1", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_pl1",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_pl2$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_pl2", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_pl2",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_pl$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_pl", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_pl",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_flpl$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_flpl", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_flpl",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g12_i$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g12_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g12_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g12qt_i$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g12qt_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g12qt_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g27_i$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g27_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g27_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g27qt_i$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g27qt_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g27qt_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_ll70_i$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_ll70_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_ll70_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_llsc_i$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_llsc_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_llsc_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g12_c$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g12_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g12_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g12qt_c$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g12qt_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g12qt_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g27_c$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g27_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g27_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_g27qt_c$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_g27qt_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_g27qt_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_ll70_c$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_ll70_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_ll70_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_vv_llsc_c$graph,groups = vviq_context, palette = "pastel", title = "bt_sp_eg_vv_llsc_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_vv_llsc_c",filetype = filetype,layout="spring")


qgraph(bt_sp_eg_ps_fl$graph,groups = psiq_context, labels = colnames(psiq_fl[,psiq_col_idx]), title = "bt_sp_eg_ps_fl", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_fl",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_uk$graph,groups = psiq_context, labels = colnames(psiq_uk[,psiq_col_idx]), title = "bt_sp_eg_ps_uk", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_uk",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_ukfl$graph,groups = psiq_context, labels = colnames(psiq_ukfl[,psiq_col_idx]), title = "bt_sp_eg_ps_ukfl", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_ukfl",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g12_i$graph,groups = psiq_context, labels = colnames(psiq_g12_i[,psiq_col_idx]), title = "bt_sp_eg_ps_g12_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g12_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g12qt_i$graph,groups = psiq_context, labels = colnames(psiq_g12qt_i[,psiq_col_idx]), title = "bt_sp_eg_ps_g12qt_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g12qt_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g27_i$graph,groups = psiq_context, labels = colnames(psiq_g27_i[,psiq_col_idx]), title = "bt_sp_eg_ps_g27_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g27_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g27qt_i$graph,groups = psiq_context, labels = colnames(psiq_g27qt_i[,psiq_col_idx]), title = "bt_sp_eg_ps_g27qt_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g27qt_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_ll70_i$graph,groups = psiq_context, labels = colnames(psiq_ll70_i[,psiq_col_idx]), title = "bt_sp_eg_ps_ll70_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_ll70_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_llsc_i$graph,groups = psiq_context, labels = colnames(psiq_llsc_i[,psiq_col_idx]), title = "bt_sp_eg_ps_llsc_i", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_llsc_i",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g12_c$graph,groups = psiq_context, labels = colnames(psiq_g12_c[,psiq_col_idx]), title = "bt_sp_eg_ps_g12_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g12_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g12qt_c$graph,groups = psiq_context, labels = colnames(psiq_g12qt_c[,psiq_col_idx]), title = "bt_sp_eg_ps_g12qt_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g12qt_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g27_c$graph,groups = psiq_context, labels = colnames(psiq_g27_c[,psiq_col_idx]), title = "bt_sp_eg_ps_g27_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g27_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_g27qt_c$graph,groups = psiq_context, labels = colnames(psiq_g27qt_c[,psiq_col_idx]), title = "bt_sp_eg_ps_g27qt_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_g27qt_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_ll70_c$graph,groups = psiq_context, labels = colnames(psiq_ll70_c[,psiq_col_idx]), title = "bt_sp_eg_ps_ll70_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_ll70_c",filetype = filetype,layout="spring")
qgraph(bt_sp_eg_ps_llsc_c$graph,groups = psiq_context, labels = colnames(psiq_llsc_c[,psiq_col_idx]), title = "bt_sp_eg_ps_llsc_c", filename = "reports/figures/svg/sp_eb/bt_sp_eg_ps_llsc_c",filetype = filetype,layout="spring")

bt_sp_eg_vv_fl_ct <- centralityTable(bt_sp_eg_vv_fl, standardized = FALSE)
bt_sp_eg_vv_pl1_ct <- centralityTable(bt_sp_eg_vv_pl1, standardized = FALSE)
bt_sp_eg_vv_pl2_ct <- centralityTable(bt_sp_eg_vv_pl2, standardized = FALSE)
bt_sp_eg_vv_pl_ct <- centralityTable(bt_sp_eg_vv_pl, standardized = FALSE)
bt_sp_eg_vv_flpl_ct <- centralityTable(bt_sp_eg_vv_flpl, standardized = FALSE)

bt_sp_eg_vv_fl_ct$task <- "vviq"
bt_sp_eg_vv_fl_ct$group <- "fl"
bt_sp_eg_vv_fl_ct$model <- "human"

bt_sp_eg_vv_pl1_ct$task <- "vviq"
bt_sp_eg_vv_pl1_ct$group <- "pl1"
bt_sp_eg_vv_pl1_ct$model <- "human"

bt_sp_eg_vv_pl2_ct$task <- "vviq"
bt_sp_eg_vv_pl2_ct$group <- "pl2"
bt_sp_eg_vv_pl2_ct$model <- "human"

bt_sp_eg_vv_pl_ct$task <- "vviq"
bt_sp_eg_vv_pl_ct$group <- "pl"
bt_sp_eg_vv_pl_ct$model <- "human"

bt_sp_eg_vv_flpl_ct$task <- "vviq"
bt_sp_eg_vv_flpl_ct$group <- "plfl"
bt_sp_eg_vv_flpl_ct$model <- "human"


bt_sp_eg_centrality_vviq_humans <- bind_rows(bt_sp_eg_vv_fl_ct,
                                         bt_sp_eg_vv_pl1_ct,
                                         bt_sp_eg_vv_pl2_ct,
                                         bt_sp_eg_vv_pl_ct,
                                         bt_sp_eg_vv_pl_ct,
                                         bt_sp_eg_vv_flpl_ct)

write_csv(bt_sp_eg_centrality_vviq_humans,"data/processed/bt_sp_eg_centrality_vviq_humans.csv")

bt_sp_eg_vv_g12_i_ct <- centralityTable(bt_sp_eg_vv_g12_i, standardized = FALSE)
bt_sp_eg_vv_g12qt_i_ct <- centralityTable(bt_sp_eg_vv_g12qt_i, standardized = FALSE)
bt_sp_eg_vv_g27_i_ct <- centralityTable(bt_sp_eg_vv_g27_i, standardized = FALSE)
bt_sp_eg_vv_g27qt_i_ct <- centralityTable(bt_sp_eg_vv_g27qt_i, standardized = FALSE)
bt_sp_eg_vv_ll70_i_ct <- centralityTable(bt_sp_eg_vv_ll70_i, standardized = FALSE)
bt_sp_eg_vv_llsc_i_ct <- centralityTable(bt_sp_eg_vv_llsc_i, standardized = FALSE)
bt_sp_eg_vv_g12_c_ct <- centralityTable(bt_sp_eg_vv_g12_c, standardized = FALSE)
bt_sp_eg_vv_g12qt_c_ct <- centralityTable(bt_sp_eg_vv_g12qt_c, standardized = FALSE)
bt_sp_eg_vv_g27_c_ct <- centralityTable(bt_sp_eg_vv_g27_c, standardized = FALSE)
bt_sp_eg_vv_g27qt_c_ct <- centralityTable(bt_sp_eg_vv_g27qt_c, standardized = FALSE)
bt_sp_eg_vv_ll70_c_ct <- centralityTable(bt_sp_eg_vv_ll70_c, standardized = FALSE)
bt_sp_eg_vv_llsc_c_ct <- centralityTable(bt_sp_eg_vv_llsc_c, standardized = FALSE)


bt_sp_eg_vv_g12_i_ct$task <- "vviq"
bt_sp_eg_vv_g12_i_ct$group <- "independent"
bt_sp_eg_vv_g12_i_ct$model <- "g12"

bt_sp_eg_vv_g12qt_i_ct$task <- "vviq"
bt_sp_eg_vv_g12qt_i_ct$group <- "independent"
bt_sp_eg_vv_g12qt_i_ct$model <- "g12qt"

bt_sp_eg_vv_g27_i_ct$task <- "vviq"
bt_sp_eg_vv_g27_i_ct$group <- "independent"
bt_sp_eg_vv_g27_i_ct$model <- "g27"

bt_sp_eg_vv_g27qt_i_ct$task <- "vviq"
bt_sp_eg_vv_g27qt_i_ct$group <- "independent"
bt_sp_eg_vv_g27qt_i_ct$model <- "g27qt"

bt_sp_eg_vv_ll70_i_ct$task <- "vviq"
bt_sp_eg_vv_ll70_i_ct$group <- "independent"
bt_sp_eg_vv_ll70_i_ct$model <- "ll70"

bt_sp_eg_vv_llsc_i_ct$task <- "vviq"
bt_sp_eg_vv_llsc_i_ct$group <- "independent"
bt_sp_eg_vv_llsc_i_ct$model <- "llsc"

bt_sp_eg_vv_g12_c_ct$task <- "vviq"
bt_sp_eg_vv_g12_c_ct$group <- "cumulative"
bt_sp_eg_vv_g12_c_ct$model <- "g12"

bt_sp_eg_vv_g12qt_c_ct$task <- "vviq"
bt_sp_eg_vv_g12qt_c_ct$group <- "cumulative"
bt_sp_eg_vv_g12qt_c_ct$model <- "g12qt"

bt_sp_eg_vv_g27_c_ct$task <- "vviq"
bt_sp_eg_vv_g27_c_ct$group <- "cumulative"
bt_sp_eg_vv_g27_c_ct$model <- "g27"

bt_sp_eg_vv_g27qt_c_ct$task <- "vviq"
bt_sp_eg_vv_g27qt_c_ct$group <- "cumulative"
bt_sp_eg_vv_g27qt_c_ct$model <- "g27qt" 

bt_sp_eg_vv_ll70_c_ct$task <- "vviq"
bt_sp_eg_vv_ll70_c_ct$group <- "cumulative"
bt_sp_eg_vv_ll70_c_ct$model <- "ll70"

bt_sp_eg_vv_llsc_c_ct$task <- "vviq"
bt_sp_eg_vv_llsc_c_ct$group <- "cumulative"
bt_sp_eg_vv_llsc_c_ct$model <- "llsc"


bt_sp_eg_centrality_vviq_models <- bind_rows(bt_sp_eg_vv_g12_i_ct,
                                         bt_sp_eg_vv_g12qt_i_ct,
                                         bt_sp_eg_vv_g27_i_ct,
                                         bt_sp_eg_vv_g27qt_i_ct,
                                         bt_sp_eg_vv_ll70_i_ct,
                                         bt_sp_eg_vv_llsc_i_ct,
                                         bt_sp_eg_vv_g12_c_ct,
                                         bt_sp_eg_vv_g12qt_c_ct,
                                         bt_sp_eg_vv_g27_c_ct,
                                         bt_sp_eg_vv_g27qt_c_ct,
                                         bt_sp_eg_vv_ll70_c_ct,
                                         bt_sp_eg_vv_llsc_c_ct)

write_csv(bt_sp_eg_centrality_vviq_models,"data/processed/bt_sp_eg_centrality_vviq_models.csv")

###################
bt_sp_eg_ps_fl_ct <- centralityTable(bt_sp_eg_ps_fl, standardized = FALSE)
bt_sp_eg_ps_uk_ct <- centralityTable(bt_sp_eg_ps_uk, standardized = FALSE)
bt_sp_eg_ps_ukfl_ct <- centralityTable(bt_sp_eg_ps_ukfl, standardized = FALSE)

bt_sp_eg_ps_fl_ct$task <- "psiq"
bt_sp_eg_ps_fl_ct$group <- "fl"
bt_sp_eg_ps_fl_ct$model <- "human"

bt_sp_eg_ps_uk_ct$task <- "psiq"
bt_sp_eg_ps_uk_ct$group <- "uk"
bt_sp_eg_ps_uk_ct$model <- "human"

bt_sp_eg_ps_ukfl_ct$task <- "psiq"
bt_sp_eg_ps_ukfl_ct$group <- "ukfl"
bt_sp_eg_ps_ukfl_ct$model <- "human"


bt_sp_eg_centrality_psiq_humans <- bind_rows(bt_sp_eg_ps_fl_ct,
                                         bt_sp_eg_ps_uk_ct,
                                         bt_sp_eg_ps_ukfl_ct)

write_csv(bt_sp_eg_centrality_psiq_humans,"data/processed/bt_sp_eg_centrality_psiq_humans.csv")

bt_sp_eg_ps_g12_i_ct <- centralityTable(bt_sp_eg_ps_g12_i, standardized = FALSE)
bt_sp_eg_ps_g12qt_i_ct <- centralityTable(bt_sp_eg_ps_g12qt_i, standardized = FALSE)
bt_sp_eg_ps_g27_i_ct <- centralityTable(bt_sp_eg_ps_g27_i, standardized = FALSE)
bt_sp_eg_ps_g27qt_i_ct <- centralityTable(bt_sp_eg_ps_g27qt_i, standardized = FALSE)
bt_sp_eg_ps_ll70_i_ct <- centralityTable(bt_sp_eg_ps_ll70_i, standardized = FALSE)
bt_sp_eg_ps_llsc_i_ct <- centralityTable(bt_sp_eg_ps_llsc_i, standardized = FALSE)
bt_sp_eg_ps_g12_c_ct <- centralityTable(bt_sp_eg_ps_g12_c, standardized = FALSE)
bt_sp_eg_ps_g12qt_c_ct <- centralityTable(bt_sp_eg_ps_g12qt_c, standardized = FALSE)
bt_sp_eg_ps_g27_c_ct <- centralityTable(bt_sp_eg_ps_g27_c, standardized = FALSE)
bt_sp_eg_ps_g27qt_c_ct <- centralityTable(bt_sp_eg_ps_g27qt_c, standardized = FALSE)
bt_sp_eg_ps_ll70_c_ct <- centralityTable(bt_sp_eg_ps_ll70_c, standardized = FALSE)
bt_sp_eg_ps_llsc_c_ct <- centralityTable(bt_sp_eg_ps_llsc_c, standardized = FALSE)


bt_sp_eg_ps_g12_i_ct$task <- "psiq"
bt_sp_eg_ps_g12_i_ct$group <- "independent"
bt_sp_eg_ps_g12_i_ct$model <- "g12"

bt_sp_eg_ps_g12qt_i_ct$task <- "psiq"
bt_sp_eg_ps_g12qt_i_ct$group <- "independent"
bt_sp_eg_ps_g12qt_i_ct$model <- "g12qt"

bt_sp_eg_ps_g27_i_ct$task <- "psiq"
bt_sp_eg_ps_g27_i_ct$group <- "independent"
bt_sp_eg_ps_g27_i_ct$model <- "g27"

bt_sp_eg_ps_g27qt_i_ct$task <- "psiq"
bt_sp_eg_ps_g27qt_i_ct$group <- "independent"
bt_sp_eg_ps_g27qt_i_ct$model <- "g27qt"

bt_sp_eg_ps_ll70_i_ct$task <- "psiq"
bt_sp_eg_ps_ll70_i_ct$group <- "independent"
bt_sp_eg_ps_ll70_i_ct$model <- "ll70"

bt_sp_eg_ps_llsc_i_ct$task <- "psiq"
bt_sp_eg_ps_llsc_i_ct$group <- "independent"
bt_sp_eg_ps_llsc_i_ct$model <- "llsc"

bt_sp_eg_ps_g12_c_ct$task <- "psiq"
bt_sp_eg_ps_g12_c_ct$group <- "cumulative"
bt_sp_eg_ps_g12_c_ct$model <- "g12"

bt_sp_eg_ps_g12qt_c_ct$task <- "psiq"
bt_sp_eg_ps_g12qt_c_ct$group <- "cumulative"
bt_sp_eg_ps_g12qt_c_ct$model <- "g12qt"

bt_sp_eg_ps_g27_c_ct$task <- "psiq"
bt_sp_eg_ps_g27_c_ct$group <- "cumulative"
bt_sp_eg_ps_g27_c_ct$model <- "g27"

bt_sp_eg_ps_g27qt_c_ct$task <- "psiq"
bt_sp_eg_ps_g27qt_c_ct$group <- "cumulative"
bt_sp_eg_ps_g27qt_c_ct$model <- "g27qt"

bt_sp_eg_ps_ll70_c_ct$task <- "psiq"
bt_sp_eg_ps_ll70_c_ct$group <- "cumulative"
bt_sp_eg_ps_ll70_c_ct$model <- "ll70"

bt_sp_eg_ps_llsc_c_ct$task <- "psiq"
bt_sp_eg_ps_llsc_c_ct$group <- "cumulative"
bt_sp_eg_ps_llsc_c_ct$model <- "llsc"

bt_sp_eg_centrality_psiq_models <- bind_rows(bt_sp_eg_ps_g12_i_ct,
                                         bt_sp_eg_ps_g12qt_i_ct,
                                         bt_sp_eg_ps_g27_i_ct,
                                         bt_sp_eg_ps_g27qt_i_ct,
                                         bt_sp_eg_ps_ll70_i_ct,
                                         bt_sp_eg_ps_llsc_i_ct,
                                         bt_sp_eg_ps_g12_c_ct,
                                         bt_sp_eg_ps_g12qt_c_ct,
                                         bt_sp_eg_ps_g27_c_ct,
                                         bt_sp_eg_ps_g27qt_c_ct,
                                         bt_sp_eg_ps_ll70_c_ct,
                                         bt_sp_eg_ps_llsc_c_ct)

write_csv(bt_sp_eg_centrality_psiq_models,"data/processed/bt_sp_eg_centrality_psiq_models.csv")


corStab_sp_eg_vv_fl_df <- data.frame(
  Name = names(corStab_sp_eg_vv_fl),
  Value = as.numeric(corStab_sp_eg_vv_fl) # Ensure the values are numeric
)

corStab_sp_eg_vv_pl1_df <- data.frame(
  Name = names(corStab_sp_eg_vv_pl1),
  Value = as.numeric(corStab_sp_eg_vv_pl1) # Ensure the values are numeric
)

corStab_sp_eg_vv_pl2_df <- data.frame(
  Name = names(corStab_sp_eg_vv_pl2),
  Value = as.numeric(corStab_sp_eg_vv_pl2) # Ensure the values are numeric
)

corStab_sp_eg_vv_pl_df <- data.frame(
  Name = names(corStab_sp_eg_vv_pl),
  Value = as.numeric(corStab_sp_eg_vv_pl) # Ensure the values are numeric
)

corStab_sp_eg_vv_flpl_df <- data.frame(
  Name = names(corStab_sp_eg_vv_flpl),
  Value = as.numeric(corStab_sp_eg_vv_flpl) # Ensure the values are numeric
)

corStab_sp_eg_vv_g12_i_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g12_i),
  Value = as.numeric(corStab_sp_eg_vv_g12_i) # Ensure the values are numeric
)

corStab_sp_eg_vv_g12qt_i_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g12qt_i),
  Value = as.numeric(corStab_sp_eg_vv_g12qt_i) # Ensure the values are numeric
)
corStab_sp_eg_vv_g27_i_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g27_i),
  Value = as.numeric(corStab_sp_eg_vv_g27_i) # Ensure the values are numeric
)
corStab_sp_eg_vv_g27qt_i_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g27qt_i),
  Value = as.numeric(corStab_sp_eg_vv_g27qt_i) # Ensure the values are numeric
)
corStab_sp_eg_vv_ll70_i_df <- data.frame(
  Name = names(corStab_sp_eg_vv_ll70_i),
  Value = as.numeric(corStab_sp_eg_vv_ll70_i) # Ensure the values are numeric
)

corStab_sp_eg_vv_llsc_i_df <- data.frame(
  Name = names(corStab_sp_eg_vv_llsc_i),
  Value = as.numeric(corStab_sp_eg_vv_llsc_i) # Ensure the values are numeric
)

corStab_sp_eg_vv_g12_c_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g12_c),
  Value = as.numeric(corStab_sp_eg_vv_g12_c) # Ensure the values are numeric
)

corStab_sp_eg_vv_g12qt_c_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g12qt_c),
  Value = as.numeric(corStab_sp_eg_vv_g12qt_c) # Ensure the values are numeric
)
corStab_sp_eg_vv_g27_c_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g27_c),
  Value = as.numeric(corStab_sp_eg_vv_g27_c) # Ensure the values are numeric
)
corStab_sp_eg_vv_g27qt_c_df <- data.frame(
  Name = names(corStab_sp_eg_vv_g27qt_c),
  Value = as.numeric(corStab_sp_eg_vv_g27qt_i) # Ensure the values are numeric
)
corStab_sp_eg_vv_ll70_c_df <- data.frame(
  Name = names(corStab_sp_eg_vv_ll70_c),
  Value = as.numeric(corStab_sp_eg_vv_ll70_c) # Ensure the values are numeric
)

corStab_sp_eg_vv_llsc_c_df <- data.frame(
  Name = names(corStab_sp_eg_vv_llsc_c),
  Value = as.numeric(corStab_sp_eg_vv_llsc_c) # Ensure the values are numeric
)

corStab_sp_eg_vv_fl_df$model <- "humans" 
corStab_sp_eg_vv_pl1_df$model <- "humans" 
corStab_sp_eg_vv_pl2_df$model <- "humans" 
corStab_sp_eg_vv_pl_df$model <- "humans" 
corStab_sp_eg_vv_flpl_df$model <- "humans" 
corStab_sp_eg_vv_g12_i_df$model <- "g12"
corStab_sp_eg_vv_g12qt_i_df$model <- "g12qt"
corStab_sp_eg_vv_g27_i_df$model <- "g27"
corStab_sp_eg_vv_g27qt_i_df$model <- "g27qt"
corStab_sp_eg_vv_ll70_i_df$model <- "ll70"
corStab_sp_eg_vv_llsc_i_df$model <- "llsc"
corStab_sp_eg_vv_g12_c_df$model <- "g12"
corStab_sp_eg_vv_g12qt_c_df$model <- "g12qt"
corStab_sp_eg_vv_g27_c_df$model <- "g27"
corStab_sp_eg_vv_g27qt_c_df$model <- "g27qt"
corStab_sp_eg_vv_ll70_c_df$model <- "ll70"
corStab_sp_eg_vv_llsc_c_df$model <- "llsc"

corStab_sp_eg_vv_fl_df$task <- "vviq"
corStab_sp_eg_vv_pl1_df$task <- "vviq"
corStab_sp_eg_vv_pl2_df$task <- "vviq"
corStab_sp_eg_vv_pl_df$task <- "vviq"
corStab_sp_eg_vv_flpl_df$task <- "vviq"
corStab_sp_eg_vv_g12_i_df$task <- "vviq"
corStab_sp_eg_vv_g12qt_i_df$task <- "vviq"
corStab_sp_eg_vv_g27_i_df$task <- "vviq"
corStab_sp_eg_vv_g27qt_i_df$task <- "vviq"
corStab_sp_eg_vv_ll70_i_df$task <- "vviq"
corStab_sp_eg_vv_llsc_i_df$task <- "vviq"
corStab_sp_eg_vv_g12_c_df$task <- "vviq"
corStab_sp_eg_vv_g12qt_c_df$task <- "vviq"
corStab_sp_eg_vv_g27_c_df$task <- "vviq"
corStab_sp_eg_vv_g27qt_c_df$task <- "vviq"
corStab_sp_eg_vv_ll70_c_df$task <- "vviq"
corStab_sp_eg_vv_llsc_c_df$task <- "vviq"

corStab_sp_eg_vv_fl_df$group <- "fl"
corStab_sp_eg_vv_pl1_df$group <- "pl1"
corStab_sp_eg_vv_pl2_df$group <- "pl2"
corStab_sp_eg_vv_pl_df$group <- "pl"
corStab_sp_eg_vv_flpl_df$group <- "flpl"
corStab_sp_eg_vv_g12_i_df$group <- "independent"
corStab_sp_eg_vv_g12qt_i_df$group <- "independent"
corStab_sp_eg_vv_g27_i_df$group <- "independent"
corStab_sp_eg_vv_g27qt_i_df$group <- "independent"
corStab_sp_eg_vv_ll70_i_df$group <- "independent"
corStab_sp_eg_vv_llsc_i_df$group <- "independent"
corStab_sp_eg_vv_g12_c_df$group <- "cumulative"
corStab_sp_eg_vv_g12qt_c_df$group <- "cumulative"
corStab_sp_eg_vv_g27_c_df$group <- "cumulative"
corStab_sp_eg_vv_g27qt_c_df$group <- "cumulative"
corStab_sp_eg_vv_ll70_c_df$group <- "cumulative"
corStab_sp_eg_vv_llsc_c_df$group <- "cumulative"

sp_eg_cor_stab_vviq <- bind_rows(corStab_sp_eg_vv_fl_df,
corStab_sp_eg_vv_pl1_df,
corStab_sp_eg_vv_pl2_df,
corStab_sp_eg_vv_pl_df,
corStab_sp_eg_vv_flpl_df,
corStab_sp_eg_vv_g12_i_df,
corStab_sp_eg_vv_g12qt_i_df,
corStab_sp_eg_vv_g27_i_df,
corStab_sp_eg_vv_g27qt_i_df,
corStab_sp_eg_vv_ll70_i_df,
corStab_sp_eg_vv_llsc_i_df,
corStab_sp_eg_vv_g12_c_df,
corStab_sp_eg_vv_g12qt_c_df,
corStab_sp_eg_vv_g27_c_df,
corStab_sp_eg_vv_g27qt_c_df,
corStab_sp_eg_vv_ll70_c_df,
corStab_sp_eg_vv_llsc_c_df)
write_csv(sp_eg_cor_stab_vviq,"data/processed/sp_eg_cor_stab_vviq.csv")

corStab_sp_eg_ps_fl_df <- data.frame(
  Name = names(corStab_sp_eg_ps_fl),
  Value = as.numeric(corStab_sp_eg_ps_fl) # Ensure the values are numeric
)

corStab_sp_eg_ps_uk_df <- data.frame(
  Name = names(corStab_sp_eg_ps_uk),
  Value = as.numeric(corStab_sp_eg_ps_uk) # Ensure the values are numeric
)

corStab_sp_eg_ps_ukfl_df <- data.frame(
  Name = names(corStab_sp_eg_ps_ukfl),
  Value = as.numeric(corStab_sp_eg_ps_ukfl) # Ensure the values are numeric
)

corStab_sp_eg_ps_g12_i_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g12_i),
  Value = as.numeric(corStab_sp_eg_ps_g12_i) # Ensure the values are numeric
)

corStab_sp_eg_ps_g12qt_i_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g12qt_i),
  Value = as.numeric(corStab_sp_eg_ps_g12qt_i) # Ensure the values are numeric
)
corStab_sp_eg_ps_g27_i_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g27_i),
  Value = as.numeric(corStab_sp_eg_ps_g27_i) # Ensure the values are numeric
)
corStab_sp_eg_ps_g27qt_i_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g27qt_i),
  Value = as.numeric(corStab_sp_eg_ps_g27qt_i) # Ensure the values are numeric
)
corStab_sp_eg_ps_ll70_i_df <- data.frame(
  Name = names(corStab_sp_eg_ps_ll70_i),
  Value = as.numeric(corStab_sp_eg_ps_ll70_i) # Ensure the values are numeric
)

corStab_sp_eg_ps_llsc_i_df <- data.frame(
  Name = names(corStab_sp_eg_ps_llsc_i),
  Value = as.numeric(corStab_sp_eg_ps_llsc_i) # Ensure the values are numeric
)

corStab_sp_eg_ps_g12_c_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g12_c),
  Value = as.numeric(corStab_sp_eg_ps_g12_c) # Ensure the values are numeric
)

corStab_sp_eg_ps_g12qt_c_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g12qt_c),
  Value = as.numeric(corStab_sp_eg_ps_g12qt_c) # Ensure the values are numeric
)
corStab_sp_eg_ps_g27_c_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g27_c),
  Value = as.numeric(corStab_sp_eg_ps_g27_c) # Ensure the values are numeric
)
corStab_sp_eg_ps_g27qt_c_df <- data.frame(
  Name = names(corStab_sp_eg_ps_g27qt_c),
  Value = as.numeric(corStab_sp_eg_ps_g27qt_c) # Ensure the values are numeric
)
corStab_sp_eg_ps_ll70_c_df <- data.frame(
  Name = names(corStab_sp_eg_ps_ll70_c),
  Value = as.numeric(corStab_sp_eg_ps_ll70_c) # Ensure the values are numeric
)

corStab_sp_eg_ps_llsc_c_df <- data.frame(
  Name = names(corStab_sp_eg_ps_llsc_c),
  Value = as.numeric(corStab_sp_eg_ps_llsc_c) # Ensure the values are numeric
)

corStab_sp_eg_ps_fl_df$model <- "human"
corStab_sp_eg_ps_uk_df$model <- "human"
corStab_sp_eg_ps_ukfl_df$model <- "human"
corStab_sp_eg_ps_g12_i_df$model <- "g12"
corStab_sp_eg_ps_g12qt_i_df$model <- "g12qt"
corStab_sp_eg_ps_g27_i_df$model <- "g27"
corStab_sp_eg_ps_g27qt_i_df$model <- "g27qt"
corStab_sp_eg_ps_ll70_i_df$model <- "ll70"
corStab_sp_eg_ps_llsc_i_df$model <- "llsc"
corStab_sp_eg_ps_g12_c_df$model <- "g12"
corStab_sp_eg_ps_g12qt_c_df$model <- "g12qt"
corStab_sp_eg_ps_g27_c_df$model <- "g27"
corStab_sp_eg_ps_g27qt_c_df$model <- "g27qt"
corStab_sp_eg_ps_ll70_c_df$model <- "ll70"
corStab_sp_eg_ps_llsc_c_df$model <- "llsc"


corStab_sp_eg_ps_fl_df$task <- "psiq"
corStab_sp_eg_ps_uk_df$task <- "psiq"
corStab_sp_eg_ps_ukfl_df$task <- "psiq"
corStab_sp_eg_ps_g12_i_df$task <- "psiq"
corStab_sp_eg_ps_g12qt_i_df$task <- "psiq"
corStab_sp_eg_ps_g27_i_df$task <- "psiq"
corStab_sp_eg_ps_g27qt_i_df$task <- "psiq"
corStab_sp_eg_ps_ll70_i_df$task <- "psiq"
corStab_sp_eg_ps_llsc_i_df$task <- "psiq"
corStab_sp_eg_ps_g12_c_df$task <- "psiq"
corStab_sp_eg_ps_g12qt_c_df$task <- "psiq"
corStab_sp_eg_ps_g27_c_df$task <- "psiq"
corStab_sp_eg_ps_g27qt_c_df$task <- "psiq"
corStab_sp_eg_ps_ll70_c_df$task <- "psiq"
corStab_sp_eg_ps_llsc_c_df$task <- "psiq"


corStab_sp_eg_ps_fl_df$group <- "fl"
corStab_sp_eg_ps_uk_df$group <- "uk"
corStab_sp_eg_ps_ukfl_df$group <- "ukfl"
corStab_sp_eg_ps_g12_i_df$group <- "independent"
corStab_sp_eg_ps_g12qt_i_df$group <- "independent"
corStab_sp_eg_ps_g27_i_df$group <- "independent"
corStab_sp_eg_ps_g27qt_i_df$group <- "independent"
corStab_sp_eg_ps_ll70_i_df$group <- "independent"
corStab_sp_eg_ps_llsc_i_df$group <- "independent"
corStab_sp_eg_ps_g12_c_df$group <- "cumulative"
corStab_sp_eg_ps_g12qt_c_df$group <- "cumulative"
corStab_sp_eg_ps_g27_c_df$group <- "cumulative"
corStab_sp_eg_ps_g27qt_c_df$group <- "cumulative"
corStab_sp_eg_ps_ll70_c_df$group <- "cumulative"
corStab_sp_eg_ps_llsc_c_df$group <- "cumulative"

sp_eg_cor_stab_psiq <- bind_rows(corStab_sp_eg_ps_fl_df,
corStab_sp_eg_ps_uk_df,
corStab_sp_eg_ps_ukfl_df,
corStab_sp_eg_ps_g12_i_df,
corStab_sp_eg_ps_g12qt_i_df,
corStab_sp_eg_ps_g27_i_df,
corStab_sp_eg_ps_g27qt_i_df,
corStab_sp_eg_ps_ll70_i_df,
corStab_sp_eg_ps_llsc_i_df,
corStab_sp_eg_ps_g12_c_df,
corStab_sp_eg_ps_g12qt_c_df,
corStab_sp_eg_ps_g27_c_df,
corStab_sp_eg_ps_g27qt_c_df,
corStab_sp_eg_ps_ll70_c_df,
corStab_sp_eg_ps_llsc_c_df)
write_csv(sp_eg_cor_stab_psiq,"data/processed/sp_eg_cor_stab_psiq.csv")

