from flask import Flask,request ,render_template
import os
import PyPDF2
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# helper_functions
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in reader.pages:
            text += page.extract_text(page)
        return test    
    
def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = file.read()
    
def extract_text(file_path):
    if file_name.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_name.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_name.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file format")
     
@app.route("/")
def matchresume():
    return render_template("matchresume.html")

@app.route("/matchresume", methods=['GET', 'POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume = request.form['resume']

        resumes = []
        for resume_file in resume_files:
           filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
           resume_file.save(filename)
           resumes.append(extract_text(filename))

        if not resumes and not job_description:
            return render_template("matchresume.html", error="Please provide a job description or upload at least one resume.") 
        
        vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
        vectors = vectorizer.toarray()
        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity([job_vector], resume_vectors)[0]

        top_indices = similarities.argsort()[-5:][::-1]
        top_resumes = [resumes[i] for i in top_indices]
        similarity_scores = [round(similarities[i], 2) for i in top_indices]  

        return render_template("matchresume.html", message="Top matching resumes:")
    
    return render_template("matchresume.html")
        

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        port = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=port)