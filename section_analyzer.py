# section_analyzer.py

import re

def extract_sections(text):
    sections = {
        "skills": "",
        "experience": "",
        "education": "",
        "projects": ""
    }

    text_lower = text.lower()

    for key in sections.keys():
        pattern = rf"{key}.*?(?=\n\n|\Z)"
        match = re.search(pattern, text_lower, re.DOTALL)
        if match:
            sections[key] = match.group()

    return sections
