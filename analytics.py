# ======================================================
# ENTERPRISE AI ATS - INTERACTIVE ANALYTICS ENGINE
# Plotly Powered | Animated | Premium
# ======================================================

import plotly.graph_objects as go
import plotly.express as px
import numpy as np


# -----------------------------------------------------
# INTERACTIVE SCORE BREAKDOWN
# -----------------------------------------------------

def score_breakdown_chart(semantic, keyword, final):

    fig = go.Figure(data=[
        go.Bar(
            x=["Semantic", "Keyword", "Final"],
            y=[semantic, keyword, final],
            text=[f"{semantic:.1f}%", f"{keyword:.1f}%", f"{final:.1f}%"],
            textposition="auto"
        )
    ])

    fig.update_layout(
        height=350,
        template="plotly_dark",
        yaxis=dict(range=[0, 100]),
        margin=dict(l=20, r=20, t=40, b=20),
        title="Score Breakdown"
    )

    return fig


# -----------------------------------------------------
# INTERACTIVE RADAR
# -----------------------------------------------------

def radar_chart(metrics_dict):

    categories = list(metrics_dict.keys())
    values = list(metrics_dict.values())

    categories += [categories[0]]
    values += [values[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))

    fig.update_layout(
        template="plotly_dark",
        height=420,
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        margin=dict(l=20, r=20, t=40, b=20),
        title="Multi-Dimensional Performance Radar"
    )

    return fig


# -----------------------------------------------------
# SKILL GAP PIE
# -----------------------------------------------------

def skill_gap_chart(matched_count, missing_count):

    fig = px.pie(
        values=[matched_count, missing_count],
        names=["Matched", "Missing"],
        template="plotly_dark"
    )

    fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))

    return fig


# -----------------------------------------------------
# RECRUITER READINESS INDEX
# -----------------------------------------------------

def recruiter_readiness(semantic, keyword, skill_score, quality_score, weights):

    composite = (
        weights["semantic"] * semantic +
        weights["keyword"] * keyword +
        weights["skill"] * skill_score +
        weights["quality"] * quality_score
    )

    return max(0, min(composite, 100))
