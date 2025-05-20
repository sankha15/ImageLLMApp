from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt):
        response = model.generate_content(prompt)
        return response.text

st.set_page_config(page_title="Gemini LLM App", page_icon=":robot:")
st.header("Gemini LLM App")

input = st.text_input("Input: ",key="input")
submit = st.button(label="Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
    
    
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyA3z9E5hOxAyZVS2HvmVM6STCeRNhV5zlc")

# models = genai.list_models()
# for m in models:
#     print(m.name, m.supported_generation_methods)