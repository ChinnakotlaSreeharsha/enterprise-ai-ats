# ======================================================
# SECTION ANALYZER - ADVANCED VERSION
# Intelligent Resume Section Extraction
# ======================================================

import re


SECTION_PATTERNS = {
    "skills": r"(skills|technical skills|core competencies)",
    "experience": r"(experience|work experience|professional experience|employment)",
    "education": r"(education|academic background|qualification)",
    "projects": r"(projects|academic projects|research|personal projects)"
}


def extract_sections(text):
    """
    Extract structured resume sections using flexible header detection.
    """

    if not text:
        return {key: "" for key in SECTION_PATTERNS}

    sections = {key: "" for key in SECTION_PATTERNS}
    text_lower = text.lower()

    for section_name, pattern in SECTION_PATTERNS.items():

        regex = rf"{pattern}.*?(?=\n[A-Z][^\n]+\n|\Z)"
        match = re.search(regex, text_lower, re.DOTALL)

        if match:
            sections[section_name] = match.group().strip()

    return sections
