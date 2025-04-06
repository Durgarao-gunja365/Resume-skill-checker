# ✅ Disable file watching before anything else

# Put this at the very top of your script (main.py or app.py)
import os
os.environ["STREAMLIT_DISABLE_FILE_WATCHING"] = "1"

# Now import torch and others
import torch
import streamlit as st






# ✅ Then import all other libraries

# ... your other imports




from resume_parser import process_resume, extract_skills_from_text

st.set_page_config(page_title="Resume Skill Matcher", layout="centered")
st.title("📄 Resume Skill Matcher")

st.markdown("### 📥 Upload your resume")
uploaded_file = st.file_uploader("Supported formats: PDF, DOCX, TXT", type=["pdf", "docx", "txt"])

st.markdown("### 📝 Paste Job Description")
job_description = st.text_area("Paste the job description below", height=250)

if uploaded_file and job_description:
    # 🔍 Extract skills from job description using NLP
    job_skills_list = extract_skills_from_text(job_description)

    st.markdown("### ✅ Extracted Job Skills")
    if job_skills_list:
        st.write(", ".join(job_skills_list))
    else:
        st.warning("No recognizable skills found in the job description.")

    st.markdown("### 🔍 Resume Analysis Result")
    process_resume(uploaded_file, uploaded_file.name, job_skills_list)
elif not uploaded_file and job_description:
    st.info("Please upload your resume to proceed.")
elif uploaded_file and not job_description:
    st.info("Please paste the job description to extract required skills. To get fast result  press ctr + enter to apply")
