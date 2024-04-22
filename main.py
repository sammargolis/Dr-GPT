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


def test_diagnosis():
    # Assuming a simplified logic to generate diagnosis
    diagnosis_text = """

    ### Differential Diagnosis:
    
    1. **Asthma**
       - **Likelihood:** More likely
       - **Reasoning:** Given your family history of respiratory conditions and symptoms like shortness of breath and persistent cough, asthma is a possible diagnosis. Chest pain from coughing is also possible in asthmatic conditions.
       
    2. **Chronic Obstructive Pulmonary Disease (COPD)**
       - **Likelihood:** Less likely
       - **Reasoning:** Typically occurs in older individuals and often associated with smoking. However, it can present earlier especially if significant family history.
    
    3. **Pulmonary Embolism (PE)**
       - **Likelihood:** Less likely but potentially serious
       - **Reasoning:** PE could cause shortness of breath and chest pain; however, it is less common in young people without predisposing factors.
    
    4. **Gastroesophageal Reflux Disease (GERD)**
       - **Likelihood:** Less likely
       - **Reasoning:** GERD can cause chronic cough and chest pain, but shortness of breath is less commonly associated.

    ### Recommended Action:
    
    - **Immediate Concerns:** If you experience severe symptoms such as severe chest pain or sudden shortness of breath, seek immediate medical attention at an emergency room.
    - **General Next Steps:** Schedule an appointment with your primary care provider for a physical examination and possible diagnostic tests.
    - **Conclusion:** Professional evaluation is crucial for an accurate diagnosis and effective treatment.
    """
    
    return diagnosis_text


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
        apologies_messages = """My apologies... I no longer maintain this application. If you are interested in it, feel free to email or message me.  Previously it would output similar to the following:"""
        st.subheader(apologies_messages)
        mock_diagnosis = test_diagnosis()
        st.write(mock_diagnosis)

st.warning('Disclaimer: Dr. GPT is not a substitute for medical advice. In the event of an emergency, contact a medical professional.')
