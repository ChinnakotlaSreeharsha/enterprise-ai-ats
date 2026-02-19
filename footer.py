# ======================================================
# ENTERPRISE AI ATS — FOOTER (professional light-mode)
# ======================================================

import streamlit as st
import streamlit.components.v1 as components


def load_footer():

    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: transparent; font-family: 'Plus Jakarta Sans', sans-serif; }
    a { text-decoration: none; }

    .ft {
        background: #f8f6f1;
        border-top: 1px solid rgba(30,26,22,0.10);
        padding: 2.8rem 3rem 2.2rem;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        flex-wrap: wrap;
        gap: 2.2rem;
    }
    .ft-name {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 900;
        color: #1e1a16;
        line-height: 1;
        margin-bottom: 6px;
        letter-spacing: -0.015em;
    }
    .ft-name em { color: #c8401a; font-style: italic; }
    .ft-sub { font-size: 0.82rem; color: #7a7065; font-weight: 500; }

    .socials { display: flex; gap: 0.7rem; flex-wrap: wrap; }
    .sb {
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 4px;
        min-width: 70px;
        padding: 0.9rem 0.6rem;
        border: 1.5px solid rgba(30,26,22,0.11);
        background: #fdfcf7;
        transition: all 0.24s ease;
    }
    .sb:hover {
        transform: translateY(-4px);
        border-color: #c8401a;
        background: #fff8f2;
        box-shadow: 0 6px 16px rgba(200,64,26,0.08);
    }
    .ab {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e1a16;
    }
    .lb {
        font-size: 0.60rem;
        font-weight: 800;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        color: #7a7065;
    }

    /* ── Tags strip — clean warm light bar ── */
    .tags {
        background: #f0ece3;
        border-top: 1px solid rgba(30,26,22,0.07);
        border-bottom: 1px solid rgba(30,26,22,0.07);
        padding: 0.85rem 3rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        flex-wrap: wrap;
    }
    .tg {
        font-size: 0.62rem;
        font-weight: 800;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        padding: 4px 12px;
        border: 1px solid rgba(200,64,26,0.30);
        color: #5a4a40;
        background: rgba(200,64,26,0.04);
    }
    .yr {
        font-family: 'Playfair Display', serif;
        font-size: 0.82rem;
        color: #9a8e84;
        margin-left: auto;
    }

    /* ── Bottom bar ── */
    .fb {
        background: #f5f2ea;
        border-top: 1px solid rgba(30,26,22,0.09);
        padding: 2rem 3rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1.6rem;
        color: #4a433b;
    }
    .fb-copy { font-size: 0.76rem; color: #6b6357; }
    .fb-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        font-weight: 900;
        color: #1e1a16;
    }
    .fb-name em { color: #c8401a; }
    .fb-heart {
        font-size: 1.6rem;
        color: #c8401a;
        animation: hb 2s ease-in-out infinite;
    }
    @keyframes hb {
        0%,100% { transform: scale(1); }
        20%     { transform: scale(1.4); }
        40%     { transform: scale(1); }
    }

    @media (max-width: 640px) {
        .ft, .fb { flex-direction: column; align-items: flex-start; padding: 2rem 1.6rem; }
        .tags { padding: 1rem 1.6rem; }
    }
    </style>
    </head>
    <body>

    <div class="ft">
        <div>
            <div class="ft-name">Sree <em>AI</em> ATS</div>
            <div class="ft-sub">Enterprise-Grade Resume Intelligence Platform</div>
        </div>
        <div class="socials">
            <a href="https://www.linkedin.com/in/chinnakotla-sree-harsha-85502620b" target="_blank" class="sb">
                <span class="ab">LI</span><span class="lb">LinkedIn</span>
            </a>
            <a href="https://myportfolio-i3gd.onrender.com/" target="_blank" class="sb">
                <span class="ab">PF</span><span class="lb">Portfolio</span>
            </a>
            <a href="https://github.com/ChinnakotlaSreeharsha" target="_blank" class="sb">
                <span class="ab">GH</span><span class="lb">GitHub</span>
            </a>
            <a href="https://linktr.ee/chinnakotla_sreeharsha" target="_blank" class="sb">
                <span class="ab">LT</span><span class="lb">Linktree</span>
            </a>
        </div>
    </div>

    <div class="tags">
        <span class="tg">ATS Engine</span>
        <span class="tg">Semantic AI</span>
        <span class="tg">Skill Analysis</span>
        <span class="tg">PDF Export</span>
        <span class="tg">Deep Diagnostics</span>
        <span class="yr">2026</span>
    </div>

    <div class="fb">
        <div>
            <div class="fb-copy">All Rights Reserved &middot; 2026</div>
            <div class="fb-name">Crafted by <em>Chinnakotla Sree Harsha</em></div>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:0.62rem; font-weight:800; letter-spacing:0.14em; text-transform:uppercase; color:#7a7065;">Made with</span>
            <span class="fb-heart">&#9829;</span>
        </div>
    </div>

    </body>
    </html>
    """, height=380, scrolling=False)
