import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def extract_keywords(text):
    words = clean_text(text).split()
    return set(words)

def analyze_resume(resume_text, job_text):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    # TF-IDF Similarity
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume_clean, job_clean])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

    # Keyword comparison
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)
    missing_keywords = list(job_keywords - resume_keywords)

    # Suggestions
    suggestions = "Consider including the following terms in your CV to better match the job: " +         ", ".join(missing_keywords[:10]) if missing_keywords else "Your resume aligns well with the job description."

    return score, missing_keywords, suggestions
