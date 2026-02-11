# analytics.py

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import streamlit as st

# -------------------------------------------------
# Score Breakdown Bar Chart
# -------------------------------------------------

def score_breakdown_chart(semantic, keyword, final):

    data = pd.DataFrame({
        "Metric": ["Semantic", "Keyword", "Final"],
        "Score": [semantic, keyword, final]
    })

    fig, ax = plt.subplots()
    sns.barplot(x="Metric", y="Score", data=data, ax=ax)
    ax.set_ylim(0, 100)

    st.pyplot(fig)

# -------------------------------------------------
# Radar Chart
# -------------------------------------------------

def radar_chart(skill_match_percent):

    labels = list(skill_match_percent.keys())
    values = list(skill_match_percent.values())

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 100)

    st.pyplot(fig)
