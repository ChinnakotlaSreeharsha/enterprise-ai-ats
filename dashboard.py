# ======================================================
# ENTERPRISE AI ATS - EXECUTIVE DASHBOARD
# Pure components.html — zero Streamlit dark widgets
# ======================================================

import streamlit as st
import streamlit.components.v1 as components


def hiring_classification(score):
    if score >= 85:
        return "High Confidence Hire", "#16a34a", "rgba(22,163,74,0.08)", "#86efac"
    elif score >= 70:
        return "Strong Potential Candidate", "#1a4fc8", "rgba(26,79,200,0.08)", "#93c5fd"
    elif score >= 55:
        return "Moderate Fit – Needs Optimization", "#d97706", "rgba(217,119,6,0.08)", "#fcd34d"
    else:
        return "High Rejection Risk", "#c8401a", "rgba(200,64,26,0.08)", "#fca5a5"


def render_dashboard(semantic, keyword, final, skill_score=None, quality_score=None, sections=None):

    semantic    = float(semantic)
    keyword     = float(keyword)
    final       = float(final)
    skill_val   = float(skill_score)   if skill_score   is not None else None
    quality_val = float(quality_score) if quality_score is not None else None

    classification, cl_color, cl_bg, cl_border = hiring_classification(final)

    skill_display   = f"{skill_val:.0f}%"   if skill_val   is not None else "N/A"
    quality_display = f"{quality_val:.0f}%" if quality_val is not None else "N/A"

    pct = final / 100

    # Progress bar colour
    if final >= 70:   pb = "#16a34a"
    elif final >= 55: pb = "#d97706"
    else:             pb = "#c8401a"

    # Section rows
    sec_html = ""
    if sections:
        for name, content in sections.items():
            ok     = bool(content)
            dc     = "#16a34a" if ok else "#c8401a"
            label  = "Present" if ok else "Missing"
            rowbg  = "rgba(22,163,74,0.04)" if ok else "rgba(200,64,26,0.04)"
            sec_html += f"""
            <div style="display:flex;justify-content:space-between;align-items:center;
                        padding:0.55rem 0.9rem;border-bottom:1px solid rgba(30,26,22,0.06);
                        background:{rowbg};">
                <span style="font-size:0.83rem;font-weight:600;color:#3c3631;
                             text-transform:capitalize;">{name}</span>
                <span style="display:flex;align-items:center;gap:6px;font-size:0.70rem;
                             font-weight:800;letter-spacing:0.10em;color:{dc};">
                    <span style="width:7px;height:7px;border-radius:50%;
                                 background:{dc};display:inline-block;"></span>{label}
                </span>
            </div>"""

    # Risks
    risks = []
    if semantic < 60:  risks.append("Low contextual alignment with job description.")
    if keyword  < 60:  risks.append("Insufficient keyword optimization for ATS filters.")
    if skill_val  is not None and skill_val  < 60: risks.append("Skill coverage does not sufficiently match job requirements.")
    if quality_val is not None and quality_val < 50: risks.append("Resume lacks quantified achievements or optimal structure.")
    if not risks: risks.append("No major structural or alignment risks detected.")

    risk_html = "".join(f"""
        <div style="display:flex;gap:0.65rem;align-items:flex-start;
                    padding:0.5rem 0;border-bottom:1px solid rgba(30,26,22,0.06);">
            <span style="color:#c8401a;font-size:0.9rem;flex-shrink:0;margin-top:2px;">▸</span>
            <span style="font-size:0.84rem;color:#5a4a40;line-height:1.6;">{r}</span>
        </div>""" for r in risks)

    # Recommendations
    recs = []
    if keyword  < 75: recs.append("Integrate more role-specific keywords naturally within experience section.")
    if semantic < 75: recs.append("Rephrase responsibilities to better mirror job description context.")
    if skill_val  is not None and skill_val  < 75: recs.append("Add missing required skills explicitly in skills section.")
    if quality_val is not None and quality_val < 60: recs.append("Include measurable achievements (%, numbers, impact metrics).")
    if not recs: recs.append("Resume is strategically aligned. Minor refinements may enhance competitiveness.")

    rec_html = "".join(f"""
        <div style="display:flex;gap:0.65rem;align-items:flex-start;
                    padding:0.5rem 0;border-bottom:1px solid rgba(30,26,22,0.06);">
            <span style="color:#1a4fc8;font-size:0.9rem;flex-shrink:0;margin-top:2px;">→</span>
            <span style="font-size:0.84rem;color:#5a4a40;line-height:1.6;">{r}</span>
        </div>""" for r in recs)

    sec_panel = f"""
    <div class="panel">
        <div class="ph"><span class="ptag">Structure</span>
            <span class="ptitle">Section Completeness Matrix</span></div>
        <div style="padding:0;">{sec_html}</div>
    </div>""" if sections else ""

    components.html(f"""<!DOCTYPE html><html><head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    body{{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;color:#1e1a16;}}
    .panel{{background:#fdfcf7;border:1px solid rgba(30,26,22,0.10);margin-bottom:1.1rem;overflow:hidden;}}
    .ph{{display:flex;align-items:center;gap:0.55rem;padding:0.7rem 1.1rem;
         border-bottom:1px solid rgba(30,26,22,0.08);background:#f5f2ea;}}
    .ptag{{font-size:0.56rem;font-weight:800;letter-spacing:0.18em;text-transform:uppercase;
           color:#c8401a;border:1px solid rgba(200,64,26,0.35);padding:2px 8px;
           background:rgba(200,64,26,0.04);}}
    .ptitle{{font-family:'Playfair Display',serif;font-size:0.95rem;font-weight:700;
             color:#1e1a16;letter-spacing:-0.01em;}}
    .pb{{padding:1.1rem;}}
    .score-big{{font-family:'Playfair Display',serif;font-size:4rem;font-weight:900;
                color:#1e1a16;line-height:1;letter-spacing:-0.03em;}}
    .lbl{{font-size:0.60rem;font-weight:800;letter-spacing:0.16em;text-transform:uppercase;color:#9a8e84;margin-bottom:3px;}}
    .prog{{height:5px;background:rgba(30,26,22,0.08);margin-top:0.9rem;}}
    .pf{{height:100%;background:{pb};width:{pct*100:.1f}%;}}
    .grid4{{display:grid;grid-template-columns:repeat(4,1fr);gap:0.85rem;}}
    .mc{{background:#f8f6f1;border:1px solid rgba(30,26,22,0.09);
         border-left:3px solid #1a4fc8;padding:0.8rem 0.9rem;
         transition:border-left-color 0.2s;}}
    .mc:hover{{border-left-color:#c8401a;}}
    .mv{{font-family:'Playfair Display',serif;font-size:1.55rem;font-weight:900;
         color:#1e1a16;letter-spacing:-0.02em;line-height:1;margin-bottom:3px;}}
    .ml{{font-size:0.58rem;font-weight:800;letter-spacing:0.13em;text-transform:uppercase;color:#9a8e84;}}
    </style></head><body>

    <!-- PRIMARY SCORE -->
    <div class="panel">
        <div class="ph"><span class="ptag">ATS Score</span>
            <span class="ptitle">Candidate Performance Overview</span></div>
        <div class="pb">
            <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:1rem;">
                <div>
                    <div class="lbl">Final ATS Score</div>
                    <div class="score-big">{final:.0f}<span style="font-size:2rem;color:#9a8e84;">%</span></div>
                </div>
                <div style="text-align:right;">
                    <div class="lbl">Hiring Classification</div>
                    <div style="display:inline-block;font-size:0.82rem;font-weight:800;
                                letter-spacing:0.05em;padding:7px 16px;
                                border:1.5px solid {cl_border};color:{cl_color};
                                background:{cl_bg};">{classification}</div>
                </div>
            </div>
            <div class="prog"><div class="pf"></div></div>
        </div>
    </div>

    <!-- SCORE ARCHITECTURE -->
    <div class="panel">
        <div class="ph"><span class="ptag">Architecture</span>
            <span class="ptitle">Score Breakdown</span></div>
        <div class="pb">
            <div class="grid4">
                <div class="mc"><div class="mv">{semantic:.0f}%</div><div class="ml">Semantic Alignment</div></div>
                <div class="mc"><div class="mv">{keyword:.0f}%</div><div class="ml">Keyword Relevance</div></div>
                <div class="mc"><div class="mv">{skill_display}</div><div class="ml">Skill Match</div></div>
                <div class="mc"><div class="mv">{quality_display}</div><div class="ml">Resume Quality</div></div>
            </div>
        </div>
    </div>

    <!-- SECTION COMPLETENESS -->
    {sec_panel}

    <!-- RISK ASSESSMENT -->
    <div class="panel">
        <div class="ph"><span class="ptag">Risk</span>
            <span class="ptitle">Risk Assessment</span></div>
        <div class="pb">{risk_html}</div>
    </div>

    <!-- OPTIMIZATION ROADMAP -->
    <div class="panel">
        <div class="ph"><span class="ptag">Roadmap</span>
            <span class="ptitle">Optimization Roadmap</span></div>
        <div class="pb">{rec_html}</div>
    </div>

    </body></html>""", height=1020, scrolling=True)