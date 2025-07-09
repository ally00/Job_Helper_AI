
# 🤖 Job Application Helper AI

This is a Streamlit-based AI agent that helps job seekers analyze their resume (CV) against a specific job description and provides:
- A match score using keyword comparison
- Missing keywords to improve targeting
- AI-powered resume improvement suggestions using OpenAI GPT

## 🚀 Features
- Text input for resume and job description
- Keyword similarity scoring using TF-IDF
- Natural language suggestions powered by GPT-3.5-Turbo

## 📂 Project Structure
```
job-helper-ai/
├── app.py                  # Main Streamlit app
├── resume_utils.py         # Core logic for scoring & suggestions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## 📦 Installation & Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🔑 GEMINI API Key
Create a `.streamlit/secrets.toml` file or set an environment variable:
```toml
[general]
OPENAI_API_KEY="your-api-key"
```

## 🌐 Deploy on Streamlit Cloud
1. Push this project to GitHub
2. Connect repo to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your GEMINI key to `secrets`

---

Created with ❤️ by Ally Manzi
