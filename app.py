# ======================================================
# ENTERPRISE AI ATS SYSTEM - FINAL CLEAN VERSION
# ======================================================

import streamlit as st
import PyPDF2

from ats_engine import compute_scores, clean_text
from skill_engine import extract_skills, skill_match_score
from analytics import score_breakdown_chart, radar_chart
from report_generator import generate_pdf_report
from section_analyzer import extract_sections
from quality_analyzer import analyze_quality

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------

st.set_page_config(
    page_title="Enterprise AI ATS",
    layout="wide",
    page_icon="https://www.flaticon.com/free-icon/human-resources_9948580"
)

# ------------------------------------------------------
# THEME TOGGLE
# ------------------------------------------------------

theme = st.sidebar.radio("Theme Mode", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: #ffffff;
        }
        </style>
    """, unsafe_allow_html=True)

# ------------------------------------------------------
# HEADER
# ------------------------------------------------------

st.markdown("""
<h1 style='text-align:center;'>Enterprise AI ATS Resume Scanner</h1>
<p style='text-align:center;'>Advanced Resume Intelligence & Job Matching Platform</p>
<hr>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------

if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
    st.session_state.jd_text = None
    st.session_state.scores = None

# ------------------------------------------------------
# SIDEBAR NAVIGATION
# ------------------------------------------------------

menu = st.sidebar.radio("Navigation", [
    "Upload & Initialize",
    "Dashboard",
    "Skill Analysis",
    "Score Breakdown",
    "Insights",
    "Export Report"
])

# ======================================================
# MODULE 1: UPLOAD
# ======================================================

if menu == "Upload & Initialize":

    st.subheader("Upload Resume & Job Description")

    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    jd_text = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):

        if resume_file and jd_text:

            reader = PyPDF2.PdfReader(resume_file)
            text = ""

            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content + " "

            st.session_state.resume_text = text
            st.session_state.jd_text = jd_text
            st.session_state.scores = compute_scores(text, jd_text)

            st.success("Resume & JD initialized successfully!")

        else:
            st.warning("Please upload both Resume and Job Description.")

# ------------------------------------------------------
# CHECK INITIALIZATION
# ------------------------------------------------------

if menu != "Upload & Initialize" and not st.session_state.scores:
    st.warning("Please initialize resume and JD first.")
    st.stop()

# ======================================================
# DASHBOARD
# ======================================================

if menu == "Dashboard":

    st.subheader("ATS Overview")

    semantic, keyword, final = st.session_state.scores

    col1, col2, col3 = st.columns(3)

    col1.metric("Semantic Score", f"{semantic:.2f}%")
    col2.metric("Keyword Score", f"{keyword:.2f}%")
    col3.metric("Final ATS Score", f"{final:.2f}%")

    st.progress(int(final))

    quality = analyze_quality(st.session_state.resume_text)

    st.subheader("Resume Quality")
    st.metric("Quality Score", quality["quantification_score"])
    st.write("Word Count:", quality["word_count"])

# ======================================================
# SKILL ANALYSIS
# ======================================================

elif menu == "Skill Analysis":

    st.subheader("Skill Gap & Radar Analysis")

    resume_clean = clean_text(st.session_state.resume_text)
    jd_clean = clean_text(st.session_state.jd_text)

    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    col1, col2 = st.columns(2)

    with col1:
        st.write("### ✅ Matched Skills")
        st.write(matched)

    with col2:
        st.write("### ❌ Missing Skills")
        st.write(missing)

    skill_match_percent = skill_match_score(resume_skills, jd_skills)

    st.metric("Skill Match %", f"{skill_match_percent:.2f}%")

    radar_chart({
        "Skill Match": skill_match_percent,
        "Resume Quality": analyze_quality(st.session_state.resume_text)["quantification_score"]
    })

# ======================================================
# SCORE BREAKDOWN
# ======================================================

elif menu == "Score Breakdown":

    st.subheader("Score Breakdown Analytics")

    semantic, keyword, final = st.session_state.scores
    score_breakdown_chart(semantic, keyword, final)

# ======================================================
# INSIGHTS
# ======================================================

elif menu == "Insights":

    st.subheader("Resume Section Insights")

    sections = extract_sections(st.session_state.resume_text)

    for section_name, content in sections.items():
        st.markdown(f"### {section_name.capitalize()}")
        st.write(content[:600] + "..." if content else "Not Detected")

# ======================================================
# EXPORT REPORT
# ======================================================

elif menu == "Export Report":

    st.subheader("Download Professional ATS PDF Report")

    semantic, keyword, final = st.session_state.scores
    quality = analyze_quality(st.session_state.resume_text)

    generate_pdf_report({
        "semantic": semantic,
        "keyword": keyword,
        "final": final,
        "word_count": quality["word_count"]
    })

# ======================================================
# CLEAN ICON FOOTER (STREAMLIT NATIVE)
# ======================================================

st.markdown("---")

st.markdown("© 2026 **Chinnakotla Sree Harsha**")
st.markdown("AI Powered ATS Resume Scanner Platform")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3536/3536505.png", width=30)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/chinnakotla-sree-harsha-85502620b)")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/841/841364.png", width=30)
    st.markdown("[Portfolio](https://myportfolio-i3gd.onrender.com/)")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/733/733553.png", width=30)
    st.markdown("[GitHub](https://github.com/ChinnakotlaSreeharsha)")

with col4:
    st.image("https://cdn-icons-png.flaticon.com/512/733/733558.png", width=30)
    st.markdown("[Linktree](https://linktr.ee/chinnakotla_sreeharsha)")
