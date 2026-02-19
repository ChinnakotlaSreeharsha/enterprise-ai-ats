# ======================================================
# ENTERPRISE AI ATS — APP CORE
# ======================================================

import streamlit as st
import streamlit.components.v1 as components
import time

from header import load_header
from footer import load_footer
from upload import render_upload_page
from dashboard import render_dashboard
from skills import render_skills_page
from diagnostics import render_diagnostics

from ats_engine import clean_text
from analytics import (
    score_breakdown_chart, radar_chart,
    skill_gap_chart, recruiter_readiness
)
from report_generator import generate_pdf_report
from section_analyzer import extract_sections
from quality_analyzer import analyze_quality


def generate_executive_summary(semantic, keyword, skill, quality, readiness):
    for v in [semantic, keyword, skill, quality, readiness]:
        v = float(max(0, min(v, 100)))
    readiness = float(max(0, min(readiness, 100)))
    semantic  = float(max(0, min(semantic,  100)))
    keyword   = float(max(0, min(keyword,   100)))
    skill     = float(max(0, min(skill,     100)))
    quality   = float(max(0, min(quality,   100)))

    if readiness >= 85:
        tier, verdict = "ELITE CANDIDATE", "Exceptional hiring potential with strong market positioning."
        color, bg, border = "#16a34a", "#f0fdf4", "#86efac"
    elif readiness >= 70:
        tier, verdict = "STRONG CANDIDATE", "High potential with a competitive professional profile."
        color, bg, border = "#1a4fc8", "#eff6ff", "#93c5fd"
    elif readiness >= 55:
        tier, verdict = "MODERATE FIT", "Solid foundation with clear optimization opportunities."
        color, bg, border = "#d97706", "#fffbeb", "#fcd34d"
    else:
        tier, verdict = "REQUIRES ENHANCEMENT", "Significant optimization needed for competitive positioning."
        color, bg, border = "#c8401a", "#fff7f5", "#fca5a5"

    return dict(tier=tier, verdict=verdict, color=color, bg=bg, border=border,
                semantic=semantic, keyword=keyword, skill=skill,
                quality=quality, readiness=readiness)


# ── Page config ────────────────────────────────────────
st.set_page_config(
    page_title="Sree AI ATS — Enterprise Resume Intelligence",
    layout="wide", page_icon="⚡",
    initial_sidebar_state="collapsed",
)

# ── Session state ──────────────────────────────────────
for k, v in [("initialized", False), ("generated_pdf", None),
             ("show_export_modal", False), ("download_complete", False)]:
    if k not in st.session_state:
        st.session_state[k] = v

# ── Header (injects global CSS) ────────────────────────
load_header(st.session_state.initialized)

# ══════════════════════════════════════════════════════
# NUCLEAR DARK-MODE KILL — overrides ALL remaining dark
# Streamlit widget defaults not covered by header.py
# ══════════════════════════════════════════════════════
st.markdown("""
<style>
/* ── st.title / st.header rendered as dark text ── */
h1, h2, h3 {
    color: #1e1a16 !important;
    font-family: 'Playfair Display', serif !important;
}

/* ── st.metric — force light ── */
[data-testid="stMetric"] {
    background: #fdfcf7 !important;
    border: 1px solid rgba(30,26,22,0.10) !important;
    border-left: 4px solid #1a4fc8 !important;
    border-radius: 0 !important;
    padding: 1.1rem 1.2rem !important;
}
[data-testid="stMetricValue"] > div,
[data-testid="stMetricValue"] {
    color: #1e1a16 !important;
    font-family: 'Playfair Display', serif !important;
    font-weight: 900 !important;
}
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] > div {
    color: #7a7065 !important;
    font-size: 0.70rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}
[data-testid="stMetricDelta"] {
    color: #16a34a !important;
}

/* ── st.progress ── */
[data-testid="stProgressBar"] > div,
[data-testid="stProgress"] > div,
div[role="progressbar"] > div {
    background: #c8401a !important;
}
[data-testid="stProgress"],
[data-testid="stProgressBar"] {
    background: rgba(30,26,22,0.08) !important;
    border-radius: 0 !important;
}

/* ── Sliders ── */
[data-testid="stSlider"] {
    background: transparent !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: #c8401a !important;
    border-color: #c8401a !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] div[class*="track"] {
    background: rgba(30,26,22,0.12) !important;
}
[data-testid="stSlider"] label {
    color: #5a4a40 !important;
    font-weight: 700 !important;
    font-size: 0.78rem !important;
}

/* ── Plotly charts: kill dark container bg ── */
.js-plotly-plot, .plotly, .plot-container {
    background: #fdfcf7 !important;
}
.stPlotlyChart {
    background: #fdfcf7 !important;
    border: 1px solid rgba(30,26,22,0.09) !important;
}

/* ── Dialog / modal ── */
[data-testid="stModal"],
[data-testid="stModal"] > div,
[data-baseweb="modal"],
[data-baseweb="modal"] > div,
[data-baseweb="dialog"],
[data-baseweb="dialog"] > div,
div[role="dialog"],
div[role="dialog"] > div {
    background: #fdfcf7 !important;
    background-color: #fdfcf7 !important;
    color: #1e1a16 !important;
    border-radius: 0 !important;
}
/* Modal header */
[data-testid="stModal"] header,
div[role="dialog"] header {
    background: #f5f2ea !important;
    border-bottom: 1px solid rgba(30,26,22,0.10) !important;
    color: #1e1a16 !important;
    font-family: 'Playfair Display', serif !important;
    font-weight: 700 !important;
}
/* Modal overlay backdrop */
[data-baseweb="modal"] ~ div,
div[data-baseweb="layer"] > div:first-child {
    background: rgba(30,26,22,0.45) !important;
}

/* ── Success / info / warning / error alerts ── */
[data-testid="stAlert"] {
    background: #fdfcf7 !important;
    border-radius: 0 !important;
    border-left-width: 4px !important;
    color: #1e1a16 !important;
}
[data-testid="stAlert"] p,
[data-testid="stAlert"] div {
    color: #1e1a16 !important;
}

/* ── st.spinner ── */
[data-testid="stSpinner"] > div {
    border-top-color: #c8401a !important;
}

/* ── Dividers ── */
hr { border-color: rgba(30,26,22,0.10) !important; }

/* ── Any stray dark backgrounds from old .card CSS ── */
div[class*="card"] {
    background: #fdfcf7 !important;
    border-radius: 0 !important;
    color: #1e1a16 !important;
}

/* ── Columns background ── */
[data-testid="column"] {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ── Welcome banner ─────────────────────────────────────
if not st.session_state.initialized:
    components.html("""<!DOCTYPE html><html><head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
    <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    body{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;}
    .hero{background:#f8f6f1;border:1px solid rgba(30,26,22,0.09);border-left:5px solid #c8401a;
          padding:3.5rem 3rem 3rem;position:relative;overflow:hidden;
          animation:fadeUp 0.5s ease-out both;}
    @keyframes fadeUp{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:translateY(0);}}
    .wm{position:absolute;right:-0.04em;top:-0.08em;font-family:'Playfair Display',serif;
        font-size:clamp(7rem,18vw,15rem);font-weight:900;color:transparent;
        -webkit-text-stroke:1px rgba(30,26,22,0.04);pointer-events:none;
        line-height:1;user-select:none;letter-spacing:-0.02em;}
    .tag{display:inline-block;font-size:0.62rem;font-weight:800;letter-spacing:0.18em;
         text-transform:uppercase;color:#c8401a;border:1px solid #c8401a;
         padding:3px 10px;margin-bottom:1.2rem;background:rgba(200,64,26,0.04);}
    .hl{font-family:'Playfair Display',serif;font-size:clamp(2.4rem,5.5vw,5rem);
        font-weight:900;line-height:1.0;letter-spacing:-0.02em;color:#1e1a16;margin-bottom:1.1rem;}
    .hl-accent{color:#c8401a;} .hl-sub{color:rgba(30,26,22,0.35);font-style:italic;}
    .sub{font-size:1rem;color:#7a7065;max-width:52ch;line-height:1.7;
         font-weight:400;margin-bottom:2rem;}
    .bars{display:flex;gap:6px;} .b{height:4px;border-radius:2px;}
    </style></head><body>
    <div class="hero">
        <div class="wm">ATS</div>
        <div class="tag">Enterprise Platform &mdash; 2026</div>
        <div class="hl">Welcome to<br>
            <span class="hl-accent">Sree</span>
            <em class="hl-sub">&#8202;AI&#8202;</em>&nbsp;ATS</div>
        <div class="sub">Enterprise-grade resume intelligence powered by advanced AI.
            Upload your resume and job description to unlock professional insights.</div>
        <div class="bars">
            <div class="b" style="width:56px;background:#c8401a;"></div>
            <div class="b" style="width:38px;background:#1a4fc8;"></div>
            <div class="b" style="width:22px;background:#d97706;"></div>
            <div class="b" style="width:14px;background:#16a34a;"></div>
        </div>
    </div></body></html>""", height=340, scrolling=False)


# ── Tabs ───────────────────────────────────────────────
tab_upload, tab_dashboard, tab_skills, tab_analytics, tab_diagnostics, tab_export = st.tabs([
    "📤 Upload", "📊 Dashboard", "🎯 Skills",
    "📈 Analytics", "🔍 Diagnostics", "📄 Export"
])
with tab_upload:
    render_upload_page()


def render_locked():
    components.html("""<!DOCTYPE html><html><head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,700&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    body{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;}
    .lk{text-align:center;padding:4rem 2rem;background:#f8f6f1;
        border:1px solid rgba(26,23,19,0.09);border-top:4px solid #d97706;}
    .lk-tag{display:inline-block;font-size:0.60rem;font-weight:800;
            letter-spacing:0.18em;text-transform:uppercase;color:#d97706;
            border:1px solid #d97706;padding:3px 12px;margin-bottom:1.1rem;
            background:rgba(217,119,6,0.05);}
    .lk-h{font-family:'Playfair Display',serif;font-size:2.6rem;font-weight:900;
          letter-spacing:-0.02em;color:#1e1a16;margin-bottom:0.75rem;}
    .lk-h em{color:#d97706;font-style:italic;}
    .lk-p{color:#7a7065;font-size:0.95rem;font-weight:500;}
    .lk-p strong{color:#3a332c;}
    </style></head><body>
    <div class="lk">
        <div class="lk-tag">Access Restricted</div>
        <div class="lk-h">Section <em>Locked</em></div>
        <div class="lk-p">Upload a resume in the <strong>Upload</strong> tab to unlock this section.</div>
    </div></body></html>""", height=280, scrolling=False)


def section_head(tag, title, em_word, sub):
    st.markdown(
        f'<div style="display:inline-block;font-family:\'Plus Jakarta Sans\',sans-serif;'
        f'font-size:0.63rem;font-weight:800;letter-spacing:0.18em;text-transform:uppercase;'
        f'color:#c8401a;border:1px solid #c8401a;padding:3px 10px;margin-bottom:0.6rem;'
        f'background:rgba(200,64,26,0.04);">{tag}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-family:\'Playfair Display\',serif;font-size:2.3rem;font-weight:900;'
        f'color:#1e1a16;line-height:1.05;letter-spacing:-0.02em;margin:0 0 0.2rem;">'
        f'{title} <em style="color:#c8401a;font-style:italic;">{em_word}</em></div>',
        unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-family:\'Plus Jakarta Sans\',sans-serif;font-size:0.86rem;'
        f'color:#7a7065;font-weight:500;margin-bottom:1.75rem;'
        f'border-left:3px solid #1a4fc8;padding-left:0.7rem;">{sub}</div>',
        unsafe_allow_html=True)


def accent_label(text, color="#1a4fc8"):
    st.markdown(
        f'<div style="font-family:\'Plus Jakarta Sans\',sans-serif;font-size:0.66rem;'
        f'font-weight:800;letter-spacing:0.14em;text-transform:uppercase;color:{color};'
        f'margin-bottom:0.9rem;border-left:3px solid {color};padding-left:0.65rem;">'
        f'{text}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════

if not st.session_state.initialized:
    for _t in [tab_dashboard, tab_skills, tab_analytics, tab_diagnostics, tab_export]:
        with _t:
            render_locked()

else:
    semantic, keyword, final = map(float, st.session_state.scores)
    semantic = max(0.0, min(semantic, 100.0))
    keyword  = max(0.0, min(keyword,  100.0))
    final    = max(0.0, min(final,    100.0))

    resume_text  = st.session_state.resume_text
    jd_text      = st.session_state.jd_text
    resume_clean = clean_text(resume_text)
    jd_clean     = clean_text(jd_text)

    quality_data = analyze_quality(resume_text)
    sections     = extract_sections(resume_text)

    from skills import extract_skills, skill_match_score
    resume_skills = extract_skills(resume_clean)
    jd_skills     = extract_skills(jd_clean)
    skill_score   = skill_match_score(resume_skills, jd_skills)

    # ── DASHBOARD ──────────────────────────────────────
    with tab_dashboard:
        section_head("Overview", "Executive", "Dashboard",
                     "Comprehensive ATS performance overview")
        ph = st.empty()
        for i in range(int(final) + 1):
            ph.metric("Final ATS Score", f"{i}%",
                      delta=f"+{i-50}%" if i > 50 else None)
            time.sleep(0.002)
        st.markdown("<br>", unsafe_allow_html=True)
        render_dashboard(semantic, keyword, final,
                         skill_score=skill_score,
                         quality_score=quality_data["quality_score"],
                         sections=sections)

    # ── SKILLS ─────────────────────────────────────────
    with tab_skills:
        section_head("Skills Intelligence", "Skills", "Analysis",
                     "Detailed skill matching and gap analysis")
        render_skills_page(resume_clean, jd_clean)

    # ── ANALYTICS ──────────────────────────────────────
    with tab_analytics:
        section_head("Deep Analysis", "Advanced", "Analytics",
                     "Interactive recruiter simulation and performance insights")

        accent_label("Recruiter Weight Simulation", "#1a4fc8")
        col1, col2, col3, col4 = st.columns(4)
        weights = {
            "semantic": col1.slider("Semantic", 0.0, 1.0, 0.35, key="sem_s"),
            "keyword":  col2.slider("Keyword",  0.0, 1.0, 0.30, key="key_s"),
            "skill":    col3.slider("Skill",    0.0, 1.0, 0.20, key="ski_s"),
            "quality":  col4.slider("Quality",  0.0, 1.0, 0.15, key="qua_s"),
        }
        total = sum(weights.values())
        if total > 0:
            for k in weights: weights[k] /= total

        readiness = float(max(0, min(
            recruiter_readiness(semantic, keyword, skill_score,
                                quality_data["quality_score"], weights), 100)))

        st.markdown("<br>", unsafe_allow_html=True)
        ca, cb = st.columns([2, 1])
        with ca: st.metric("Simulated Recruiter Score", f"{readiness:.1f}%")
        with cb: st.progress(readiness / 100)

        st.divider()
        c1, c2 = st.columns(2)
        with c1: st.plotly_chart(score_breakdown_chart(semantic, keyword, final),
                                 use_container_width=True)
        with c2: st.plotly_chart(radar_chart({
            "Semantic": semantic, "Keyword": keyword,
            "Skill": skill_score, "Quality": quality_data["quality_score"]
        }), use_container_width=True)

        st.divider()
        st.plotly_chart(skill_gap_chart(
            len(set(resume_skills) & set(jd_skills)),
            len(set(jd_skills) - set(resume_skills))
        ), use_container_width=True)
        st.divider()

        accent_label("AI Executive Summary", "#c8401a")
        s = generate_executive_summary(semantic, keyword, skill_score,
                                       quality_data["quality_score"], readiness)
        components.html(f"""<!DOCTYPE html><html><head>
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
        <style>
        *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
        body{{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;}}
        .card{{background:{s['bg']};border:1px solid {s['border']};
               border-left:5px solid {s['color']};padding:1.5rem 1.75rem;}}
        .tier{{font-size:0.62rem;font-weight:800;letter-spacing:0.18em;
               text-transform:uppercase;color:{s['color']};margin-bottom:0.6rem;}}
        .verdict{{font-family:'Playfair Display',serif;font-size:1.45rem;font-weight:700;
                  color:#1e1a16;margin-bottom:0.65rem;line-height:1.2;}}
        .stats{{font-size:0.83rem;color:#5a5248;line-height:1.8;}}
        .stats strong{{color:#1e1a16;font-weight:700;}}
        .sl{{margin-top:0.5rem;font-size:0.9rem;font-weight:800;color:{s['color']};}}
        </style></head><body>
        <div class="card">
            <div class="tier">{s['tier']}</div>
            <div class="verdict">{s['verdict']}</div>
            <div class="stats">
                Semantic: <strong>{s['semantic']:.1f}%</strong> &nbsp;&bull;&nbsp;
                Keyword: <strong>{s['keyword']:.1f}%</strong> &nbsp;&bull;&nbsp;
                Skills: <strong>{s['skill']:.1f}%</strong> &nbsp;&bull;&nbsp;
                Quality: <strong>{s['quality']:.1f}%</strong>
                <div class="sl">Recruiter Score: {s['readiness']:.1f}%</div>
            </div>
        </div></body></html>""", height=190, scrolling=False)

    # ── DIAGNOSTICS ────────────────────────────────────
    with tab_diagnostics:
        section_head("Structural Audit", "Deep", "Diagnostics",
                     "Comprehensive resume structure and quality analysis")
        render_diagnostics(sections=sections, quality_data=quality_data,
                           keyword_score=keyword)

    # ── EXPORT ─────────────────────────────────────────
    with tab_export:
        section_head("Report Generator", "Professional", "Export",
                     "Generate and download your comprehensive ATS intelligence report")

        components.html(f"""<!DOCTYPE html><html><head>
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
        <style>
        *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
        body{{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;}}
        .ec{{background:#fdfcf7;border:1px solid rgba(30,26,22,0.10);
             border-left:5px solid #1a4fc8;padding:1.4rem 1.6rem;
             display:flex;justify-content:space-between;align-items:center;
             flex-wrap:wrap;gap:1.25rem;margin-bottom:1rem;}}
        .et{{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:900;
             color:#1e1a16;letter-spacing:-0.01em;margin-bottom:4px;}}
        .es{{font-size:0.78rem;color:#7a7065;font-weight:500;}}
        .sr{{display:flex;gap:1rem;flex-wrap:wrap;}}
        .st{{text-align:center;padding:0.6rem 1rem;background:#f5f2ea;
             border:1px solid rgba(30,26,22,0.09);}}
        .sv{{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:900;color:#1e1a16;}}
        .sl{{font-size:0.56rem;font-weight:800;letter-spacing:0.14em;
             text-transform:uppercase;color:#9a8e84;}}
        </style></head><body>
        <div class="ec">
            <div>
                <div class="et">ATS Intelligence Report</div>
                <div class="es">Comprehensive PDF — scores, skill analysis, diagnostics &amp; recommendations.</div>
            </div>
            <div class="sr">
                <div class="st"><div class="sv">{final:.0f}%</div><div class="sl">ATS Score</div></div>
                <div class="st"><div class="sv">{skill_score:.0f}%</div><div class="sl">Skill Match</div></div>
                <div class="st"><div class="sv">{quality_data["quality_score"]:.0f}%</div><div class="sl">Quality</div></div>
            </div>
        </div></body></html>""", height=140, scrolling=False)

        _, cc, _ = st.columns([1, 2, 1])
        with cc:
            if st.button("Generate Professional PDF Report",
                         use_container_width=True, type="primary"):
                with st.spinner("Generating your professional report…"):
                    pdf_bytes = generate_pdf_report({
                        "semantic":       semantic,
                        "keyword":        keyword,
                        "final":          final,
                        "skill_score":    skill_score,
                        "quality_score":  quality_data["quality_score"],
                        "word_count":     quality_data["word_count"],
                        "matched_skills": list(set(resume_skills) & set(jd_skills)),
                        "missing_skills": list(set(jd_skills) - set(resume_skills)),
                        "sections":       sections,
                        "readiness":      readiness,
                    })
                    if pdf_bytes:
                        st.session_state.generated_pdf     = pdf_bytes
                        st.session_state.show_export_modal = True
                        st.session_state.download_complete = False

        if st.session_state.show_export_modal:
            @st.dialog("Report Generated Successfully", width="large")
            def export_modal():
                ph2 = st.empty()
                for i in range(101):
                    ph2.progress(i / 100, text=f"Processing… {i}%")
                    time.sleep(0.01)
                st.success("Your professional ATS intelligence report is ready!")
                st.download_button(
                    label="Download PDF Report",
                    data=st.session_state.generated_pdf,
                    file_name="Sree_ATS_Professional_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True, type="primary",
                    on_click=lambda: st.session_state.update(download_complete=True)
                )
                if st.session_state.download_complete:
                    st.balloons()
                    st.info("Download initiated successfully!")
                    time.sleep(2)
                    st.session_state.show_export_modal = False
                    st.session_state.download_complete = False
                    st.rerun()
                if st.button("Close", use_container_width=True):
                    st.session_state.show_export_modal = False
                    st.rerun()
            export_modal()


# ── Footer ─────────────────────────────────────────────
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
load_footer()