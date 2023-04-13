import streamlit as st

st.header("Dr. GPT")


col1, col2 = st.columns(2)
with col1:
    sex = st.selectbox(
        'What is your biological sex?',
        ('Male', 'Female', 'Other'))
    
with col2:
    option_dialect = st.multiselect(
        'Do you have other information you would like to provide?',
        ('Demographic information', 'Test results', 'Family history', 'Ruled out diagnoses'))

def get_text():
    input_text = st.text_area(label="Symptom Input", label_visibility='collapsed', placeholder="Your Symptoms...", key="symptom_input")
    return input_text

symptoms_input = get_text()


st.button("*Go*", type='secondary', help="Click to see a predicted set of symptoms.", on_click="")

st.markdown("### Diagnosis:")