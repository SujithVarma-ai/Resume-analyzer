# Resume Analyzer (AI Project)

A web application that analyzes and ranks resumes based on a given job description using NLP techniques.

## Features

* Upload multiple resumes (PDF/DOCX)
* Extracts text automatically
* Compares resumes with job description
* Ranks resumes using cosine similarity (TF-IDF)

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

## How It Works

* Extracts text from resumes (PDF/DOCX)
* Converts text into numerical vectors using TF-IDF
* Calculates similarity using cosine similarity
* Ranks resumes based on match score

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

* Add user authentication
* Improve UI/UX
* Add support for more file formats
* Deploy with Docker for scalability
