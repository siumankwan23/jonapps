# app.py

#from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
#from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import OpenAI
from streamlit_extras.buy_me_a_coffee import button

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
    st.title('💬 Interview Helper')
    st.markdown('''
    ''')
st.write("Siumankwan23@gmail.com")
st.write("Support Me")
button(username="siumankwan23", floating=False, width=221)
st.sidebar.success("Select a tool above.")

# Main function
def main():
    
    st.title("Interview helper\n Create Q&A responses focusing on a chosen area, like managerial, technical, or problem-solving skills.")
    
    # Input boxes for resume and job description
    col1, col2, col3 = st.columns(3)
    with col1:
        resume = st.text_area("Paste Your Resume Here:", height=400)

    with col2:
        job_description = st.text_area("Paste the Job Description Here:", height=400)
        
    with col3:
        topic = st.text_area("Topic Q&A to generate:", height=400)
    # Input boxes for resume and job description

    if st.button("Submit"):
        # Prepare prompt for OpenAI
        #prompt = f"Compare the resume with the job description and identify what is missing from the resume. Resume: {resume}. Job Description: {job_description}."

        # Generate response from OpenAI
        response = generate_interview_qa(resume, job_description, topic)

        # Display missing points as bullet points
        st.write("### Gap in the resume for the job posting:")
        for point in response:
            st.write(f"{point}")

def generate_interview_qa(resume, job_description, topic):
    
        # Prepare prompt for OpenAI
    prompt = f"my resume is \n{resume}.\n\n the job description is \n{job_description}.\n\n Generate questions and answers to prepare for the interview on the topic {topic}. make sure the responses are questions along with answers"
    
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

if __name__ == "__main__":
    main()
