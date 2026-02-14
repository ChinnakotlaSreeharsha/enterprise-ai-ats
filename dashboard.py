# ======================================================
# ENTERPRISE AI ATS - PROFESSIONAL EXECUTIVE DASHBOARD
# Structured | Visual | Enterprise-Grade
# ======================================================

import streamlit as st


def hiring_classification(score):
    if score >= 85:
        return "High Confidence Hire", "#16a34a"
    elif score >= 70:
        return "Strong Potential Candidate", "#22c55e"
    elif score >= 55:
        return "Moderate Fit – Needs Optimization", "#f59e0b"
    else:
        return "High Rejection Risk", "#dc2626"


def render_dashboard(semantic, keyword, final, skill_score=None, quality_score=None, sections=None):

    semantic = float(semantic)
    keyword = float(keyword)
    final = float(final)

    classification, color = hiring_classification(final)

    st.markdown("""
    <style>
    .card {
        background: #111827;
        padding: 24px;
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.05);
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .big-score {
        font-size: 38px;
        font-weight: 700;
    }
    .subtle {
        color: #9ca3af;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Executive Hiring Intelligence Overview")

    # --------------------------------------------------
    # PRIMARY SCORE PANEL
    # --------------------------------------------------
    st.markdown(f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between;">
            <div>
                <div class="subtle">Final ATS Score</div>
                <div class="big-score">{final:.0f}%</div>
            </div>
            <div style="text-align:right;">
                <div class="subtle">Hiring Classification</div>
                <div style="font-size:20px; font-weight:600; color:{color};">
                    {classification}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(float(max(0, min(final, 100)) / 100))

    # --------------------------------------------------
    # SCORE ARCHITECTURE
    # --------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Score Architecture</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Semantic Alignment", f"{semantic:.1f}%")
    col2.metric("Keyword Relevance", f"{keyword:.1f}%")

    if skill_score is not None:
        col3.metric("Skill Match", f"{float(skill_score):.1f}%")
    else:
        col3.metric("Skill Match", "N/A")

    if quality_score is not None:
        col4.metric("Resume Quality", f"{float(quality_score):.0f}%")
    else:
        col4.metric("Resume Quality", "N/A")

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------
    # SECTION COMPLETENESS MATRIX
    # --------------------------------------------------
    if sections:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Section Completeness</div>', unsafe_allow_html=True)

        for name, content in sections.items():
            status = "Present" if content else "Missing"
            color_status = "#16a34a" if content else "#dc2626"

            st.markdown(
                f"<div style='display:flex; justify-content:space-between;'>"
                f"<div>{name.capitalize()}</div>"
                f"<div style='color:{color_status}; font-weight:600;'>{status}</div>"
                f"</div>",
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------
    # RISK ASSESSMENT
    # --------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Risk Assessment</div>', unsafe_allow_html=True)

    risks = []

    if semantic < 60:
        risks.append("Low contextual alignment with job description.")
    if keyword < 60:
        risks.append("Insufficient keyword optimization for ATS filters.")
    if skill_score is not None and skill_score < 60:
        risks.append("Skill coverage does not sufficiently match job requirements.")
    if quality_score is not None and quality_score < 50:
        risks.append("Resume lacks quantified achievements or optimal structure.")

    if not risks:
        risks.append("No major structural or alignment risks detected.")

    for r in risks:
        st.write(f"- {r}")

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------
    # OPTIMIZATION ROADMAP
    # --------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Optimization Roadmap</div>', unsafe_allow_html=True)

    recommendations = []

    if keyword < 75:
        recommendations.append("Integrate more role-specific keywords naturally within experience section.")
    if semantic < 75:
        recommendations.append("Rephrase responsibilities to better mirror job description context.")
    if skill_score and skill_score < 75:
        recommendations.append("Add missing required skills explicitly in skills section.")
    if quality_score and quality_score < 60:
        recommendations.append("Include measurable achievements (%, numbers, impact metrics).")

    if not recommendations:
        recommendations.append("Resume is strategically aligned. Minor refinements may enhance competitiveness.")

    for rec in recommendations:
        st.write(f"- {rec}")

    st.markdown('</div>', unsafe_allow_html=True)
