import streamlit as st
import PyPDF2 
import os 
import io
from openai import OpenAI
from dotenv import load_dotenv

##loads envirionment from the .env file (the AI api key)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

##To run the streamlit, remember to do: "uv run streamlit run main.py (or whatever name the file is)" because uv is used
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📃", layout="centered")

st.title("AI Resume Analyzer")
st.markdown("Upload your resume and get instant feedback powered by AI!")

uploaded_file = st.file_uploader("Choose a PDF/TXT file", type=["pdf", "txt"])
position = st.text_input("Enter the job position you are applying for (optional)")
analyze_button = st.button("Analyze Resume")

def extract_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_from_file(file):
    if file.type == "application/pdf":
        return extract_from_pdf(io.BytesIO(file.read()))
    return file.read().decode("utf-8")

if analyze_button and uploaded_file:
    try:
        file_content = extract_from_file(uploaded_file)

        if not file_content.strip(): 
            st.error("The uploaded file is empty or could not be read")
            st.stop()
        prompt = f"""Please analyze the following resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience description
        4. Specific imporovements for the position: {position if position else 'general job application'}
        Resume Content:
        {file_content}
        Provide your feedback in a clear and structured manner."""

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are a helpful and expert resume reviewer with years of experience in HR and recruitment that provides resume feedback."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature= 0.5
        )
        st.markdown("### Resume Analysis Feedback")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
    