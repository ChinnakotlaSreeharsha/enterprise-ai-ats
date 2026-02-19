# ======================================================
# UPLOAD PAGE - ATS ANALYSIS MODULE
# ======================================================

import streamlit as st
import PyPDF2

from ats_engine import compute_scores


def render_upload_page():

    # ── Deep CSS overrides — target every Streamlit internal layer ──
    st.markdown("""
    <style>
    /* ══════════════════════════════════════════
       FILE UPLOADER — nuke all dark backgrounds
    ══════════════════════════════════════════ */

    /* Outer wrapper */
    [data-testid="stFileUploader"] {
        background: #fdfcf7 !important;
        border: 1.5px dashed rgba(200,64,26,0.30) !important;
        border-radius: 0 !important;
        padding: 0.3rem !important;
        transition: border-color 0.2s ease;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #c8401a !important;
    }

    /* The inner dark dropzone div — every known selector */
    [data-testid="stFileUploader"] section,
    [data-testid="stFileUploader"] section > div,
    [data-testid="stFileUploadDropzone"],
    [data-testid="stFileUploadDropzone"] > div,
    [data-baseweb="file-uploader"],
    [data-baseweb="file-uploader"] > div,
    div[class*="uploadedFile"],
    div[class*="fileUploader"],
    div[class*="dropzone"],
    [data-testid="stFileUploader"] > div,
    [data-testid="stFileUploader"] > div > div,
    [data-testid="stFileUploader"] > div > div > div {
        background: #fdfcf7 !important;
        background-color: #fdfcf7 !important;
        border: none !important;
        border-radius: 0 !important;
    }

    /* Force all text inside uploader to be dark */
    [data-testid="stFileUploader"] *,
    [data-testid="stFileUploadDropzone"] * {
        color: #5a4a40 !important;
        background-color: transparent !important;
    }

    /* Re-apply background only to the section wrapper */
    [data-testid="stFileUploader"] section {
        background: #fdfcf7 !important;
        padding: 0.6rem 0.8rem !important;
    }

    /* Cloud upload icon — terracotta */
    [data-testid="stFileUploader"] svg,
    [data-testid="stFileUploadDropzone"] svg {
        fill: #c8401a !important;
        color: #c8401a !important;
        opacity: 0.75;
    }

    /* "Drag and drop" text */
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploadDropzone"] span,
    [data-testid="stFileUploadDropzone"] small {
        color: #7a7065 !important;
        background: transparent !important;
    }

    /* Browse files button */
    [data-testid="stFileUploader"] button,
    [data-testid="stFileUploadDropzone"] button {
        background: #f0ece3 !important;
        background-color: #f0ece3 !important;
        color: #1e1a16 !important;
        border: 1.5px solid rgba(30,26,22,0.18) !important;
        border-radius: 0 !important;
        font-weight: 800 !important;
        font-size: 0.76rem !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }
    [data-testid="stFileUploader"] button:hover,
    [data-testid="stFileUploadDropzone"] button:hover {
        background: #fff8f2 !important;
        background-color: #fff8f2 !important;
        border-color: #c8401a !important;
        color: #c8401a !important;
    }

    /* ══════════════════════════════════════════
       LABELS
    ══════════════════════════════════════════ */
    [data-testid="stFileUploader"] label,
    [data-testid="stTextArea"] label {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.70rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.16em !important;
        text-transform: uppercase !important;
        color: #5a4a40 !important;
        margin-bottom: 0.5rem !important;
        background: transparent !important;
    }

    /* ══════════════════════════════════════════
       TEXTAREA
    ══════════════════════════════════════════ */
    [data-testid="stTextArea"] textarea {
        background: #fdfcf7 !important;
        background-color: #fdfcf7 !important;
        border: 1.5px solid rgba(30,26,22,0.12) !important;
        border-radius: 0 !important;
        color: #1e1a16 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.9rem !important;
        line-height: 1.65 !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
        resize: vertical;
    }
    [data-testid="stTextArea"] textarea:focus {
        border-color: #c8401a !important;
        box-shadow: 0 0 0 3px rgba(200,64,26,0.08) !important;
        outline: none !important;
    }
    [data-testid="stTextArea"] textarea::placeholder {
        color: #b0a898 !important;
    }
    /* Textarea wrapper bg */
    [data-testid="stTextArea"] > div,
    [data-testid="stTextArea"] > div > div {
        background: transparent !important;
        border-radius: 0 !important;
    }

    /* ══════════════════════════════════════════
       PRIMARY BUTTON
    ══════════════════════════════════════════ */
    [data-testid="stButton"] button[kind="primary"] {
        background: #c8401a !important;
        color: #fff !important;
        border: none !important;
        border-radius: 0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.76rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        padding: 0.75rem 2.2rem !important;
        transition: background 0.2s ease, transform 0.15s ease, box-shadow 0.15s ease;
    }
    [data-testid="stButton"] button[kind="primary"]:hover {
        background: #a83415 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(200,64,26,0.25) !important;
    }

    /* ══════════════════════════════════════════
       ALERTS
    ══════════════════════════════════════════ */
    [data-testid="stAlert"] {
        border-radius: 0 !important;
        border-left-width: 4px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── Page heading ──
    import streamlit.components.v1 as components
    components.html("""
    <!DOCTYPE html><html><head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
    <style>
    *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
    body { background:transparent; font-family:'Plus Jakarta Sans',sans-serif; }
    .uh {
        padding: 0 0 1.6rem 0;
        border-bottom: 1px solid rgba(30,26,22,0.08);
        margin-bottom: 0.4rem;
    }
    .uh-tag {
        display: inline-block;
        font-size: 0.62rem; font-weight: 800;
        letter-spacing: 0.18em; text-transform: uppercase;
        color: #c8401a; border: 1px solid #c8401a;
        padding: 3px 10px; margin-bottom: 0.9rem;
        background: rgba(200,64,26,0.04);
    }
    .uh-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 4vw, 3.2rem);
        font-weight: 900;
        color: #1e1a16;
        letter-spacing: -0.02em;
        line-height: 1.05;
        margin-bottom: 0.5rem;
    }
    .uh-title em { color: #c8401a; font-style: italic; }
    .uh-sub {
        font-size: 0.88rem;
        color: #7a7065;
        font-weight: 500;
        line-height: 1.6;
        border-left: 3px solid #1a4fc8;
        padding-left: 0.7rem;
        max-width: 56ch;
    }
    </style>
    </head><body>
    <div class="uh">
        <div class="uh-tag">Step 01 &mdash; Input</div>
        <div class="uh-title">Resume Upload &amp; <em>ATS</em> Analysis</div>
        <div class="uh-sub">Upload your resume PDF and paste the target job description to begin the intelligence analysis.</div>
    </div>
    </body></html>
    """, height=170, scrolling=False)

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    with col2:
        jd_text = st.text_area(
            "Paste Job Description",
            height=220,
            placeholder="Paste the full job description here…"
        )

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

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