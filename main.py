import streamlit as st

# from langchain import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain.chains import SimpleSequentialChain
# from Bio_Epidemiology_NER.bio_recognizer import ner_prediction

# openai_api_key = st.secrets["openai_api_key"]

# simplellm = OpenAI(temperature=1, model_name="text-ada-001", openai_api_key=openai_api_key)
# llm = OpenAI(temperature=0,
#              model_name="text-davinci-003",
#              openai_api_key=openai_api_key)


template = """
You are a doctor. I will give you a dictionary mapping from biological and medical concepts to values. Based on my symptoms, please list the top 5 most likely diagnoses ranked most to least likely with a single-line explanation. Of the listed diagnoses guess what you think I have with percentage likelihood in parentheses.

Based on the most likely diagnosis, what should I do to confirm the diagnosis? Based on the most likely diagnosis, what would the treatment be?

Provide a link from Mayo Clinic that has information on the most likely diagnosis.

{symptoms}

RESPONSE:
"""

# prompt = PromptTemplate(
#     input_variables=["symptoms"],
#     template=template,
# )

# Title + Description Items
st.title("Dr. GPT 👩‍⚕️")

st.header("Get diagnostic and care direction based on your symptoms 📋")

st.write("What are your symptoms?")


### Getting the text inputs from all text fields ###

# Returns text area that takes in symptom input
def get_symptom_input():
    input_text = st.text_area(label="Symptom Input",
                              label_visibility='collapsed',
                              placeholder="Example: I have a cough and runny nose",
                              key="symptom_input")
    return input_text


# State that sets our current list of symptoms
symptom_input = get_symptom_input()

# Updates our current sessions symptom state with view's symptom input


def update_text_with_symptoms():
    st.session_state.symptom_input = symptom_input


def get_demographics():
    input_text = st.text_area(label="Demographic information",
                              label_visibility='collapsed',
                              placeholder="Example: I am a 24 year old woman",
                              key="dempgraphics_input")
    return input_text


def get_history():
    input_text = st.text_area(label="Family History",
                              label_visibility='collapsed',
                              placeholder="Example: My family has a history of respiratory conditions.",
                              key="history_input")
    return input_text


def get_other_diagnosis():
    input_text = st.text_area(label="Other Diagnosic Information", label_visibility='collapsed',
                              placeholder="Example: I know I do not have COVID, since I have taken a test", key="other_diagnostic_input")
    return input_text


# Add additional information components for user input
with st.expander("Add additional information"):
    st.subheader("Demographic Information")
    dempgraphics_input = get_demographics()
    st.subheader("Family History")
    history_input = get_history()
    st.subheader("Other Diagnostic Information")
    other_diagnostic_input = get_other_diagnosis()

# Update state and re-run
st.button("*Go*", type='primary', help="Click to see a predicted set of symptoms.",
          on_click=update_text_with_symptoms)

st.header("Diagnosis:")

# Really ugly method to remove some of the unnessary string. Shouldn't have this but got lazy looking for a solution and built this for now


# def reformatJSON(input):
#     formatted_Input = input.replace("],[", "\n\n")
#     formatted_Input = formatted_Input.replace(",", ":")
#     formatted_Input = formatted_Input.replace("[", "")
#     formatted_Input = formatted_Input.replace("]", "")
#     formatted_Input = formatted_Input.strip('\"')
#     return formatted_Input

# Returns dictionary mapping NER concept type to user provided value
# def mapToMedicalEntities(symptom_input):
#     df_med_entities = ner_prediction(corpus=symptom_input, compute='cpu')
#     df_med_entities = df_med_entities.drop(['score'], axis=1)
#     med_entities_dict = dict(
#         zip(df_med_entities.entity_group, df_med_entities.value))
#     # json_MedEntities = df_med_entities.to_json(orient="values")
#     # formatted_MedEntities = reformatJSON(json_MedEntities)
#     return med_entities_dict


# def runModel(symptom_input):
#     medEntities = mapToMedicalEntities(symptom_input)
#     prompt_with_symptoms = prompt.format(symptoms=medEntities)
#     formatted_diagnosis = llm(prompt_with_symptoms)
#     return formatted_diagnosis
#     # return prompt_with_symptoms


# If state value present then check if API key is avaialble and then call to model
if symptom_input:
    # if not openai_api_key:
    #     st.warning(
    #         'Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
    #     st.stop()

    demographic_info = st.session_state.dempgraphics_input
    family_history = st.session_state.history_input

    # Aggregate all of the user input
    user_input = "Subject: Self, Symptoms: " + symptom_input + " and " + \
        demographic_info + " and history: " + family_history
    # st.warning(user_input)

    with st.spinner('One moment, I am thinking...'):
        # formatted_diagnosis = runModel(user_input)
        formatted_diagnosis = """So sorry I no longer maintain this application. If you are interested in it, feel free to email or message me.  Previously it would output similar to the following"""
        st.write(formatted_diagnosis)

st.warning('Disclaimer: Dr. GPT is not a substitute for medical advice. In the event of an emergency, contact a medical professional.')
