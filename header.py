# ======================================================
# ENTERPRISE AI ATS — HEADER
# Professional light-mode — 2026
# ======================================================

import streamlit as st
import streamlit.components.v1 as components


def load_header(initialized=False):

    status_text  = "SYSTEM ACTIVE"        if initialized else "READY TO ANALYZE"
    status_color = "#16a34a"              if initialized else "#c8401a"
    status_bg    = "rgba(22,163,74,0.10)" if initialized else "rgba(200,64,26,0.08)"
    status_border= "#86efac"              if initialized else "#c8401a"

    # ══════════════════════════════════════════════════
    # GLOBAL CSS — force warm parchment light theme
    # ══════════════════════════════════════════════════
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700;1,900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* ── Force warm light background throughout ── */
    html, body,
    .stApp, .stApp > div,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section,
    section.main, section.main > div,
    .block-container,
    .st-emotion-cache-13ln4jf,
    .st-emotion-cache-yw8pof {
        background-color: #f5f2ea !important;
        color: #1e1a16 !important;
        background-image: none !important;
    }

    .block-container {
        padding-top: 0 !important;
        max-width: 100% !important;
        padding-left: 2.5rem !important;
        padding-right: 2.5rem !important;
    }

    /* Hide Streamlit chrome */
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu, footer { visibility: hidden !important; }

    /* ── Typography ── */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif !important;
        color: #1e1a16 !important;
        font-weight: 900 !important;
        letter-spacing: -0.01em !important;
    }
    p, span, div, label, li, a {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #3c3631 !important;
    }

    /* ── Metric cards ── */
    div[data-testid="stMetric"] {
        background: #fdfcf7 !important;
        border: 1px solid rgba(30,26,22,0.10) !important;
        border-left: 4px solid #1a4fc8 !important;
        border-radius: 0 !important;
        padding: 1.3rem 1.4rem !important;
        transition: transform 0.22s, box-shadow 0.22s, border-left-color 0.22s !important;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border-left-color: #c8401a !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.07);
    }
    div[data-testid="stMetricValue"] {
        color: #1e1a16 !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 900 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #7a7065 !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
    }

    /* ── Tabs ── */
    div[data-baseweb="tab-list"] {
        background: #f0ece3 !important;
        border-bottom: 2px solid rgba(30,26,22,0.11) !important;
        gap: 0 !important;
    }
    button[data-baseweb="tab"] {
        background: transparent !important;
        color: #7a7065 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.76rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        border-radius: 0 !important;
        border-bottom: 2px solid transparent !important;
        padding: 0.75rem 1.25rem !important;
        transition: color 0.2s, border-color 0.2s !important;
    }
    button[data-baseweb="tab"]:hover {
        color: #1e1a16 !important;
        background: rgba(30,26,22,0.04) !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background: #fdfcf7 !important;
        color: #c8401a !important;
        border-bottom: 2px solid #c8401a !important;
        font-weight: 800 !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: #1e1a16 !important;
        color: #f5f2ea !important;
        border: 2px solid #1e1a16 !important;
        border-radius: 0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.76rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.10em !important;
        text-transform: uppercase !important;
        transition: background 0.2s, border-color 0.2s, transform 0.15s !important;
    }
    .stButton > button:hover {
        background: #c8401a !important;
        border-color: #c8401a !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(200,64,26,0.20) !important;
    }
    .stButton > button[kind="primary"] {
        background: #c8401a !important;
        border-color: #c8401a !important;
        color: #fff !important;
    }
    .stButton > button[kind="primary"]:hover {
        background: #a83415 !important;
        border-color: #a83415 !important;
    }

    .stDownloadButton > button {
        background: #15803d !important;
        border-color: #15803d !important;
        color: #fff !important;
        border-radius: 0 !important;
    }
    .stDownloadButton > button:hover {
        background: #166534 !important;
        border-color: #166534 !important;
    }

    /* ── Divider ── */
    hr { border-color: rgba(30,26,22,0.10) !important; }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #f0ece3; }
    ::-webkit-scrollbar-thumb { background: #c4b8a8; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #8a8070; }

    /* ── Progress bar ── */
    div[data-testid="stProgress"] > div {
        background: #c8401a !important;
    }

    /* ── Alerts ── */
    div[data-testid="stAlert"] {
        border-radius: 0 !important;
        border-left-width: 4px !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════
    # FIXED HEADER BAR — Variant C Editorial Masthead
    # ══════════════════════════════════════════════════
    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
    *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ background:transparent; overflow:hidden; font-family:'Plus Jakarta Sans',sans-serif; }}

    /* ── Outer fixed bar ── */
    .hdr {{
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 68px;
        background: #fdfcf7;
        border-bottom: 1px solid rgba(30,26,22,0.11);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0;
        box-shadow: 0 2px 16px rgba(30,26,22,0.06);
        z-index: 9999;
        overflow: hidden;
    }}

    /* ════════════════════════════════════
       LEFT — Variant C Editorial Masthead
    ════════════════════════════════════ */
    .brand {{
        display: flex;
        align-items: stretch;
        height: 100%;
        flex-shrink: 0;
    }}

    /* 5px gradient spine — red → blue → amber */
    .brand-spine {{
        width: 5px;
        height: 100%;
        background: linear-gradient(180deg, #c8401a 0%, #1a4fc8 55%, #d97706 100%);
        flex-shrink: 0;
    }}

    /* Brand body — hover tint */
    .brand-body {{
        display: flex;
        align-items: center;
        padding: 0 1.5rem 0 1.1rem;
        gap: 1rem;
        height: 100%;
        border-right: 1px solid rgba(30,26,22,0.09);
        transition: background 0.22s ease;
        cursor: default;
    }}
    .brand-body:hover {{
        background: rgba(200,64,26,0.04);
    }}

    /* "Sree" wordmark — big, serif, italic ee */
    .brand-wordmark {{
        font-family: 'Playfair Display', serif;
        font-size: 1.9rem;
        font-weight: 900;
        color: #1e1a16;
        letter-spacing: -0.03em;
        line-height: 1;
        white-space: nowrap;
        user-select: none;
    }}
    .brand-wordmark em {{
        color: #c8401a;
        font-style: italic;
        transition: color 0.22s ease;
    }}
    .brand-body:hover .brand-wordmark em {{
        color: #a83415;
    }}

    /* Hairline divider between wordmark and meta */
    .brand-divider {{
        width: 1px;
        height: 1.9rem;
        background: rgba(30,26,22,0.13);
        flex-shrink: 0;
    }}

    /* Platform + tagline stack */
    .brand-meta {{
        display: flex;
        flex-direction: column;
        gap: 4px;
    }}
    .brand-platform {{
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #1e1a16;
        line-height: 1;
        white-space: nowrap;
    }}
    .brand-tagline {{
        font-size: 0.56rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #9a8e84;
        line-height: 1;
        border-left: 2px solid #1a4fc8;
        padding-left: 0.45rem;
        white-space: nowrap;
    }}

    /* ════════════════════════════════════
       CENTER — decorative diamond rule
    ════════════════════════════════════ */
    .hdr-center {{
        flex: 1;
        display: flex;
        align-items: center;
        gap: 7px;
        padding: 0 2rem;
        opacity: 0.5;
        pointer-events: none;
    }}
    .hc-line    {{ flex: 1; height: 1px; background: rgba(30,26,22,0.10); }}
    .hc-diamond {{
        width: 5px; height: 5px;
        background: #c8401a;
        transform: rotate(45deg);
        flex-shrink: 0;
        opacity: 0.7;
    }}

    /* ════════════════════════════════════
       RIGHT — status badges
    ════════════════════════════════════ */
    .hdr-right {{
        display: flex;
        align-items: center;
        gap: 0.55rem;
        padding-right: 2rem;
        flex-shrink: 0;
    }}

    .badge {{
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 6px 13px;
        font-size: 0.60rem;
        font-weight: 800;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        border: 1.5px solid;
        white-space: nowrap;
        transition: transform 0.18s ease, box-shadow 0.18s ease;
        cursor: default;
    }}
    .badge:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(30,26,22,0.08);
    }}
    .badge-year {{
        border-color: rgba(30,26,22,0.14);
        color: #8a8070;
        background: #f5f2ea;
        font-family: 'Playfair Display', serif;
        font-size: 0.82rem;
        font-weight: 700;
        font-style: italic;
        letter-spacing: 0.04em;
        text-transform: none;
    }}
    .badge-ai {{
        border-color: #1a4fc8;
        color: #1a4fc8;
        background: rgba(26,79,200,0.07);
    }}
    .badge-status {{
        border-color: {status_border};
        color: {status_color};
        background: {status_bg};
    }}

    .dot {{
        width: 7px; height: 7px;
        border-radius: 50%;
        flex-shrink: 0;
    }}
    .dot-ai     {{ background: #1a4fc8; animation: pulse 2.4s ease-in-out infinite; }}
    .dot-status {{ background: {status_color}; }}

    @keyframes pulse {{
        0%,100% {{ opacity:1; transform:scale(1); }}
        50%      {{ opacity:0.25; transform:scale(1.8); }}
    }}

    /* ── 3-colour accent strip pinned below header ── */
    .hdr-strip {{
        position: fixed;
        top: 68px; left: 0; right: 0;
        height: 3px;
        display: flex;
        z-index: 9998;
    }}
    .s1 {{ flex: 4; background: #c8401a; }}
    .s2 {{ flex: 2; background: #1a4fc8; }}
    .s3 {{ flex: 1; background: #d97706; }}
    .s4 {{ flex: 1; background: #16a34a; }}
    </style>
    </head>
    <body>

    <div class="hdr">

        <!-- ── LEFT: Editorial Masthead Brand ── -->
        <div class="brand">
            <div class="brand-spine"></div>
            <div class="brand-body">
                <div class="brand-wordmark">Sr<em>ee</em></div>
                <div class="brand-divider"></div>
                <div class="brand-meta">
                    <div class="brand-platform">Enterprise AI ATS</div>
                    <div class="brand-tagline">Resume Intelligence</div>
                </div>
            </div>
        </div>

        <!-- ── CENTER: decorative rule ── -->
        <div class="hdr-center">
            <div class="hc-line"></div>
            <div class="hc-diamond"></div>
            <div class="hc-line"></div>
        </div>

        <!-- ── RIGHT: badges ── -->
        <div class="hdr-right">
            <div class="badge badge-year">2026</div>
            <div class="badge badge-ai">
                <div class="dot dot-ai"></div>
                AI Powered
            </div>
            <div class="badge badge-status">
                <div class="dot dot-status"></div>
                {status_text}
            </div>
        </div>

    </div>

    <!-- 3-px colour strip pinned below header -->
    <div class="hdr-strip">
        <div class="s1"></div>
        <div class="s2"></div>
        <div class="s3"></div>
        <div class="s4"></div>
    </div>

    </body>
    </html>
    """, height=71, scrolling=False)
