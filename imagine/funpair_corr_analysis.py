import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg
from pathlib import Path
from scipy.stats import shapiro, zscore, levene


def pvalues_to_annotation_matrix(
    pg_df,
    corr_df,
    p_unc_col="p-unc",
    p_corr_col="p-corr",
    unc_rules=None,
    corr_rules=None,
    plus_symbol="+",
    star_symbol="*",
    show_numbers=True,
    number_fmt="{:.2f}",
):
    """
    Build an annotation matrix that uses APA-style repeated symbols to indicate p-value ranges.

    - For corrected p-values (pv_corr) the helper will map thresholds to star strings (e.g. '*','**','***').
    - For uncorrected p-values (pv_unc) the helper will map thresholds to plus strings (e.g. '+','++','+++').

    Rules are lists of (threshold, symbol_string) ordered from smallest p to largest. The first rule
    matched (p < threshold) is used.

    Returns: (annot_df, pv_unc, pv_corr)
    """
    # default rules (APA-like for stars; plus mirrors these for uncorrected)
    if corr_rules is None:
        corr_rules = [(0.001, star_symbol * 3), (0.01, star_symbol * 2), (0.05, star_symbol)]
    if unc_rules is None:
        unc_rules = [(0.001, plus_symbol * 3), (0.01, plus_symbol * 2), (0.05, plus_symbol)]

    # detect pair column names
    if "X" in pg_df.columns and "Y" in pg_df.columns:
        xcol, ycol = "X", "Y"
    else:
        cand = [c for c in pg_df.columns if pg_df[c].dtype == object]
        if len(cand) < 2:
            raise ValueError("Couldn't detect pair columns in pg_df")
        xcol, ycol = cand[0], cand[1]

    # build uncorrected p matrix
    if p_unc_col in pg_df.columns:
        pv_unc = pg_df.pivot(index=xcol, columns=ycol, values=p_unc_col)
        pv_unc = pv_unc.reindex(index=corr_df.index, columns=corr_df.columns)
        pv_unc = pv_unc.combine_first(pv_unc.T)
    else:
        pv_unc = pd.DataFrame(np.nan, index=corr_df.index, columns=corr_df.columns)

    # build corrected p matrix
    if p_corr_col in pg_df.columns:
        pv_corr = pg_df.pivot(index=xcol, columns=ycol, values=p_corr_col)
        pv_corr = pv_corr.reindex(index=corr_df.index, columns=corr_df.columns)
        pv_corr = pv_corr.combine_first(pv_corr.T)
    else:
        pv_corr = pd.DataFrame(np.nan, index=corr_df.index, columns=corr_df.columns)

    # helper to map p to a symbol string using rule list
    def map_rules(p, rules):
        if pd.isna(p):
            return ""
        for thr, sym in rules:
            if p < thr:
                return sym
        return ""

    # build annotation df: corrected stars override uncorrected pluses
    annot = pd.DataFrame("", index=corr_df.index, columns=corr_df.columns, dtype=object)
    for i in corr_df.index:
        for j in corr_df.columns:
            pcorr = pv_corr.loc[i, j] if (i in pv_corr.index and j in pv_corr.columns) else np.nan
            pup = pv_unc.loc[i, j] if (i in pv_unc.index and j in pv_unc.columns) else np.nan
            sym = ""
            # first check corrected p rules
            s_corr = map_rules(pcorr, corr_rules)
            if s_corr:
                sym = s_corr
            else:
                s_unc = map_rules(pup, unc_rules)
                if s_unc:
                    sym = s_unc
            annot.loc[i, j] = sym

    if show_numbers:
        combined = pd.DataFrame(index=corr_df.index, columns=corr_df.columns, dtype=object)
        for i in corr_df.index:
            for j in corr_df.columns:
                n = "" if pd.isna(corr_df.loc[i, j]) else number_fmt.format(corr_df.loc[i, j])
                s = annot.loc[i, j]
                if s and n:
                    combined.loc[i, j] = f"{n}\n{s}"
                elif s:
                    combined.loc[i, j] = s
                else:
                    combined.loc[i, j] = n
        return combined, pv_unc, pv_corr
    else:
        return annot, pv_unc, pv_corr


def build_pvalue_matrices(pg_df, corr_df, p_unc_col="p-unc", p_corr_col="p-corr"):
    """Return (pv_unc, pv_corr) aligned with corr_df index/columns.

    pg_df: pingouin pairwise_corr output (long-form)
    corr_df: square correlation matrix (index/columns order)
    """
    # detect pair column names
    if "X" in pg_df.columns and "Y" in pg_df.columns:
        xcol, ycol = "X", "Y"
    else:
        cand = [c for c in pg_df.columns if pg_df[c].dtype == object]
        if len(cand) < 2:
            raise ValueError("Couldn't detect pair columns in pg_df")
        xcol, ycol = cand[0], cand[1]

    def build(col):
        if col in pg_df.columns:
            m = pg_df.pivot(index=xcol, columns=ycol, values=col)
            m = m.reindex(index=corr_df.index, columns=corr_df.columns)
            m = m.combine_first(m.T)
        else:
            m = pd.DataFrame(np.nan, index=corr_df.index, columns=corr_df.columns)
        return m

    pv_unc = build(p_unc_col)
    pv_corr = build(p_corr_col)
    return pv_unc, pv_corr


def compute_annotation(
    pg_df,
    corr_df,
    p_unc_col="p-unc",
    p_corr_col="p-corr",
    unc_rules=None,
    corr_rules=None,
    plus_symbol="+",
    star_symbol="*",
    show_numbers=False,
):
    """Wrapper that returns (annot_df, pv_unc, pv_corr) using pvalues_to_annotation_matrix if present,
    otherwise builds a simple one.
    """
    # reuse notebook's pvalues_to_annotation_matrix if available
    if "pvalues_to_annotation_matrix" in globals():
        return pvalues_to_annotation_matrix(
            pg_df,
            corr_df,
            p_unc_col=p_unc_col,
            p_corr_col=p_corr_col,
            unc_rules=unc_rules,
            corr_rules=corr_rules,
            plus_symbol=plus_symbol,
            star_symbol=star_symbol,
            show_numbers=show_numbers,
        )
    # fallback: simple mapping
    pv_unc, pv_corr = build_pvalue_matrices(pg_df, corr_df, p_unc_col, p_corr_col)
    annot = pd.DataFrame("", index=corr_df.index, columns=corr_df.columns, dtype=object)
    if corr_rules is None:
        corr_rules = [(0.001, star_symbol * 3), (0.01, star_symbol * 2), (0.05, star_symbol)]
    if unc_rules is None:
        unc_rules = [(0.001, plus_symbol * 3), (0.01, plus_symbol * 2), (0.05, plus_symbol)]

    def map_rules(p, rules):
        if pd.isna(p):
            return ""
        for thr, sym in rules:
            if p < thr:
                return sym
        return ""

    for i in corr_df.index:
        for j in corr_df.columns:
            pc = pv_corr.loc[i, j] if (i in pv_corr.index and j in pv_corr.columns) else np.nan
            pu = pv_unc.loc[i, j] if (i in pv_unc.index and j in pv_unc.columns) else np.nan
            s = map_rules(pc, corr_rules)
            if not s:
                s = map_rules(pu, unc_rules)
            annot.loc[i, j] = s

    return annot, pv_unc, pv_corr


def plot_heatmap_with_caption(
    corr_df,
    annot_df,
    title,
    outpath: Path,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    annot_kws=None,
    label_map: dict = None,
    font_family: str = "Palatino",
):
    """Plot seaborn heatmap with annotation DataFrame (strings) and save to outpath.

    Counts plus/star cells and writes a small caption under the figure.
    """
    if annot_kws is None:
        annot_kws = {"fontsize": 18, "color": "black"} #"color": "black"
    # Use the requested font family for this figure via an rc context so it does not
    # affect global matplotlib state outside this function. Set serif family so
    # specifying a Palatino serif works on systems with that font installed.
    rc = {"font.family": "serif", "font.serif": [font_family]}
    with plt.rc_context(rc):
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(
            corr_df,
            annot=annot_df.values,
            fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax,
        )

        # apply custom label mapping if provided
        if label_map is not None:
            try:
                xlabels = [label_map.get(x, x) for x in corr_df.columns]
                ylabels = [label_map.get(y, y) for y in corr_df.index]
                ax.set_xticklabels(xlabels, rotation=90)
                ax.set_yticklabels(ylabels, rotation=0)
            except Exception:
                # fallback: ignore label_map failures
                pass

        n_plus = annot_df.applymap(lambda s: isinstance(s, str) and s.startswith("+")).sum().sum()
        n_star = annot_df.applymap(lambda s: isinstance(s, str) and s.startswith("*")).sum().sum()
        # caption = f"+ = {int(n_plus)} (uncorrected p < .05); * = {int(n_star)} (corrected p < .05)"
        ax.set_title(title)
        # plt.figtext(0.5, -0.02, caption, ha="center", fontsize=9)
        outpath.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(outpath, bbox_inches="tight", dpi=300)
        print("----xxxx----",outpath)
        plt.show()
        plt.close()

    return {"n_plus": int(n_plus), "n_star": int(n_star), "path": outpath}


def analyze_measure(
    df_all,
    measure,
    groups,
    title_str,
    fig_out_dir,
    padjust="fdr_bh",
    corr_method="pearson",
    label_map: dict = None,
    font_family: str = "Palatino",
    hypothesis: str = "two-sided",
):
    """High-level helper to compute correlation matrix, pairwise p-values, annotation, and plot for a measure.

    Returns a dict with correlation matrix, pg pairwise df, pv matrices, annot df, and counts.
    """
    dfm = df_all.loc[df_all["measure"] == measure]
    pivot = dfm.pivot_table(index="node", columns="groupmodel", values="value")
    pivot = pivot.reindex(columns=groups)
    corr = pivot.corr()
    # use `alternative`/`hypothesis` argument from pingouin to select two-sided/greater/less
    pg_df = pg.pairwise_corr(pivot, method=corr_method, padjust=padjust, alternative=hypothesis)
    annot, pv_unc, pv_corr = compute_annotation(pg_df, corr, show_numbers=False)
    fname = (
        fig_out_dir
        / f"{title_str}_{('vv_' if 'vv_' in str(fig_out_dir) else '')}{measure.replace(' ', '_').lower()}_annot.svg"
    )
    print("--xx--",fname)

    title = f"{measure} (significance markers only)"

    counts = plot_heatmap_with_caption(
        corr, annot, title, fname, label_map=label_map, font_family=font_family
    )
    return {
        "pivot": pivot,
        "corr": corr,
        "pg_df": pg_df,
        "pv_unc": pv_unc,
        "pv_corr": pv_corr,
        "annot": annot,
        "counts": counts,
    }


# Assumption checks for Pearson and Spearman alternative (refactored to reuse pivots from plot results)
# This section computes Shapiro normality, outlier counts, a simple Levene homoscedasticity check,
# and the Spearman correlations (with FDR correction) for every pair of group-model columns
# for each centrality measure and dataset (VVIQ / PSIQ). Results are saved to CSV files.


def check_pearson_assumptions(x, y, alpha=0.05):
    """Return a dict of simple assumption checks for Pearson correlation between two 1-D arrays.

    Returns keys:
      - shapiro_x_p, shapiro_y_p: p-values
      - normal_x / normal_y: True if do not reject normality (p >= alpha)
      - n_outliers_x / n_outliers_y: counts of |z|>3
      - levene_p: p-value from Levene test (NaN when insufficient data)
      - *_violation booleans and 'violations' (comma-separated list)
      - recommended_method: 'pearson' or 'spearman' based on simple heuristics
    """
    x = np.asarray(x)
    y = np.asarray(y)
    res = {}

    # Shapiro (requires n>=3)
    try:
        if len(x) >= 3:
            res["shapiro_x_p"] = float(shapiro(x).pvalue)
            res["normal_x"] = res["shapiro_x_p"] >= alpha
        else:
            res["shapiro_x_p"] = np.nan
            res["normal_x"] = False
    except Exception:
        res["shapiro_x_p"] = np.nan
        res["normal_x"] = False

    try:
        if len(y) >= 3:
            res["shapiro_y_p"] = float(shapiro(y).pvalue)
            res["normal_y"] = res["shapiro_y_p"] >= alpha
        else:
            res["shapiro_y_p"] = np.nan
            res["normal_y"] = False
    except Exception:
        res["shapiro_y_p"] = np.nan
        res["normal_y"] = False

    # outliers via z-score
    try:
        zx = np.abs(zscore(x, nan_policy="omit"))
        res["n_outliers_x"] = int(np.sum(zx > 3))
    except Exception:
        res["n_outliers_x"] = 0
    try:
        zy = np.abs(zscore(y, nan_policy="omit"))
        res["n_outliers_y"] = int(np.sum(zy > 3))
    except Exception:
        res["n_outliers_y"] = 0

    # Levene: compare variance of y for low/high x split (median)
    try:
        med = np.nanmedian(x)
        g1 = y[x <= med]
        g2 = y[x > med]
        if len(g1) >= 2 and len(g2) >= 2:
            res["levene_p"] = float(levene(g1, g2).pvalue)
        else:
            res["levene_p"] = np.nan
    except Exception:
        res["levene_p"] = np.nan

    # violation flags
    res["normal_x_violation"] = not bool(res.get("normal_x", False))
    res["normal_y_violation"] = not bool(res.get("normal_y", False))
    res["outliers_x_violation"] = bool(res.get("n_outliers_x", 0) > 0)
    res["outliers_y_violation"] = bool(res.get("n_outliers_y", 0) > 0)
    res["levene_violation"] = False
    if not np.isnan(res.get("levene_p", np.nan)):
        res["levene_violation"] = res["levene_p"] < 0.05

    # collect textual violations
    violations = []
    if res["normal_x_violation"]:
        violations.append("normality_x")
    if res["normal_y_violation"]:
        violations.append("normality_y")
    if res["outliers_x_violation"]:
        violations.append("outliers_x")
    if res["outliers_y_violation"]:
        violations.append("outliers_y")
    if res["levene_violation"]:
        violations.append("heteroscedasticity")
    res["violations"] = ",".join(violations) if violations else ""

    # recommendation heuristic
    ok_normal = bool(res.get("normal_x", False) and res.get("normal_y", False))
    ok_outliers = res.get("n_outliers_x", 0) == 0 and res.get("n_outliers_y", 0) == 0
    lev_ok = np.isnan(res.get("levene_p")) or res.get("levene_p") >= 0.05
    res["recommended_method"] = "pearson" if (ok_normal and ok_outliers and lev_ok) else "spearman"

    return res


def analyze_centrality_assumptions_from_results(plot_results, label_prefix):
    """Compute Pearson and Spearman pairwise correlations + assumption checks for each column pair
    using pivot tables already present in plot_results (output of analyze_measure).

    Returns a dict mapping measure -> DataFrame.
    """
    # Deprecated compatibility wrapper kept for backwards-compatibility.
    return analyze_centrality_assumptions(plot_results, label_prefix)


def analyze_pairwise_assumptions(pivots, label_prefix, out_dir=None, padjust="fdr_bh", alternative="two-sided", hypothesis: str = None):
    """Compute Pearson and Spearman pairwise correlations + assumption checks for each column pair.

    General-purpose function for pairwise data. Accepts either:
      - a mapping (dict-like) of name -> result-dict (where result['pivot'] is a DataFrame),
      - or a mapping of name -> pivot DataFrame,
      - or a single pivot DataFrame (in which case the returned dict will use the provided label_prefix as name).

    Parameters
    - pivots: dict or DataFrame
    - label_prefix: str used for filenames
    - out_dir: Path-like directory where CSVs will be written (defaults to global data_dir if present)
    - padjust: pingouin padjust method
    - alternative: pingouin alternative argument for pairwise_corr

    Returns a dict mapping name -> DataFrame of results.
    """
    if out_dir is None:
        out_dir = globals().get("data_dir", Path("."))
    else:
        out_dir = Path(out_dir)

    # Normalize input to an iterable of (measure_name, pivot)
    items = []
    if isinstance(pivots, pd.DataFrame):
        items = [(label_prefix, pivots)]
    elif isinstance(pivots, dict):
        # allow dict of {measure: result_dict} where result_dict may contain 'pivot', or dict of {measure: pivot}
        for k, v in pivots.items():
            if isinstance(v, dict) and "pivot" in v:
                items.append((k, v["pivot"]))
            elif isinstance(v, pd.DataFrame):
                items.append((k, v))
            else:
                raise TypeError(f"Unsupported pivot entry for key {k}: expected DataFrame or dict with 'pivot'.")
    else:
        raise TypeError("pivots must be a DataFrame or a dict mapping measure->pivot/result-dict")

    outd = {}
    for name, pivot in items:
        # resolve hypothesis/alternative: function supports 'two-sided','greater','less'
        alt = hypothesis if hypothesis is not None else alternative
        # compute pairwise stats
        pear = pg.pairwise_corr(pivot, method="pearson", padjust=padjust, alternative=alt)
        spear = pg.pairwise_corr(pivot, method="spearman", padjust=padjust, alternative=alt)
        rows = []
        for _, row in pear.iterrows():
            xcol = row["X"]
            ycol = row["Y"]
            r = row.get("r", np.nan)
            p_unc = row.get("p-unc", np.nan)
            p_corr = row.get("p-corr", np.nan)
            srow = spear.loc[(spear["X"] == xcol) & (spear["Y"] == ycol)]
            if not srow.empty:
                rho = float(srow.iloc[0].get("r", np.nan))
                s_punc = float(srow.iloc[0].get("p-unc", np.nan))
                s_pcorr = float(srow.iloc[0].get("p-corr", np.nan))
            else:
                rho = np.nan
                s_punc = np.nan
                s_pcorr = np.nan
            sx = pivot[xcol].values
            sy = pivot[ycol].values
            asum = check_pearson_assumptions(sx, sy)
            rows.append(
                {
                    "X": xcol,
                    "Y": ycol,
                    "pearson_r": r,
                    "pearson_p_unc": p_unc,
                    "pearson_p_corr": p_corr,
                    "spearman_rho": rho,
                    "spearman_p_unc": s_punc,
                    "spearman_p_corr": s_pcorr,
                    "shapiro_x_p": asum["shapiro_x_p"],
                    "shapiro_y_p": asum["shapiro_y_p"],
                    "normal_x": asum["normal_x"],
                    "normal_y": asum["normal_y"],
                    "normal_x_violation": asum["normal_x_violation"],
                    "normal_y_violation": asum["normal_y_violation"],
                    "n_outliers_x": asum["n_outliers_x"],
                    "n_outliers_y": asum["n_outliers_y"],
                    "outliers_x_violation": asum["outliers_x_violation"],
                    "outliers_y_violation": asum["outliers_y_violation"],
                    "levene_p": asum["levene_p"],
                    "levene_violation": asum["levene_violation"],
                    "violations": asum["violations"],
                    "recommended_method": asum["recommended_method"],
                }
            )
        out = pd.DataFrame(rows)
        # file name uses the provided name (was 'measure' in earlier API)
        fname = out_dir / f"assumption_checks_{label_prefix}_{name.replace(' ', '_').lower()}.csv"
        out.to_csv(fname, index=False)
        print(f"Saved assumption check + spearman results to: {fname}")
        outd[name] = out
    return outd


# Backwards-compatible alias for previous function name
analyze_centrality_assumptions = analyze_pairwise_assumptions


def plot_centrality_comparison(
    measure,
    vv_result,
    ps_result,
    outpath: Path,
    label_map: dict = None,
    font_family: str = "Palatino",
    cmap: str = "coolwarm",
    vmin: float = -1,
    vmax: float = 1,
    annot_kws: dict = None,
):
    """Plot a side-by-side comparison (VVIQ left, PSIQ right) of correlation heatmaps for a measure.

    Parameters
    - measure: name of the centrality measure (used for titles if not provided)
    - vv_result: either a result-dict (with keys 'corr' and 'annot') or a tuple (corr_df, annot_df)
    - ps_result: same as vv_result but for PSIQ
    - outpath: Path to save the combined figure (SVG/PNG)
    - label_map: optional dict mapping original labels to display labels
    - font_family: font family to use for tick labels and titles
    - cmap, vmin, vmax, annot_kws: plotting options forwarded to seaborn heatmap

    Returns: dict with keys 'path' and per-panel counts like {'vv': {...}, 'ps': {...}}
    """
    # normalize inputs to (corr_df, annot_df)
    def _unpack(res):
        if isinstance(res, dict):
            if "corr" in res and "annot" in res:
                return res["corr"], res["annot"]
            # accept result-dict that contains pivot -> compute corr/annot? not supported here
            raise TypeError("result dict must contain 'corr' and 'annot' keys")
        elif isinstance(res, (list, tuple)) and len(res) >= 2:
            return res[0], res[1]
        else:
            raise TypeError("vv_result/ps_result must be result-dict or (corr_df, annot_df) tuple")

    vv_corr, vv_annot = _unpack(vv_result)
    ps_corr, ps_annot = _unpack(ps_result)

    if annot_kws is None:
        annot_kws = {"fontsize": 18, "color": "black"} # "color": "black"

    # ensure output dir
    outpath.parent.mkdir(parents=True, exist_ok=True)

    # create the figure with shared colorbar
    rc = {"font.family": "serif", "font.serif": [font_family]}
    with plt.rc_context(rc):
        fig, axes = plt.subplots(1, 2, figsize=(16, 7), squeeze=False)
        ax_l = axes[0, 0]
        ax_r = axes[0, 1]

        sns.heatmap(
            vv_corr,
            annot=vv_annot.values,
            fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax_l,
            cbar=False,
        )
        sns.heatmap(
            ps_corr,
            annot=ps_annot.values,
            fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax_r,
            cbar=True,
            cbar_kws={"shrink": 0.7},
        )

        # apply label_map if provided
        if label_map is not None:
            try:
                ax_l.set_xticklabels([label_map.get(x, x) for x in vv_corr.columns], rotation=90)
                ax_l.set_yticklabels([label_map.get(y, y) for y in vv_corr.index], rotation=0)
                ax_r.set_xticklabels([label_map.get(x, x) for x in ps_corr.columns], rotation=90)
                ax_r.set_yticklabels([label_map.get(y, y) for y in ps_corr.index], rotation=0)
            except Exception:
                pass

        left_title = f"VVIQ — {measure}"
        right_title = f"PSIQ — {measure}"
        ax_l.set_title(left_title)
        ax_r.set_title(right_title)

        plt.tight_layout()
        plt.savefig(outpath, bbox_inches="tight", dpi=300)
        plt.show()
        plt.close()

    # compute counts for annotation symbols (same logic as plot_heatmap_with_caption)
    n_plus_vv = vv_annot.applymap(lambda s: isinstance(s, str) and s.startswith("+")).sum().sum()
    n_star_vv = vv_annot.applymap(lambda s: isinstance(s, str) and s.startswith("*")).sum().sum()
    n_plus_ps = ps_annot.applymap(lambda s: isinstance(s, str) and s.startswith("+")).sum().sum()
    n_star_ps = ps_annot.applymap(lambda s: isinstance(s, str) and s.startswith("*")).sum().sum()

    return {
        "path": outpath,
        "vv": {"n_plus": int(n_plus_vv), "n_star": int(n_star_vv)},
        "ps": {"n_plus": int(n_plus_ps), "n_star": int(n_star_ps)},
    }


def plot_2x2_grid_comparison(
    measures,
    vv_results,
    ps_results,
    outpath: Path,
    label_map: dict = None,
    font_family: str = "Palatino",
    cmap: str = "coolwarm",
    vmin: float = -1,
    vmax: float = 1,
    annot_kws: dict = None,
):
    """Create a 2x2 grid of heatmaps (rows = dataset [VVIQ, PSIQ], columns = two measures).

    Parameters
    - measures: iterable/list/tuple of exactly two measure names [m1, m2]
    - vv_results: dict-like mapping measure -> result-dict (with 'corr' and 'annot') or pivot
    - ps_results: same as vv_results but for PSIQ
    - outpath: Path to save the figure
    - label_map, font_family, cmap, vmin, vmax, annot_kws: plotting options

    Returns: dict with 'path' and per-panel annotation counts.
    """
    if len(measures) != 2:
        raise ValueError("measures must be a sequence of two measure names")
    m1, m2 = measures

    def _unpack_from_results(results, m):
        # accept dict of {measure: result-dict} where result-dict contains 'corr' and 'annot',
        # or accepts a pivot DataFrame directly under results[m].
        if isinstance(results, dict) and m in results:
            val = results[m]
            if isinstance(val, dict):
                if "corr" in val and "annot" in val:
                    return val["corr"], val["annot"]
                if "pivot" in val:
                    pivot = val["pivot"]
                    corr = pivot.corr()
                    pg_df = pg.pairwise_corr(pivot, method="pearson", padjust="fdr_bh")
                    annot, pv_unc, pv_corr = compute_annotation(pg_df, corr, show_numbers=False)
                    return corr, annot
            elif isinstance(val, pd.DataFrame):
                pivot = val
                corr = pivot.corr()
                pg_df = pg.pairwise_corr(pivot, method="pearson", padjust="fdr_bh")
                annot, pv_unc, pv_corr = compute_annotation(pg_df, corr, show_numbers=False)
                return corr, annot
        raise KeyError(f"Couldn't locate measure '{m}' in provided results")

    vv_corr1, vv_annot1 = _unpack_from_results(vv_results, m1)
    vv_corr2, vv_annot2 = _unpack_from_results(vv_results, m2)
    ps_corr1, ps_annot1 = _unpack_from_results(ps_results, m1)
    ps_corr2, ps_annot2 = _unpack_from_results(ps_results, m2)

    if annot_kws is None:
        annot_kws = {"fontsize": 18, "color": "black"} #

    import matplotlib as mpl
    rc = {"font.family": "serif", "font.serif": [font_family]}
    with plt.rc_context(rc):
        fig, axes = plt.subplots(2, 2, figsize=(14, 12))
        ax00 = axes[0, 0]
        ax01 = axes[0, 1]
        ax10 = axes[1, 0]
        ax11 = axes[1, 1]

        sns.heatmap(
            vv_corr1,
            annot=vv_annot1.values,
            #fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax00,
            cbar=False,
        )
        sns.heatmap(
            vv_corr2,
            annot=vv_annot2.values,
            #fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax01,
            cbar=False,
        )
        sns.heatmap(
            ps_corr1,
            annot=ps_annot1.values,
            #fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax10,
            cbar=False,
        )
        sns.heatmap(
            ps_corr2,
            annot=ps_annot2.values,
            #fmt="",
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot_kws=annot_kws,
            ax=ax11,
            cbar=False,
        )

        # apply label_map if provided
        try:
            for ax, corr in [(ax00, vv_corr1), (ax01, vv_corr2), (ax10, ps_corr1), (ax11, ps_corr2)]:
                if label_map is not None:
                    ax.set_xticklabels([label_map.get(x, x) for x in corr.columns], rotation=90)
                    ax.set_yticklabels([label_map.get(y, y) for y in corr.index], rotation=0)
        except Exception:
            pass

        ax00.set_title(f"VVIQ — {m1}")
        ax01.set_title(f"VVIQ — {m2}")
        ax10.set_title(f"PSIQ — {m1}")
        ax11.set_title(f"PSIQ — {m2}")

        # shared colorbar
        mappable = mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(vmin=vmin, vmax=vmax), cmap=cmap)
        mappable.set_array([])
        fig.colorbar(mappable, ax=[ax00, ax01, ax10, ax11], shrink=0.75)

        plt.tight_layout()
        outpath.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(outpath, bbox_inches="tight", dpi=300)
        plt.show()
        plt.close()

    # compute annotation counts
    def _counts(annot_df):
        n_plus = int(annot_df.applymap(lambda s: isinstance(s, str) and s.startswith("+")).sum().sum())
        n_star = int(annot_df.applymap(lambda s: isinstance(s, str) and s.startswith("*")).sum().sum())
        return {"n_plus": n_plus, "n_star": n_star}

    counts = {
        f"vv_{m1}": _counts(vv_annot1),
        f"vv_{m2}": _counts(vv_annot2),
        f"ps_{m1}": _counts(ps_annot1),
        f"ps_{m2}": _counts(ps_annot2),
    }

    return {"path": outpath, "counts": counts}


# Shapiro-Wilk normality tests per column and pairwise summary
# This cell computes Shapiro-Wilk for each `groupmodel` column in each centrality pivot
# and produces per-column and per-pair DataFrames. Pairwise results attach both columns' Shapiro stats.

from scipy.stats import shapiro
import itertools

def shapiro_per_column(df_pivot):
    """Run Shapiro-Wilk on each column of df_pivot. Returns DataFrame with stat, p, n, normal(boolean)."""
    rows = []
    for col in df_pivot.columns:
        series = df_pivot[col].dropna().values
        n = len(series)
        if n >= 3:
            try:
                stat, p = shapiro(series)
            except Exception:
                stat, p = (np.nan, np.nan)
        else:
            stat, p = (np.nan, np.nan)
        rows.append(
            {
                "column": col,
                "n": n,
                "shapiro_stat": float(stat) if not np.isnan(stat) else np.nan,
                "shapiro_p": float(p) if not np.isnan(p) else np.nan,
                "normal": bool(p >= 0.05) if (not np.isnan(p)) else False,
            }
        )
    return pd.DataFrame(rows)


def shapiro_pairwise_table(df_pivot, sh_df):
    """Create a pairwise table where for each pair (X,Y) we attach Shapiro results for X and Y."""
    cols = list(df_pivot.columns)
    rows = []
    for a, b in itertools.combinations(cols, 2):
        ra = sh_df.loc[sh_df["column"] == a].iloc[0].to_dict()
        rb = sh_df.loc[sh_df["column"] == b].iloc[0].to_dict()
        rows.append(
            {
                "X": a,
                "Y": b,
                "shapiro_x_p": ra["shapiro_p"],
                "shapiro_x_stat": ra["shapiro_stat"],
                "n_x": int(ra["n"]),
                "normal_x": ra["normal"],
                "shapiro_y_p": rb["shapiro_p"],
                "shapiro_y_stat": rb["shapiro_stat"],
                "n_y": int(rb["n"]),
                "normal_y": rb["normal"],
            }
        )
    return pd.DataFrame(rows)
