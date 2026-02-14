# ======================================================
# ENTERPRISE AI ATS - FINAL PREMIUM CONTROLLER
# Modular | Interactive | Production Safe | SaaS Ready
# ======================================================

import streamlit as st
import time

from header import load_header
from footer import load_footer
from upload import render_upload_page
from dashboard import render_dashboard
from skills import render_skills_page
from diagnostics import render_diagnostics

from ats_engine import clean_text
from analytics import (
    score_breakdown_chart,
    radar_chart,
    skill_gap_chart,
    recruiter_readiness
)
from report_generator import generate_pdf_report
from section_analyzer import extract_sections
from quality_analyzer import analyze_quality


# ======================================================
# AI EXECUTIVE SUMMARY
# ======================================================

def generate_executive_summary(semantic, keyword, skill, quality, readiness):

    semantic = float(max(0, min(semantic, 100)))
    keyword = float(max(0, min(keyword, 100)))
    skill = float(max(0, min(skill, 100)))
    quality = float(max(0, min(quality, 100)))
    readiness = float(max(0, min(readiness, 100)))

    if readiness >= 85:
        tier = "Highly Competitive Candidate"
        verdict = "Strong hiring potential."
    elif readiness >= 70:
        tier = "Strong Potential Candidate"
        verdict = "Competitive but can be optimized."
    elif readiness >= 55:
        tier = "Moderate Fit Candidate"
        verdict = "Needs measurable improvements."
    else:
        tier = "Requires Significant Optimization"
        verdict = "Substantial ATS optimization required."

    return (
        f"Semantic Alignment: {semantic:.1f}% | "
        f"Keyword Optimization: {keyword:.1f}% | "
        f"Skill Match: {skill:.1f}% | "
        f"Structural Quality: {quality:.1f}%.\n\n"
        f"Recruiter Simulation Score: {readiness:.1f}%.\n\n"
        f"Candidate Classification: {tier}. {verdict}"
    )


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Enterprise AI ATS",
    layout="wide",
    page_icon="🤖"
)


# ======================================================
# GLOBAL DESIGN SYSTEM
# ======================================================

def load_global_styles():
    st.markdown("""
    <style>

    .stApp { background-color: #0b1220; }

    .section-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 15px;
        margin-top: 5px;
        color: #e5e7eb;
    }

    div[data-testid="stMetric"] {
        background: #111827;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.05);
    }

    div[data-baseweb="tab-list"] {
        background: #0b1220;
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    button[data-baseweb="tab"] {
        border-radius: 25px !important;
        padding: 8px 18px !important;
        color: #9ca3af !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: #2563eb !important;
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)


# ======================================================
# SESSION STATE
# ======================================================

if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "generated_pdf" not in st.session_state:
    st.session_state.generated_pdf = None

if "show_export_popup" not in st.session_state:
    st.session_state.show_export_popup = False


# ======================================================
# HEADER
# ======================================================

load_header(st.session_state.initialized)
load_global_styles()
st.markdown("<div style='height:85px;'></div>", unsafe_allow_html=True)


# ======================================================
# TABS
# ======================================================

tab_upload, tab_dashboard, tab_skills, tab_analytics, tab_diagnostics, tab_export = st.tabs([
    "Upload",
    "Dashboard",
    "Skills",
    "Analytics",
    "Diagnostics",
    "Export"
])


# ======================================================
# UPLOAD TAB
# ======================================================

with tab_upload:
    render_upload_page()


# ======================================================
# LOCK CHECK
# ======================================================

if not st.session_state.initialized:

    for tab in [tab_dashboard, tab_skills, tab_analytics, tab_diagnostics, tab_export]:
        with tab:
            st.warning("Upload resume to unlock this section.")

else:

    # ---------------- Core Data ----------------
    semantic, keyword, final = map(float, st.session_state.scores)

    semantic = max(0.0, min(semantic, 100.0))
    keyword = max(0.0, min(keyword, 100.0))
    final = max(0.0, min(final, 100.0))

    resume_text = st.session_state.resume_text
    jd_text = st.session_state.jd_text

    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    quality_data = analyze_quality(resume_text)
    sections = extract_sections(resume_text)

    from skills import extract_skills, skill_match_score

    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)
    skill_score = skill_match_score(resume_skills, jd_skills)


    # ======================================================
    # DASHBOARD
    # ======================================================

    with tab_dashboard:

        st.markdown('<div class="section-title">Executive Overview</div>', unsafe_allow_html=True)

        animated_placeholder = st.empty()
        for i in range(int(final) + 1):
            animated_placeholder.metric("Final ATS Score", f"{i}%")
            time.sleep(0.0015)

        render_dashboard(
            semantic,
            keyword,
            final,
            skill_score=skill_score,
            quality_score=quality_data["quality_score"],
            sections=sections
        )


    # ======================================================
    # SKILLS
    # ======================================================

    with tab_skills:
        render_skills_page(resume_clean, jd_clean)


    # ======================================================
    # ANALYTICS
    # ======================================================

    with tab_analytics:

        st.markdown('<div class="section-title">Recruiter Weight Simulation</div>', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        weights = {
            "semantic": col1.slider("Semantic", 0.0, 1.0, 0.35),
            "keyword": col2.slider("Keyword", 0.0, 1.0, 0.30),
            "skill": col3.slider("Skill", 0.0, 1.0, 0.20),
            "quality": col4.slider("Quality", 0.0, 1.0, 0.15)
        }

        total = sum(weights.values())
        if total > 0:
            for k in weights:
                weights[k] /= total

        readiness = recruiter_readiness(
            semantic,
            keyword,
            skill_score,
            quality_data["quality_score"],
            weights
        )

        readiness = max(0.0, min(readiness, 100.0))

        st.metric("Simulated Recruiter Score", f"{readiness:.1f}%")
        st.progress(readiness / 100)

        st.divider()

        colA, colB = st.columns(2)

        with colA:
            st.plotly_chart(
                score_breakdown_chart(semantic, keyword, final),
                use_container_width=True
            )

        with colB:
            st.plotly_chart(
                radar_chart({
                    "Semantic": semantic,
                    "Keyword": keyword,
                    "Skill": skill_score,
                    "Quality": quality_data["quality_score"]
                }),
                use_container_width=True
            )

        st.divider()

        st.plotly_chart(
            skill_gap_chart(
                len(set(resume_skills) & set(jd_skills)),
                len(set(jd_skills) - set(resume_skills))
            ),
            use_container_width=True
        )

        st.divider()

        st.markdown('<div class="section-title">AI Executive Summary</div>', unsafe_allow_html=True)

        summary = generate_executive_summary(
            semantic,
            keyword,
            skill_score,
            quality_data["quality_score"],
            readiness
        )

        st.info(summary)


    # ======================================================
    # DIAGNOSTICS
    # ======================================================

    with tab_diagnostics:
        render_diagnostics(
            sections=sections,
            quality_data=quality_data,
            keyword_score=keyword
        )


    # ======================================================
    # EXPORT - PREMIUM MODAL EXPERIENCE
    # ======================================================

    with tab_export:

        if "generated_pdf" not in st.session_state:
            st.session_state.generated_pdf = None

        if "show_export_modal" not in st.session_state:
            st.session_state.show_export_modal = False

        if "download_complete" not in st.session_state:
            st.session_state.download_complete = False


        if st.button("Generate PDF Report", use_container_width=True):

            pdf_bytes = generate_pdf_report({
                "semantic": semantic,
                "keyword": keyword,
                "final": final,
                "skill_score": skill_score,
                "quality_score": quality_data["quality_score"],
                "word_count": quality_data["word_count"],
                "matched_skills": list(set(resume_skills) & set(jd_skills)),
                "missing_skills": list(set(jd_skills) - set(resume_skills)),
                "sections": sections,
                "readiness": readiness
            })


            if pdf_bytes:
                st.session_state.generated_pdf = pdf_bytes
                st.session_state.show_export_modal = True
                st.session_state.download_complete = False


        # ================= MODAL =================

        if st.session_state.show_export_modal:

            @st.dialog("Report Ready")
            def export_modal():

                st.markdown(
                    """
                    <style>
                    .stDialog > div {
                        backdrop-filter: blur(10px);
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                # Animated Progress Ring
                progress_placeholder = st.empty()
                for i in range(101):
                    progress_placeholder.progress(i / 100)
                    time.sleep(0.01)

                st.success("Your ATS report has been generated successfully.")

                # PDF Preview
                st.markdown("### PDF Preview")

                pdf_preview = st.session_state.generated_pdf
                st.download_button(
                    label="Download ATS Report",
                    data=pdf_preview,
                    file_name="ATS_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    on_click=lambda: st.session_state.update(download_complete=True)
                )

                # Confetti after download
                if st.session_state.download_complete:
                    st.balloons()
                    st.info("Download started. This window will close automatically.")
                    time.sleep(2)
                    st.session_state.show_export_modal = False
                    st.session_state.download_complete = False
                    st.rerun()

                if st.button("Close"):
                    st.session_state.show_export_modal = False
                    st.rerun()

            export_modal()


# ======================================================
# FOOTER
# ======================================================

st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
load_footer()
