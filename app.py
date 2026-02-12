# ======================================================
# ENTERPRISE AI ATS SYSTEM - COMPLETE PROFESSIONAL V4
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
# PROFESSIONAL PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI ATS Pro",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🤖"
)

# ------------------------------------------------------
# COMPLETE PROFESSIONAL CSS
# ------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --glass-bg: rgba(255, 255, 255, 0.95);
        --glass-border: rgba(255,255,255,0.2);
    }
    
    .main { padding-top: 2rem; }
    
    /* HERO HEADER */
    .hero-header {
        background: var(--primary-gradient);
        border-radius: 30px;
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 30px 60px rgba(102,126,234,0.3);
    }
    
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: clamp(2.5rem, 6vw, 4.5rem);
        background: white;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 1rem 0;
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: clamp(1.1rem, 3vw, 1.4rem);
        color: rgba(255,255,255,0.95);
        margin: 0;
    }
    
    /* PRO CARDS */
    .pro-card {
        background: var(--glass-bg);
        backdrop-filter: blur(25px);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 25px 50px rgba(0,0,0,0.12);
        border: 1px solid var(--glass-border);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .pro-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 40px 80px rgba(0,0,0,0.2);
    }
    
    /* MEGA BUTTON */
    .mega-btn {
        background: var(--primary-gradient);
        border: none;
        border-radius: 20px;
        padding: 1.2rem 3rem;
        font-weight: 700;
        font-size: 1.15rem;
        color: white;
        transition: all 0.4s ease;
        box-shadow: 0 15px 35px rgba(102,126,234,0.4);
        width: 100%;
    }
    
    .mega-btn:hover {
        transform: translateY(-4px);
        box-shadow: 0 25px 50px rgba(102,126,234,0.6);
    }
    
    /* SIDEBAR */
    .sidebar .stRadio > div > div > label {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        padding: 1.2rem 1.5rem;
        border-radius: 16px;
        margin: 0.3rem 0;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        font-size: 1.05rem;
    }
    
    .sidebar .stRadio > div > div > label:hover {
        background: rgba(102,126,234,0.08);
        border-color: #667eea;
        color: #667eea !important;
        transform: translateX(8px);
    }
    
    /* STATUS */
    .status-banner {
        background: linear-gradient(135deg, #10b981, #059669);
        border-radius: 20px;
        padding: 1.5rem 2rem;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(16,185,129,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# SESSION STATE - COMPLETE
# ------------------------------------------------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = None
    st.session_state.jd_text = None
    st.session_state.scores = None
    st.session_state.initialized = False

# ------------------------------------------------------
# HERO HEADER
# ------------------------------------------------------
st.markdown("""
<div class='hero-header'>
    <h1 class='main-title'>Enterprise AI ATS Pro</h1>
    <p class='hero-subtitle'>Advanced Resume Intelligence & Precision Job Matching</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# MAIN CONTENT AREA
# ------------------------------------------------------

# SIDEBAR NAVIGATION - ALWAYS VISIBLE
with st.sidebar:
    st.markdown("## 🎛️ **Control Panel**")
    st.markdown("---")
    
    if not st.session_state.initialized:
        st.info("👆 **Step 1: Upload & Analyze**")
        st.markdown("---")
    
    nav_options = [
        "📤 **Upload & Initialize**",
        "📊 **Executive Dashboard**",
        "🎯 **Skill Analysis**", 
        "📈 **Score Breakdown**",
        "💡 **Resume Insights**",
        "📄 **Export Report**"
    ]
    
    selected = st.radio(
        "Navigate:", 
        nav_options,
        index=0 if not st.session_state.initialized else 1,
        key="main_nav"
    )
    
    menu_map = {
        "📤 **Upload & Initialize**": "Upload",
        "📊 **Executive Dashboard**": "Dashboard",
        "🎯 **Skill Analysis**": "Skills", 
        "📈 **Score Breakdown**": "Breakdown",
        "💡 **Resume Insights**": "Insights",
        "📄 **Export Report**": "Export"
    }
    menu = menu_map[selected]

# ======================================================
# UPLOAD & INITIALIZE
# ======================================================
if menu == "Upload":
    st.markdown("## 🚀 **Upload & Initialize Analysis**")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 📄 **Upload Resume**")
        resume_file = st.file_uploader(
            "Choose PDF Resume", 
            type=["pdf"],
            help="Upload your resume in PDF format"
        )
    
    with col2:
        st.markdown("### 💼 **Job Description**")
        jd_text = st.text_area(
            "Paste Job Description", 
            height=220,
            placeholder="Paste the complete job description here...",
            help="Copy-paste the full job posting"
        )
    
    if st.button("🎯 **ANALYZE RESUME NOW**", type="primary", key="analyze_btn", help="Click after uploading both files"):
        if resume_file and jd_text.strip():
            with st.spinner("🔬 AI Processing your documents..."):
                try:
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
                        <h3>✅ ANALYSIS COMPLETE!</h3>
                        <p>🎉 Use sidebar navigation to explore all insights</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error processing PDF: {str(e)}")
        else:
            st.error("🔴 **Please upload resume AND paste job description**")

# ------------------------------------------------------
# CHECK INITIALIZATION FOR OTHER PAGES
# ------------------------------------------------------
if menu != "Upload" and not st.session_state.initialized:
    st.error("👆 **Please complete Upload & Initialize first from sidebar**")
    st.stop()

# ======================================================
# DASHBOARD
# ======================================================
if menu == "Dashboard":
    st.markdown("## 📊 **Executive Dashboard**")
    
    semantic, keyword, final = st.session_state.scores
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown(f"""
        <div class='pro-card'>
            <div style='font-size: 3.5rem; margin-bottom: 1rem;'>🤖</div>
            <h4 style='color: #64748b; margin: 0.5rem 0 1.5rem 0;'>Semantic Score</h4>
            <h1 style='font-size: 3.5rem; color: #10b981; margin: 0;'>{semantic:.0f}%</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='pro-card'>
            <div style='font-size: 3.5rem; margin-bottom: 1rem;'>🔍</div>
            <h4 style='color: #64748b; margin: 0.5rem 0 1.5rem 0;'>Keyword Score</h4>
            <h1 style='font-size: 3.5rem; color: #f59e0b; margin: 0;'>{keyword:.0f}%</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='pro-card'>
            <div style='font-size: 3.5rem; margin-bottom: 1rem;'>🎯</div>
            <h4 style='color: #64748b; margin: 0.5rem 0 1.5rem 0;'>Final ATS Score</h4>
            <h1 style='font-size: 3.5rem; color: #ef4444; margin: 0;'>{final:.0f}%</h1>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### **ATS Pass Rate**")
        st.progress(final / 100)
    with col2:
        st.markdown(f"**{int(final)}%**")
    
    quality = analyze_quality(st.session_state.resume_text)
    col1, col2 = st.columns(2)
    col1.metric("📝 Resume Quality", f"{quality['quantification_score']:.1f}%")
    col2.metric("📄 Word Count", f"{quality['word_count']:,}")

# ======================================================
# SKILL ANALYSIS
# ======================================================
elif menu == "Skills":
    st.markdown("## 🎯 **Skill Gap Analysis**")
    
    resume_clean = clean_text(st.session_state.resume_text)
    jd_clean = clean_text(st.session_state.jd_text)
    
    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)
    
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    
    skill_match_percent = skill_match_score(resume_skills, jd_skills)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown(f"### ✅ **Matched Skills** ({len(matched)})")
        if matched:
            for skill in matched[:15]:
                st.success(f"• **{skill}**")
        else:
            st.warning("No matching skills found")
    
    with col2:
        st.markdown(f"### ❌ **Missing Skills** ({len(missing)})")
        if missing:
            for skill in missing[:15]:
                st.error(f"• **{skill}**")
        else:
            st.success("🎉 All skills present!")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.metric("🎯 Skill Match", f"{skill_match_percent:.1f}%")
    col2.metric("📊 Resume Quality", f"{analyze_quality(st.session_state.resume_text)['quantification_score']:.1f}%")

# ======================================================
# SCORE BREAKDOWN
# ======================================================
elif menu == "Breakdown":
    st.markdown("## 📈 **Detailed Score Breakdown**")
    
    semantic, keyword, final = st.session_state.scores
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🤖 Semantic", f"{semantic:.1f}%")
    col2.metric("🔍 Keywords", f"{keyword:.1f}%")
    col3.metric("🎯 Final Score", f"{final:.1f}%")
    
    if 'score_breakdown_chart' in globals():
        score_breakdown_chart(semantic, keyword, final)

# ======================================================
# INSIGHTS
# ======================================================
elif menu == "Insights":
    st.markdown("## 💡 **Resume Section Analysis**")
    
    sections = extract_sections(st.session_state.resume_text)
    
    for section_name, content in sections.items():
        with st.expander(f"📋 **{section_name.upper()}**"):
            if content:
                st.write(content[:800] + "..." if len(content) > 800 else content)
            else:
                st.warning("⚠️ No content detected")

# ======================================================
# EXPORT REPORT
# ======================================================
elif menu == "Export":
    st.markdown("## 📄 **Professional PDF Report**")
    
    semantic, keyword, final = st.session_state.scores
    quality = analyze_quality(st.session_state.resume_text)
    
    st.info("✅ **Report includes:** All scores, skill analysis, quality metrics & recommendations")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🎯 Final Score", f"{final:.1f}%")
    col2.metric("📝 Word Count", quality["word_count"])
    col3.metric("✨ Quality Score", f"{quality['quantification_score']:.1f}%")
    
    if st.button("🎯 **GENERATE & DOWNLOAD PDF**", type="primary", use_container_width=True):
        with st.spinner("📊 Creating professional report..."):
            generate_pdf_report({
                "semantic": semantic,
                "keyword": keyword,
                "final": final,
                "word_count": quality["word_count"]
            })

# ======================================================
# ORIGINAL PROFESSIONAL FOOTER - EXACT COPY
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
