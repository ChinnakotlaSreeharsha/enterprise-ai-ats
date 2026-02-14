# ======================================================
# UPLOAD PAGE - ATS ANALYSIS MODULE
# ======================================================

import streamlit as st
import PyPDF2

from ats_engine import compute_scores


def render_upload_page():

    st.title("Resume Upload & ATS Analysis")

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    with col2:
        jd_text = st.text_area("Paste Job Description", height=220)

    if st.button("Run ATS Analysis", type="primary"):

        if resume_file and jd_text.strip():

            try:
                reader = PyPDF2.PdfReader(resume_file)
            except Exception:
                st.error("Invalid or corrupted PDF file.")
                st.stop()

            text = ""
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text() + " "

            semantic, keyword, final = compute_scores(text, jd_text)

            st.session_state.resume_text = text
            st.session_state.jd_text = jd_text
            st.session_state.scores = (semantic, keyword, final)
            st.session_state.initialized = True

            st.success("Analysis Completed Successfully ✔")

        else:
            st.error("Both resume and job description are required.")
