import streamlit as st
from resume_utils import analyze_resume
import openai
import os

# Set your OpenAI API key here or use secrets in Streamlit Cloud
openai.api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Job Application Helper AI", layout="wide")
st.title("🤖 Job Application Helper AI")
st.markdown("Improve your CV based on a job description using AI")

resume = st.text_area("✍️ Paste your Resume (or CV) Text Here:", height=250)
job_desc = st.text_area("📌 Paste the Job Description Here:", height=250)

if st.button("Analyze Match"):
    if resume and job_desc:
        match_score, missing_keywords, suggestions = analyze_resume(resume, job_desc)

        # Use OpenAI to generate improvement tips
        prompt = f"""
        I am applying for the following job:
        {job_desc}

        Here is my resume:
        {resume}

        Based on this, how can I improve my resume to better match the job?
        Give me bullet-point suggestions and be concise.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert career advisor."},
                    {"role": "user", "content": prompt}
                ]
            )
            ai_tips = response.choices[0].message.content
        except Exception as e:
            ai_tips = f"GEMINI API error: {e}"

        st.subheader(f"✅ Match Score: {match_score:.1f}%")
        st.write("---")
        st.subheader("❌ Missing Keywords:")
        st.write(", ".join(missing_keywords) if missing_keywords else "All relevant keywords are present.")

        st.subheader("💡 Suggestions Based on Keywords:")
        st.write(suggestions)

        st.subheader("🤖 AI-Powered Improvement Tips:")
        st.write(ai_tips)
    else:
        st.warning("Please paste both your resume and the job description.")
