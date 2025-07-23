import os
import nltk
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pdfminer.high_level import extract_text
from docx import Document

nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_file(path):
    if path.endswith('.pdf'):
        return extract_text(path)
    elif path.endswith('.docx'):
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

def extract_skills(path):
    text = extract_text_from_file(path).lower()
    words = word_tokenize(text)
    filtered = [w for w in words if w.isalpha() and w not in stopwords.words('english')]
    # Sample skill list
    skills = ['python', 'sql', 'excel', 'javascript', 'html', 'css', 'machine learning']
    found = [skill for skill in skills if skill in filtered]
    return found

def match_jobs(user_skills):
    with open('job_descriptions.json') as f:
        job_data = json.load(f)

    matched_jobs = []
    max_score = 0

    for job in job_data:
        job_skills = job['skills']
        match_count = len(set(user_skills) & set(job_skills))
        score = (match_count / len(job_skills)) * 100
        if score > max_score:
            max_score = score
        if match_count > 0:
            matched_jobs.append(job)

    return matched_jobs, round(max_score, 2)
