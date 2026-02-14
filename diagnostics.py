# ======================================================
# DIAGNOSTICS MODULE
# Advanced Resume Structural Intelligence
# ======================================================

import streamlit as st
import plotly.graph_objects as go


def render_diagnostics(sections, quality_data, keyword_score):
    """
    Advanced resume structural diagnostics.
    """

    st.markdown('<div class="section-title">Resume Structural Diagnostics</div>', unsafe_allow_html=True)

    # -------------------------------------------------
    # Section Coverage Score
    # -------------------------------------------------

    total_sections = len(sections)
    present_sections = sum(1 for s in sections.values() if s)

    structure_score = (present_sections / total_sections) * 100

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Section Coverage", f"{structure_score:.0f}%")
        st.progress(structure_score / 100)

    with col2:
        st.metric("Keyword Density Score", f"{keyword_score:.1f}%")

    st.divider()

    # -------------------------------------------------
    # Section Presence Breakdown (Interactive Chart)
    # -------------------------------------------------

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=list(sections.keys()),
        y=[100 if v else 0 for v in sections.values()],
        marker_color="#2563eb"
    ))

    fig.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="#0b1220",
        plot_bgcolor="#0b1220",
        font=dict(color="white"),
        yaxis=dict(range=[0, 100])
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # -------------------------------------------------
    # Risk Flags & Improvement Suggestions
    # -------------------------------------------------

    st.markdown("### Structural Observations")

    issues = []

    if structure_score < 75:
        issues.append("Resume is missing important structural sections.")

    if quality_data["quality_score"] < 60:
        issues.append("Resume lacks strong quantification and measurable impact.")

    if keyword_score < 60:
        issues.append("Keyword optimization for ATS systems is below recommended level.")

    if not issues:
        st.success("Resume structure and formatting meet professional standards.")
    else:
        for issue in issues:
            st.warning(issue)

    st.divider()

    # -------------------------------------------------
    # Quality Metrics
    # -------------------------------------------------

    col3, col4, col5 = st.columns(3)

    col3.metric("Word Count", quality_data["word_count"])
    col4.metric("Numbers Used", quality_data["numbers_count"])
    col5.metric("Quality Score", f"{quality_data['quality_score']:.0f}%")

    st.progress(quality_data["quality_score"] / 100)
