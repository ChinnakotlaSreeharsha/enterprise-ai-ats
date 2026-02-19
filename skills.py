# ======================================================
# SKILLS MODULE — Pure light palette
# ======================================================

import re
import streamlit as st
import streamlit.components.v1 as components
from config import SKILL_KEYWORDS


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
    return float(max(0.0, min((len(matched) / len(jd_skills)) * 100, 100.0)))


def render_skills_page(resume_text, jd_text):

    resume_skills = extract_skills(resume_text)
    jd_skills     = extract_skills(jd_text)
    skill_score   = skill_match_score(resume_skills, jd_skills)
    matched       = sorted(set(resume_skills) & set(jd_skills))
    missing       = sorted(set(jd_skills) - set(resume_skills))

    if skill_score >= 80:
        sc, guidance, gc, gbg, gborder = "#16a34a", "Strong skill alignment. Resume demonstrates relevant capability coverage.", "#16a34a", "rgba(22,163,74,0.07)", "#86efac"
    elif skill_score >= 60:
        sc, guidance, gc, gbg, gborder = "#d97706", "Moderate alignment. Minor skill additions could improve competitiveness.", "#d97706", "rgba(217,119,6,0.07)", "#fcd34d"
    else:
        sc, guidance, gc, gbg, gborder = "#c8401a", "Significant skill gap detected. Add required competencies explicitly.", "#c8401a", "rgba(200,64,26,0.07)", "#fca5a5"

    matched_chips = "".join(
        f'<span style="display:inline-flex;align-items:center;gap:5px;background:rgba(22,163,74,0.09);'
        f'border:1px solid rgba(22,163,74,0.28);color:#15803d;font-size:0.72rem;font-weight:700;'
        f'padding:4px 11px;margin:3px;">'
        f'<span style="width:6px;height:6px;border-radius:50%;background:#16a34a;flex-shrink:0;"></span>{s}</span>'
        for s in matched
    ) or '<span style="color:#9a8e84;font-size:0.84rem;">No matching skills identified.</span>'

    missing_chips = "".join(
        f'<span style="display:inline-flex;align-items:center;gap:5px;background:rgba(200,64,26,0.08);'
        f'border:1px solid rgba(200,64,26,0.26);color:#b91c1c;font-size:0.72rem;font-weight:700;'
        f'padding:4px 11px;margin:3px;">'
        f'<span style="width:6px;height:6px;border-radius:50%;background:#c8401a;flex-shrink:0;"></span>{s}</span>'
        for s in missing
    ) or '<span style="color:#9a8e84;font-size:0.84rem;">All required skills appear covered.</span>'

    pct = skill_score / 100

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
    .two{{display:grid;grid-template-columns:1fr 1fr;gap:1.1rem;margin-bottom:1.1rem;}}
    .prog{{height:5px;background:rgba(30,26,22,0.08);margin-top:0.85rem;}}
    .pf{{height:100%;background:{sc};width:{pct*100:.1f}%;}}
    </style></head><body>

    <!-- SCORE -->
    <div class="panel">
        <div class="ph"><span class="ptag">Match Score</span>
            <span class="ptitle">Overall Skill Alignment</span></div>
        <div class="pb">
            <div style="display:flex;align-items:flex-end;gap:1.25rem;">
                <div style="font-family:'Playfair Display',serif;font-size:3.5rem;
                            font-weight:900;color:{sc};line-height:1;letter-spacing:-0.03em;">
                    {skill_score:.0f}%</div>
                <div style="padding-bottom:0.35rem;">
                    <div style="font-size:0.60rem;font-weight:800;letter-spacing:0.16em;
                                text-transform:uppercase;color:#9a8e84;margin-bottom:4px;">Skill Match Score</div>
                    <div style="font-size:0.82rem;font-weight:600;color:#5a4a40;">
                        {len(matched)} matched &nbsp;·&nbsp; {len(missing)} missing &nbsp;·&nbsp; {len(jd_skills)} required</div>
                </div>
            </div>
            <div class="prog"><div class="pf"></div></div>
        </div>
    </div>

    <!-- MATCHED + MISSING -->
    <div class="two">
        <div class="panel">
            <div class="ph">
                <span style="font-size:0.56rem;font-weight:800;letter-spacing:0.18em;text-transform:uppercase;
                             color:#16a34a;border:1px solid rgba(22,163,74,0.38);padding:2px 8px;
                             background:rgba(22,163,74,0.06);">Aligned</span>
                <span class="ptitle">Matched Skills</span>
            </div>
            <div class="pb" style="display:flex;flex-wrap:wrap;gap:2px;">{matched_chips}</div>
        </div>
        <div class="panel">
            <div class="ph"><span class="ptag">Missing</span>
                <span class="ptitle">Required Skills Gap</span></div>
            <div class="pb" style="display:flex;flex-wrap:wrap;gap:2px;">{missing_chips}</div>
        </div>
    </div>

    <!-- GUIDANCE -->
    <div class="panel">
        <div class="ph"><span class="ptag">Guidance</span>
            <span class="ptitle">Optimization Guidance</span></div>
        <div class="pb">
            <div style="border-left:4px solid {gborder};background:{gbg};padding:0.85rem 1rem;">
                <div style="font-size:0.88rem;color:{gc};font-weight:600;line-height:1.6;">{guidance}</div>
            </div>
        </div>
    </div>

    </body></html>""", height=700, scrolling=True)