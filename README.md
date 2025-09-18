# AI Resume Analyzer

📃 **AI Resume Analyzer** is a Streamlit web app that provides instant feedback on resumes using AI. Upload your resume (PDF or TXT), optionally provide the job position you’re applying for, and get structured feedback on content, skills, and experience presentation.

---

## Features

- Analyze resumes and provide constructive feedback.
- Supports PDF and TXT resume uploads.
- Optional job position input for targeted suggestions.
- Built with Python, Streamlit, and AI (OpenAI GPT or Google Gemini).

---

## Demo

You can run the app locally to test AI resume analysis.
Or you can go here: https://ai-resume-critique-vv2zeswzm4n3dqor26et6n.streamlit.app/
This will only show you how it functions and not provide actual results due to how OpenAI works.

---

## Requirements

- Python 3.8+
- Streamlit
- PyPDF2
- requests
- python-dotenv

---

## Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

2. Create a virtual environment
```
python -m venv venv
# Activate it:
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Get API and Use
```
#Windows (PowerShell):
$env:OPENAI_API_KEY="your_api_key_here"
streamlit run main.py

#Mac/Linux (bash/zsh):
export OPENAI_API_KEY="your_api_key_here"
streamlit run main.py
```
