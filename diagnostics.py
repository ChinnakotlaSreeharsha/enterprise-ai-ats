# ======================================================
# DIAGNOSTICS MODULE — Full warm light palette
# ======================================================

import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

_BG   = "#fdfcf7"
_PLOT = "#f8f6f1"
_GRID = "rgba(30,26,22,0.07)"


def render_diagnostics(sections, quality_data, keyword_score):

    total_sections   = len(sections)
    present_sections = sum(1 for s in sections.values() if s)
    structure_score  = (present_sections / total_sections * 100) if total_sections else 0
    quality_score    = float(quality_data.get("quality_score", 0))
    word_count       = quality_data.get("word_count", 0)
    numbers_count    = quality_data.get("numbers_count", 0)

    # Colour for structure progress
    if structure_score >= 75: sp_col = "#16a34a"
    elif structure_score >= 50: sp_col = "#d97706"
    else: sp_col = "#c8401a"

    # Observations
    issues = []
    if structure_score < 75: issues.append(("warn", "Resume is missing important structural sections."))
    if quality_score   < 60: issues.append(("warn", "Resume lacks strong quantification and measurable impact."))
    if keyword_score   < 60: issues.append(("warn", "Keyword optimization for ATS systems is below recommended level."))
    if not issues:            issues.append(("ok",   "Resume structure and formatting meet professional standards."))

    obs_html = "".join(f"""
        <div style="display:flex;gap:0.65rem;align-items:flex-start;
                    padding:0.55rem 0;border-bottom:1px solid rgba(30,26,22,0.06);">
            <span style="font-size:0.95rem;flex-shrink:0;margin-top:1px;
                         color:{'#16a34a' if t=='ok' else '#d97706'};">{'✓' if t=='ok' else '▲'}</span>
            <span style="font-size:0.84rem;color:#5a4a40;line-height:1.6;">{msg}</span>
        </div>""" for t, msg in issues)

    def mc(val, lbl, accent="#1a4fc8"):
        return f"""<div style="background:#f8f6f1;border:1px solid rgba(30,26,22,0.09);
                               border-left:3px solid {accent};padding:0.8rem 0.9rem;flex:1;min-width:120px;">
            <div style="font-family:'Playfair Display',serif;font-size:1.55rem;font-weight:900;
                        color:#1e1a16;letter-spacing:-0.02em;line-height:1;margin-bottom:3px;">{val}</div>
            <div style="font-size:0.58rem;font-weight:800;letter-spacing:0.13em;
                        text-transform:uppercase;color:#9a8e84;">{lbl}</div>
        </div>"""

    metrics_html = f"""
    <div style="display:flex;gap:0.85rem;flex-wrap:wrap;">
        {mc(f"{structure_score:.0f}%", "Section Coverage", "#1a4fc8")}
        {mc(f"{keyword_score:.1f}%",   "Keyword Density",  "#c8401a")}
        {mc(str(word_count),            "Word Count",       "#d97706")}
        {mc(str(numbers_count),         "Numbers Used",     "#16a34a")}
        {mc(f"{quality_score:.0f}%",    "Quality Score",    "#1a4fc8")}
    </div>"""

    components.html(f"""<!DOCTYPE html><html><head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    body{{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;color:#1e1a16;}}
    .panel{{background:#fdfcf7;border:1px solid rgba(30,26,22,0.10);margin-bottom:1.1rem;overflow:hidden;}}
    .ph{{display:flex;align-items:center;gap:0.55rem;padding:0.7rem 1.1rem;
         border-bottom:1px solid rgba(30,26,22,0.08);background:#f5f2ea;}}
    .ptag{{font-size:0.56rem;font-weight:800;letter-spacing:0.18em;text-transform:uppercase;
           color:#c8401a;border:1px solid rgba(200,64,26,0.35);padding:2px 8px;
           background:rgba(200,64,26,0.04);}}
    .ptitle{{font-family:'Playfair Display',serif;font-size:0.95rem;font-weight:700;
             color:#1e1a16;letter-spacing:-0.01em;}}
    .pb{{padding:1.1rem;}}
    .prog{{height:5px;background:rgba(30,26,22,0.08);margin-top:0.85rem;}}
    .pf{{height:100%;background:{sp_col};width:{structure_score:.1f}%;}}
    </style></head><body>

    <!-- METRICS -->
    <div class="panel">
        <div class="ph"><span class="ptag">Metrics</span>
            <span class="ptitle">Quality & Coverage Metrics</span></div>
        <div class="pb">
            {metrics_html}
            <div class="prog"><div class="pf"></div></div>
        </div>
    </div>

    <!-- OBSERVATIONS -->
    <div class="panel">
        <div class="ph"><span class="ptag">Audit</span>
            <span class="ptitle">Structural Observations</span></div>
        <div class="pb">{obs_html}</div>
    </div>

    </body></html>""", height=420, scrolling=False)

    # ── Section presence bar chart — fully light-themed ──
    sec_names  = list(sections.keys())
    sec_values = [100 if v else 0 for v in sections.values()]
    sec_colors = ["#16a34a" if v else "#c8401a" for v in sections.values()]

    fig = go.Figure(data=[go.Bar(
        x=sec_names, y=sec_values,
        marker=dict(color=sec_colors, line=dict(color=_BG, width=2)),
        text=["Present" if v else "Missing" for v in sections.values()],
        textposition="outside",
        textfont=dict(family="Plus Jakarta Sans", size=11, color="#3c3631", weight=700),
        width=0.5,
    )])
    fig.update_layout(
        paper_bgcolor=_BG, plot_bgcolor=_PLOT,
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#3c3631", size=12),
        margin=dict(l=16, r=16, t=40, b=16),
        title=dict(text="Section Presence Map",
                   font=dict(family="Playfair Display, serif", size=16, color="#1e1a16"), x=0),
        yaxis=dict(range=[0, 140], showgrid=True, gridcolor=_GRID,
                   zeroline=False, showticklabels=False),
        xaxis=dict(showgrid=False,
                   tickfont=dict(family="Plus Jakarta Sans", size=11,
                                 color="#5a4a40", weight=700),
                   tickangle=-15, linecolor=_GRID),
        height=300, showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)