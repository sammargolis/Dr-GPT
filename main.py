import streamlit as st

from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
You are a doctor. I will give you my symptoms. If I don't provide symptoms, then stop and tell me I need to. Based on my symptoms, please list the top 5 most likely diagnoses ranked most to least likely with a single-line explanation. Of the listed diagnoses guess what you think I have with percentage likelihood in parentheses.

Based on the most likely diagnosis, what should I do to confirm the diagnosis? Based on the most likely diagnosis, what would the treatment be?

Provide a link from Mayo Clinic that has information on the most likely diagnosis.

SYMPTOMS: {symptoms}

RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["symptoms"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    return llm


st.header("Dr. GPT")


col1, col2 = st.columns(2)
with col1:
    acknowledgement = st.selectbox(
        'Acknowledgement that this is not medical advice',
        ('Yes', 'No'))
    
with col2:
    option_dialect = st.multiselect(
        'Do you have other information you would like to provide?',
        ('Demographic information', 'Test results', 'Family history', 'Ruled out diagnoses'))





def get_text():
    input_text = st.text_area(label="Symptom Input", label_visibility='collapsed', placeholder="Your Symptoms...", key="symptom_input")
    return input_text

symptom_input = get_text()


def update_text_with_example():
    st.session_state.symptom_input = symptom_input


st.button("*Go*", type='secondary', help="Click to see a predicted set of symptoms.", on_click=update_text_with_example)

st.markdown("### Diagnosis:")


if symptom_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    st.write("Please wait, I am thinking... ")

    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_symptoms = prompt.format(symptoms=symptom_input)

    formatted_diagnosis = llm(prompt_with_symptoms)

    st.write(formatted_diagnosis)