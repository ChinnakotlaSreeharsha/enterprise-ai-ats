# ======================================================
# SKILLS MODULE
# Logic + UI Combined (Lean Architecture)
# ======================================================

import re
import streamlit as st
from config import SKILL_KEYWORDS


# ------------------------------------------------------
# SKILL EXTRACTION LOGIC
# ------------------------------------------------------

def extract_skills(text):
    if not text:
        return []

    text = text.lower()
    found = []

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found.append(skill)

    return sorted(list(set(found)))


def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0.0

    matched = set(resume_skills) & set(jd_skills)
    score = (len(matched) / len(jd_skills)) * 100

    return float(max(0.0, min(score, 100.0)))


# ------------------------------------------------------
# UI RENDERING
# ------------------------------------------------------

def render_skills_page(resume_text, jd_text):

    st.title("Skill Alignment Intelligence")

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    skill_score = skill_match_score(resume_skills, jd_skills)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

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
    </style>
    """, unsafe_allow_html=True)

    # ---------------- Skill Score ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Overall Skill Match</div>', unsafe_allow_html=True)

    st.metric("Skill Match Score", f"{skill_score:.1f}%")
    st.progress(skill_score / 100)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- Matched vs Missing ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Aligned Skills</div>', unsafe_allow_html=True)

        if matched:
            for skill in matched:
                st.write(f"• {skill}")
        else:
            st.write("No matching skills identified.")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Missing Required Skills</div>', unsafe_allow_html=True)

        if missing:
            for skill in missing:
                st.write(f"• {skill}")
        else:
            st.write("All required skills appear to be covered.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- Guidance ----------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Optimization Guidance</div>', unsafe_allow_html=True)

    if skill_score < 60:
        st.write("Significant skill gap detected. Add required competencies explicitly.")
    elif skill_score < 80:
        st.write("Moderate alignment. Minor skill additions could improve competitiveness.")
    else:
        st.write("Strong skill alignment. Resume demonstrates relevant capability coverage.")

    st.markdown('</div>', unsafe_allow_html=True)
