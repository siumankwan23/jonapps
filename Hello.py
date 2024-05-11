import streamlit as st

st.set_page_config(
    page_title="Job Hunt",
    page_icon="👋",
)

st.write("# Welcome to JobApp! 👋")

st.sidebar.success("Select a tool above.")

st.markdown(
    """
    In the contemporary job market, resumes submitted for each job posting undergo initial pre-screening, scoring, and ranking by HR systems. These processes enable recruiters to swiftly identify the most qualified candidates to advance to the next stage in the hiring process. Consequently, it is crucial to craft your resume with the pertinent information to distinguish yourself. This website is designed to bridge the disparity between your resume and the job description, aiding you in standing out from the crowd by providing a tailored cover letter.
    """
)
