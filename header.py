# ======================================================
# ATS SAAS 2.1 HEADER
# CLEAN FIXED HEADER
# ======================================================

import streamlit as st


def load_header(initialized=False):

    status_text = "System Ready" if initialized else "Awaiting Analysis"
    status_color = "#10b981" if initialized else "#f59e0b"

    st.markdown("""
    <style>

    header[data-testid="stHeader"] {
        display: none;
    }

    .block-container {
        padding-top: 0rem !important;
    }

    .main-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 85px;
        background: #0b1220;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 40px;
        z-index: 10000;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        color: white;
        font-family: Inter, sans-serif;
    }

    .header-title {
        font-size: 1.2rem;
        font-weight: 600;
    }

    .status-badge {
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="main-header">
        <div class="header-title">Enterprise AI ATS</div>
        <div class="status-badge" style="background:{status_color}20; color:{status_color};">
            {status_text}
        </div>
    </div>
    """, unsafe_allow_html=True)
