# skill_engine.py

import re
from config import SKILL_KEYWORDS

def extract_skills(text):
    found = []
    for skill in SKILL_KEYWORDS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)
    return list(set(found))

def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    return (len(set(resume_skills) & set(jd_skills)) / len(jd_skills)) * 100
