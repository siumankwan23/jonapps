# app.py

from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import requests

import streamlit as st
import os
import openai
import re

llm = ChatOpenAI(api_key="...")
#load_dotenv(find_dotenv())

# Sidebar contents
with st.sidebar:
    st.title('💬 Cover Letter Generator')
    st.markdown('''
    ## About
    This app generates a tailored cover letter based on your resume and a job description using OpenAI.
    ''')

# Main function
def main():
    st.title("Cover Letter Generator")

    # Input boxes for resume and job description
    resume = st.text_area("Paste Your Resume Here:")
    job_description = st.text_area("Paste the Job Description Here:")

    if st.button("Submit"):
        # Prepare prompt for OpenAI
        #prompt = f"Compare the resume with the job description and identify what is missing from the resume. Resume: {resume}. Job Description: {job_description}."

        # Generate response from OpenAI
        response = generate_response(resume, job_description)

        # Extract missing points from the response
        missing_points = extract_missing_points(response)

        # Generate cover letter
        cover_letter = generate_cover_letter(resume, job_description)

        # Display missing points as bullet points
        st.write("### Missing Points from Resume:")
        for point in missing_points:
            st.write(f"- {point}")

        # Display generated cover letter
        st.write("### Generated Cover Letter:")
        st.write(cover_letter[:500])  # Display first 500 characters

def generate_response(resume, job_description):
    
    chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "compare {resume} and {job_description}")
])
    print(chat_prompt)
    return chat_prompt

def extract_missing_points(response):
    # Extract bullet points from the response
    missing_points = re.findall(r"[\*-] (.+)", response)
    return missing_points

def generate_cover_letter(resume, job_description):
    # Concatenate resume and job description for cover letter generation
    combined_text = f"{resume} {job_description}"
    cover_letter = generate_response(combined_text)
    return cover_letter

if __name__ == "__main__":
    main()
