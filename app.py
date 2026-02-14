# ======================================================
# ATS SAAS 2.1 PRODUCTION BUILD
# STICKY TABS BELOW HEADER
# ======================================================

import streamlit as st
import PyPDF2
import time

from header import load_header
from footer import load_footer

from ats_engine import compute_scores, clean_text
from skill_engine import extract_skills
from analytics import score_breakdown_chart
from report_generator import generate_pdf_report
from section_analyzer import extract_sections
from quality_analyzer import analyze_quality


# ------------------------------------------------------
# CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI ATS",
    layout="wide",
    page_icon="🤖"
)

# ------------------------------------------------------
# SESSION STATE INIT
# ------------------------------------------------------
if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
    st.session_state.jd_text = None
    st.session_state.scores = None


# ------------------------------------------------------
# LOAD HEADER
# ------------------------------------------------------
load_header(st.session_state.initialized)

# Spacer for fixed header height
st.markdown("<div style='height:85px;'></div>", unsafe_allow_html=True)


# ------------------------------------------------------
# STICKY TABS CSS (THE IMPORTANT FIX)
# ------------------------------------------------------
st.markdown("""
<style>

/* Sticky Tabs */
div[data-baseweb="tab-list"] {
    position: sticky;
    top: 85px;
    background: #0b1220;
    z-index: 999;
    padding-top: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Tab Styling */
button[data-baseweb="tab"] {
    border-radius: 25px !important;
    margin-right: 8px !important;
    padding: 8px 18px !important;
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

/* Hover */
button[data-baseweb="tab"]:hover {
    border-color: #3b82f6 !important;
    color: #3b82f6 !important;
}

/* Active Tab */
button[data-baseweb="tab"][aria-selected="true"] {
    background: #3b82f6 !important;
    border-color: #3b82f6 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------
# TABS NAVIGATION
# ------------------------------------------------------
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

    st.title("Resume Upload & ATS Analysis")

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    with col2:
        jd_text = st.text_area("Paste Job Description", height=220)

    if st.button("Run ATS Analysis", type="primary"):

        if resume_file and jd_text.strip():

            loading = st.empty()

            with loading.container():

                st.info("Initializing ATS Engine...")
                progress = st.progress(0)

                for i in range(20):
                    time.sleep(0.02)
                    progress.progress(i + 1)

                st.info("Parsing Resume...")
                reader = PyPDF2.PdfReader(resume_file)
                text = ""

                for page in reader.pages:
                    if page.extract_text():
                        text += page.extract_text() + " "

                for i in range(20, 60):
                    time.sleep(0.02)
                    progress.progress(i + 1)

                st.info("Computing Scores...")
                semantic, keyword, final = compute_scores(text, jd_text)

                for i in range(60, 100):
                    time.sleep(0.02)
                    progress.progress(i + 1)

            loading.empty()

            st.session_state.resume_text = text
            st.session_state.jd_text = jd_text
            st.session_state.scores = (semantic, keyword, final)
            st.session_state.initialized = True

            st.success("Analysis Completed Successfully ✔")

        else:
            st.error("Both resume and job description are required.")


# ------------------------------------------------------
# LOCK OTHER TABS IF NOT INITIALIZED
# ------------------------------------------------------
if not st.session_state.initialized:
    with tab_dashboard:
        st.warning("Upload resume to unlock Dashboard.")
    with tab_skills:
        st.warning("Upload resume to unlock Skills.")
    with tab_analytics:
        st.warning("Upload resume to unlock Analytics.")
    with tab_diagnostics:
        st.warning("Upload resume to unlock Diagnostics.")
    with tab_export:
        st.warning("Upload resume to unlock Export.")
else:

    semantic, keyword, final = st.session_state.scores

    with tab_dashboard:
        st.title("Executive Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Semantic Match", f"{semantic:.0f}%")
        col2.metric("Keyword Match", f"{keyword:.0f}%")
        col3.metric("Final ATS Score", f"{final:.0f}%")
        st.progress(final / 100)

    with tab_skills:
        st.title("Skill Intelligence")
        resume_clean = clean_text(st.session_state.resume_text)
        jd_clean = clean_text(st.session_state.jd_text)

        resume_skills = extract_skills(resume_clean)
        jd_skills = extract_skills(jd_clean)

        matched = list(set(resume_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        col1, col2 = st.columns(2)
        with col1:
            for skill in matched[:20]:
                st.success(skill)
        with col2:
            for skill in missing[:20]:
                st.error(skill)

    with tab_analytics:
        st.title("Score Analytics")
        score_breakdown_chart(semantic, keyword, final)

    with tab_diagnostics:
        st.title("Resume Diagnostics")
        sections = extract_sections(st.session_state.resume_text)
        for name, content in sections.items():
            with st.expander(name.upper()):
                st.write(content if content else "No content detected")

    with tab_export:
        st.title("Export ATS Report")
        if st.button("Generate PDF Report", type="primary", use_container_width=True):
            generate_pdf_report({
                "semantic": semantic,
                "keyword": keyword,
                "final": final,
                "word_count": analyze_quality(st.session_state.resume_text)["word_count"]
            })
            st.success("Report Generated Successfully.")


# ------------------------------------------------------
# FOOTER
# ------------------------------------------------------
st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
load_footer()
