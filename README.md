# AI Resume Analyzer using NLP (TF-IDF + Cosine Similarity)

> Automatically ranks resumes based on a job description using Natural Language Processing techniques

## Features

* Upload multiple resumes (PDF/DOCX)
* Automatic text extraction from files
* Compares resumes with job description
* Ranks resumes using cosine similarity
* Displays match scores for each resume

## Tech Stack

* Python
* Flask
* Scikit-learn
* PyPDF2
* docx2txt

## Live Demo

👉 https://resume-analyzer-pyte.onrender.com

## Screenshot

![App Screenshot](https://raw.githubusercontent.com/SujithVarma-ai/Resume-analyzer/main/Screenshot%202026-03-25%20004455.png)

## Sample Output

* Resume 1 → 85% match
* Resume 2 → 72% match
* Resume 3 → 60% match

## How It Works

* Extracts text from resumes (PDF/DOCX)
* Converts text into numerical vectors using TF-IDF
* Calculates similarity using cosine similarity
* Ranks resumes based on similarity score

## Project Structure

* app.py → main backend logic
* templates/ → frontend HTML
* requirements.txt → dependencies

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Future Improvements

* Add user authentication system
* Improve UI/UX design
* Add visualization for scores (charts/graphs)
* Support more file formats
* Deploy with Docker for scalability

