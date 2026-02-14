# ======================================================
# QUALITY ANALYZER - ENTERPRISE VERSION
# Quantification + Structure + Length Evaluation
# ======================================================

def analyze_quality(text):
    """
    Analyzes resume quality based on:
    - Word count
    - Use of numbers (quantification)
    - Presence of percentages
    Returns normalized score out of 100.
    """

    if not text:
        return {
            "word_count": 0,
            "numbers_count": 0,
            "percentage_mentions": 0,
            "quality_score": 0.0
        }

    word_count = len(text.split())
    numbers_count = sum(c.isdigit() for c in text)
    percentage_mentions = text.count("%")

    score = 0

    # Ideal word count
    if 400 <= word_count <= 900:
        score += 40
    elif 300 <= word_count < 400 or 900 < word_count <= 1100:
        score += 20

    # Quantified achievements
    if numbers_count > 10:
        score += 30
    elif numbers_count > 5:
        score += 15

    # Percentage usage
    if percentage_mentions > 0:
        score += 30

    # Clamp score
    score = max(0, min(score, 100))

    return {
        "word_count": word_count,
        "numbers_count": numbers_count,
        "percentage_mentions": percentage_mentions,
        "quality_score": float(score)
    }
