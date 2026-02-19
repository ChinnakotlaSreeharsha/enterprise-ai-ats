# ======================================================
# ANALYTICS ENGINE — Warm light Plotly theme
# ======================================================

import plotly.graph_objects as go
import plotly.express as px

_BG   = "#fdfcf7"
_PLOT = "#f8f6f1"
_GRID = "rgba(30,26,22,0.07)"
_FONT = dict(family="Plus Jakarta Sans, sans-serif", color="#3c3631", size=12)
_MARGIN = dict(l=24, r=24, t=48, b=24)
_HOVER = dict(bgcolor="#fdfcf7", bordercolor="rgba(30,26,22,0.15)",
              font=dict(family="Plus Jakarta Sans, sans-serif", color="#1e1a16"))

_TITLE_FONT = dict(family="Playfair Display, serif", size=17, color="#1e1a16")


def score_breakdown_chart(semantic, keyword, final):
    fig = go.Figure(data=[go.Bar(
        x=["Semantic", "Keyword", "Final ATS"],
        y=[semantic, keyword, final],
        text=[f"{v:.1f}%" for v in [semantic, keyword, final]],
        textposition="outside",
        textfont=dict(family="Plus Jakarta Sans", size=12, color="#1e1a16", weight=700),
        marker=dict(
            color=["#c8401a", "#1a4fc8", "#d97706"],
            line=dict(color=_BG, width=2)
        ),
        width=0.42,
    )])
    fig.update_layout(
        paper_bgcolor=_BG, plot_bgcolor=_PLOT, font=_FONT, margin=_MARGIN,
        hoverlabel=_HOVER,
        title=dict(text="Score Breakdown", font=_TITLE_FONT, x=0),
        yaxis=dict(range=[0,118], showgrid=True, gridcolor=_GRID,
                   zeroline=False, ticksuffix="%", tickfont=dict(color="#7a7065"),
                   linecolor=_GRID),
        xaxis=dict(showgrid=False, tickfont=dict(family="Plus Jakarta Sans",
                   size=12, color="#5a4a40", weight=700), linecolor=_GRID),
        height=360, showlegend=False,
    )
    return fig


def radar_chart(metrics_dict):
    cats = list(metrics_dict.keys())
    vals = list(metrics_dict.values())
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vals + [vals[0]], theta=cats + [cats[0]],
        fill="toself",
        fillcolor="rgba(200,64,26,0.09)",
        line=dict(color="#c8401a", width=2),
        marker=dict(color="#c8401a", size=7),
    ))
    fig.update_layout(
        paper_bgcolor=_BG, font=_FONT, margin=_MARGIN, hoverlabel=_HOVER,
        title=dict(text="Multi-Dimensional Radar", font=_TITLE_FONT, x=0),
        polar=dict(
            bgcolor=_PLOT,
            radialaxis=dict(visible=True, range=[0,100], ticksuffix="%",
                            gridcolor=_GRID, linecolor=_GRID,
                            tickfont=dict(color="#7a7065", size=10)),
            angularaxis=dict(tickfont=dict(family="Plus Jakarta Sans",
                             size=12, color="#3c3631", weight=700),
                             linecolor="rgba(30,26,22,0.12)"),
        ),
        height=420,
    )
    return fig


def skill_gap_chart(matched_count, missing_count):
    total = matched_count + missing_count or 1
    fig = go.Figure(data=[go.Pie(
        labels=["Matched Skills", "Missing Skills"],
        values=[matched_count, missing_count],
        hole=0.55,
        marker=dict(colors=["#16a34a", "#c8401a"],
                    line=dict(color=_BG, width=3)),
        textfont=dict(family="Plus Jakarta Sans", size=12,
                      color="#1e1a16", weight=700),
        textinfo="label+percent",
    )])
    fig.add_annotation(
        text=f"<b>{matched_count}/{total}</b>", x=0.5, y=0.5,
        showarrow=False,
        font=dict(family="Playfair Display, serif", size=22, color="#1e1a16"),
    )
    fig.update_layout(
        paper_bgcolor=_BG, font=_FONT, margin=_MARGIN, hoverlabel=_HOVER,
        title=dict(text="Skill Gap Analysis", font=_TITLE_FONT, x=0),
        height=360,
        legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.08,
                    font=dict(family="Plus Jakarta Sans", size=12, color="#5a4a40")),
        showlegend=True,
    )
    return fig


def recruiter_readiness(semantic, keyword, skill_score, quality_score, weights):
    composite = (
        weights["semantic"] * semantic +
        weights["keyword"]  * keyword  +
        weights["skill"]    * skill_score +
        weights["quality"]  * quality_score
    )
    return max(0, min(composite, 100))