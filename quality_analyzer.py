# quality_analyzer.py

def analyze_quality(text):
    word_count = len(text.split())
    numbers_count = sum(c.isdigit() for c in text)

    score = 0

    if 400 <= word_count <= 900:
        score += 40

    if numbers_count > 10:
        score += 30

    if "%" in text:
        score += 30

    return {
        "word_count": word_count,
        "quantification_score": score
    }
