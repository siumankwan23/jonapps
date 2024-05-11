# app.py

#from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
#from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import OpenAI

#import requests

import streamlit as st
import os
#import openai
#import re
 
api_key = os.environ["OPENAI_API_KEY"]
print("test")
print(api_key)
llm = ChatOpenAI(api_key=api_key)
#load_dotenv(find_dotenv())

# Sidebar contents
with st.sidebar:
    st.title('💬 Resume Helper and Cover Letter Generator')
    st.markdown('''
                ''')

# Main function
def main():
    
    st.title("Job applicant helper\n 1. Generate missing requirements in the resume\n 2. Generate missing important keywords\n 3. Generate cover letter")
    
    # Input boxes for resume and job description
    col1, col2 = st.columns(2)
    with col1:
        resume = st.text_area("Paste Your Resume Here:", height=400)

    with col2:
        job_description = st.text_area("Paste the Job Description Here:", height=400)
    # Input boxes for resume and job description

    if st.button("Submit"):
        # Prepare prompt for OpenAI
        #prompt = f"Compare the resume with the job description and identify what is missing from the resume. Resume: {resume}. Job Description: {job_description}."

        # Generate response from OpenAI
        response = generate_response(resume, job_description)
        
        keyword = keywords(resume, job_description)
        # Generate cover letter
        cover_letter = generate_cover_letter(resume, job_description)

        # Display missing points as bullet points
        st.write("### Gap in the resume for the job posting:")
        for point in response:
            st.write(f"{point}")

        # Display missing points as bullet points
        st.write("### A list of keywords you should include:")
        for kpoint in keyword:
            st.write(f"{kpoint}")
            
        # Display generated cover letter
        st.write("### Generated Cover Letter:")
        #st.write(cover_letter[:500])  # Display first 500 characters
        st.write(f"{cover_letter}")  # Display first 500 characters
        
def generate_response(resume, job_description):
    
        # Prepare prompt for OpenAI
    prompt = f"my resume is \n{resume}.\n\n the job description is \n{job_description}.\n\n tell me what should I add to my resume to match the job description in bullet point format."
    
    # Generate response from OpenAI
    response = llm.invoke(prompt)
    #chat_prompt = ChatPromptTemplate.from_messages([
    #("system", "You are a world class technical documentation writer."),
    #("user", "compare {resume} and {job_description}")
#])
    #response = llm.ask(chat_prompt)
    print(response)
    
    # Extract content from the response data
    content = response.content

    # Split the content into a list of missing points based on newline characters
    response = content.split('\n')
    return response

def keywords(resume, job_description):
    
        # Prepare prompt for OpenAI
    prompt = f"my resume is \n{resume}.\n\n the job description is \n{job_description}.\n\n tell me a list of single keywords that is required for the job and missing in the resume in bullet point format."
    
    # Generate response from OpenAI
    response = llm.invoke(prompt)
    #chat_prompt = ChatPromptTemplate.from_messages([
    #("system", "You are a world class technical documentation writer."),
    #("user", "compare {resume} and {job_description}")
#])
    #response = llm.ask(chat_prompt)
    print(response)
    
    # Extract content from the response data
    content = response.content

    # Split the content into a list of missing points based on newline characters
    keyword = content.split('\n')
    
    return keyword

def generate_cover_letter(resume, job_description):
        
    # Prepare prompt for OpenAI
    prompt = f"my resume is \n{resume}.\n\n the job description is \n{job_description}.\n\n Please generate a cover letter with 500 characters."
    
    # Generate response from OpenAI
    response = llm.invoke(prompt)
    
    #response = llm.ask(chat_prompt)
    print(response)
    
    # Extract content from the response data
    cover_letter = response.content
    #chat_prompt = ChatPromptTemplate.from_messages([
    #("system", "You are a world class technical documentation writer."),
    #("user", "compare {resume} and {job_description}")
#])
    #response = llm.ask(chat_prompt)
    print(cover_letter)
    
    # Extract content from the response data
    return cover_letter

if __name__ == "__main__":
    main()
