import streamlit as st
from streamlit_extras.buy_me_a_coffee import button

st.set_page_config(
    page_title="Job Hunt",
    page_icon="👋",
)

st.write("# Welcome to JobApp! 👋")
st.write("Siumankwan23@gmail.com")
st.write("Support Me")
button(username="siumankwan23", floating=False, width=221)
st.sidebar.success("Select a tool above.")

st.markdown(
    """
 In the contemporary job market, resumes submitted for each job posting undergo initial pre-screening, scoring, and ranking by HR systems. These processes enable recruiters to swiftly identify the most qualified candidates to advance to the next stage in the hiring process. Consequently, it is crucial to craft your resume with the pertinent information to distinguish yourself. This website is designed to bridge the disparity between your resume and the job description, aiding you in standing out from the crowd by providing a tailored cover letter. After getting past the initial screening, use the interview helper to train for the interview.
    - Applying for a job(https://skjobapps.streamlit.app/Applying)
    - Interviewing for a job(https://skjobapps.streamlit.app/Interviewing)
    """
)
