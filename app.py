from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from model import extract_skills, match_jobs

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    skills = extract_skills(filepath)
    jobs, score = match_jobs(skills)

    return render_template('result.html', jobs=jobs, score=score)

if __name__ == '__main__':
    app.run(debug=True)
