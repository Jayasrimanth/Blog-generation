import os
import sys
import streamlit as st
from templates.prompt_templates import PromptTemplate
from models.cohere_utils import getCohereResponse

# Ensure Python can find modules in the `models` and `templates` directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "models"))
sys.path.append(os.path.join(BASE_DIR, "templates"))

# Streamlit App
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## Create two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No. of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

## Final response
if submit:
    if not input_text or not no_words or not blog_style:
        st.error("Please fill out all fields before generating!")
    else:
        try:
            response = getCohereResponse(input_text, no_words, blog_style)
            st.subheader("Generated Blog")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
