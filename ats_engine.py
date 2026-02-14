# ======================================================
# ATS ENGINE - ENTERPRISE SAFE VERSION
# Stable | Normalized | Crash-Proof | Optimized
# ======================================================

import re
import nltk
import streamlit as st

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from config import SEMANTIC_WEIGHT, KEYWORD_WEIGHT


# ------------------------------------------------------
# SAFE NLTK INITIALIZATION
# ------------------------------------------------------

@st.cache_resource
def load_nltk_resources():
    nltk.download("stopwords", quiet=True)
    nltk.download("wordnet", quiet=True)
    nltk.download("omw-1.4", quiet=True)
    return set(stopwords.words("english")), WordNetLemmatizer()


stop_words, lemmatizer = load_nltk_resources()


# ------------------------------------------------------
# CACHE SENTENCE TRANSFORMER MODEL
# ------------------------------------------------------

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


# ------------------------------------------------------
# TEXT CLEANING
# ------------------------------------------------------

def clean_text(text):
    if not text:
        return ""

    text = re.sub(r"[^a-zA-Z\s]", " ", text).lower()
    words = text.split()

    cleaned_words = []
    for w in words:
        if w not in stop_words and len(w) > 2:
            try:
                cleaned_words.append(lemmatizer.lemmatize(w))
            except Exception:
                cleaned_words.append(w)

    return " ".join(cleaned_words)


# ------------------------------------------------------
# SAFE SCORE NORMALIZER
# ------------------------------------------------------

def normalize_score(score):
    """
    Ensures score is between 0 and 100
    """
    return max(0.0, min(score, 100.0))


# ------------------------------------------------------
# COMPUTE ATS SCORES
# ------------------------------------------------------

def compute_scores(resume_text, jd_text):

    if not resume_text or not jd_text:
        return 0.0, 0.0, 0.0

    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    # ---------------- TF-IDF KEYWORD SCORE ----------------
    try:
        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform([clean_resume, clean_jd])
        keyword_score = cosine_similarity(
            matrix[0:1], matrix[1:2]
        )[0][0] * 100
    except Exception:
        keyword_score = 0.0

    # ---------------- SEMANTIC SCORE ----------------
    try:
        embeddings = model.encode([resume_text, jd_text])
        semantic_score = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0] * 100
    except Exception:
        semantic_score = 0.0

    # Normalize individual scores
    semantic_score = normalize_score(semantic_score)
    keyword_score = normalize_score(keyword_score)

    # ---------------- FINAL HYBRID SCORE ----------------
    final_score = (
        SEMANTIC_WEIGHT * semantic_score +
        KEYWORD_WEIGHT * keyword_score
    )

    final_score = normalize_score(final_score)

    return semantic_score, keyword_score, final_score
