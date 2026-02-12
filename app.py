# ======================================================
# ENTERPRISE AI ATS SYSTEM - COMPLETE PROFESSIONAL V7
# FIXED COMMON HEADER + FULL FOOTER RESTORED
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
    page_title="Enterprise AI ATS Pro",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🤖"
)

# ------------------------------------------------------
# PROFESSIONAL CSS
# ------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --glass-bg: rgba(255,255,255,0.95);
}

/* REMOVE DEFAULT TOP SPACE */
.block-container {
    padding-top: 6rem !important;
}

/* FIXED HEADER */
.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 1.2rem 2rem;
    z-index: 999;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    text-align: center;
}

.fixed-title {
    font-family: 'Inter', sans-serif;
    font-weight: 800;
    font-size: 1.8rem;
    color: white;
    margin: 0;
}

.fixed-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    color: rgba(255,255,255,0.9);
    margin-top: 4px;
}

/* SIDEBAR BRAND */
.sidebar-brand {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 1rem;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-weight: 700;
    margin-bottom: 1.5rem;
}

/* PRO CARDS */
.pro-card {
    background: var(--glass-bg);
    border-radius: 24px;
    padding: 2.5rem;
    box-shadow: 0 20px 45px rgba(0,0,0,0.12);
    text-align: center;
    transition: 0.3s ease;
}
.pro-card:hover {
    transform: translateY(-6px);
}

/* STATUS */
.status-banner {
    background: linear-gradient(135deg, #10b981, #059669);
    border-radius: 20px;
    padding: 1.2rem;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# FIXED HEADER (COMMON)
# ------------------------------------------------------
st.markdown("""
<div class='fixed-header'>
    <div class='fixed-title'>Enterprise AI ATS Pro</div>
    <div class='fixed-subtitle'>
        Advanced Resume Intelligence & Precision Job Matching
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
    st.session_state.jd_text = None
    st.session_state.scores = None
    st.session_state.initialized = False

# ------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class='sidebar-brand'>
        🤖 Enterprise AI ATS Pro
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎛️ Control Panel")
    st.markdown("---")

    if not st.session_state.initialized:
        st.info("Step 1: Upload & Analyze")

    nav_options = [
        "📤 Upload & Initialize",
        "📊 Executive Dashboard",
        "🎯 Skill Analysis",
        "📈 Score Breakdown",
        "💡 Resume Insights",
        "📄 Export Report"
    ]

    selected = st.radio(
        "Navigate:",
        nav_options,
        index=0 if not st.session_state.initialized else 1
    )

# ======================================================
# UPLOAD
# ======================================================
if selected == "📤 Upload & Initialize":

    st.markdown("## 🚀 Upload & Initialize Analysis")

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    with col2:
        jd_text = st.text_area("Paste Job Description", height=220)

    if st.button("🎯 ANALYZE RESUME NOW", type="primary"):
        if resume_file and jd_text.strip():

            reader = PyPDF2.PdfReader(resume_file)
            text = ""
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content + " "

            st.session_state.resume_text = text
            st.session_state.jd_text = jd_text
            st.session_state.scores = compute_scores(text, jd_text)
            st.session_state.initialized = True

            st.markdown("""
            <div class='status-banner'>
                ✅ Analysis Complete! Explore from sidebar.
            </div>
            """, unsafe_allow_html=True)

            st.balloons()
            st.rerun()

        else:
            st.error("Please upload resume AND paste job description.")

# ------------------------------------------------------
# PROTECTION
# ------------------------------------------------------
if selected != "📤 Upload & Initialize" and not st.session_state.initialized:
    st.error("Please complete Upload & Initialize first.")
    st.stop()

# ======================================================
# DASHBOARD
# ======================================================
elif selected == "📊 Executive Dashboard":

    semantic, keyword, final = st.session_state.scores

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"<div class='pro-card'><h3>Semantic</h3><h1>{semantic:.0f}%</h1></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='pro-card'><h3>Keyword</h3><h1>{keyword:.0f}%</h1></div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='pro-card'><h3>Final ATS</h3><h1>{final:.0f}%</h1></div>", unsafe_allow_html=True)

    st.progress(final / 100)

    quality = analyze_quality(st.session_state.resume_text)
    st.metric("Resume Quality", f"{quality['quantification_score']:.1f}%")
    st.metric("Word Count", f"{quality['word_count']:,}")

# ======================================================
# SKILL ANALYSIS
# ======================================================
elif selected == "🎯 Skill Analysis":

    resume_clean = clean_text(st.session_state.resume_text)
    jd_clean = clean_text(st.session_state.jd_text)

    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Matched Skills ({len(matched)})")
        for s in matched[:20]:
            st.success(s)

    with col2:
        st.subheader(f"Missing Skills ({len(missing)})")
        for s in missing[:20]:
            st.error(s)

# ======================================================
# SCORE BREAKDOWN
# ======================================================
elif selected == "📈 Score Breakdown":

    semantic, keyword, final = st.session_state.scores

    st.metric("Semantic", f"{semantic:.1f}%")
    st.metric("Keyword", f"{keyword:.1f}%")
    st.metric("Final", f"{final:.1f}%")

    score_breakdown_chart(semantic, keyword, final)

# ======================================================
# INSIGHTS
# ======================================================
elif selected == "💡 Resume Insights":

    sections = extract_sections(st.session_state.resume_text)

    for name, content in sections.items():
        with st.expander(name.upper()):
            st.write(content if content else "No content detected")

# ======================================================
# EXPORT
# ======================================================
elif selected == "📄 Export Report":

    semantic, keyword, final = st.session_state.scores
    quality = analyze_quality(st.session_state.resume_text)

    if st.button("Generate & Download PDF", type="primary", use_container_width=True):
        generate_pdf_report({
            "semantic": semantic,
            "keyword": keyword,
            "final": final,
            "word_count": quality["word_count"]
        })

# ======================================================
# FOOTER (FULL RESTORED WITH ICONS)
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
