# Step1 Setup UI with Streamlit (model provider, model, system prompt,web search, query)
import streamlit as st
import requests
from ao_agent import send_email_gmail


st.set_page_config(page_title="Lang Graph AI Agent", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and interact with the AI Agents!")

system_prompt = st.text_area(
    "Define your AI Agent: ", height=70, placeholder="Type your system prompt here..."
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
# MODEL_NAME_OPENAI = ["gpt-3.5-turbo"]

provider = st.radio("Select the provider:", ("Groq"))

if provider == "Groq":
    select_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)


allow_web_search = st.checkbox("Allow Web Search")

userQuesry = st.text_area("Enter you wuery", height=150, placeholder="Ask Anything")

API_URL = "http://13.211.189.248:8000/chat"

if st.button("Ask agent"):

    if userQuesry.strip():
        # Step2 Connect with Backend URL
        import requests

payload = {
    "model_name": select_model,
    "model_provider": provider,
    "system_prompt": system_prompt,
    "messages": [userQuesry],
    "allow_search": allow_web_search,
}
print("fill data is ", payload)

# get response from backend and show here
response = requests.post(API_URL, json=payload)
if response.status_code == 200:
    response_data = response.json()
    print("Response is  ", response_data)
    # send_email_gmail(
    #    to_email="sharmapallavi1308@gmail.com",
    #    subject="Munesh Chat Agent Response is ",
    #   body=response_data,
    # )

    if "error" in response_data:
        st.error(response_data["error"])
    else:
        # response = response
        st.subheader("Agent Response")
        st.markdown(f"** Munesh Agent Response: ** {response.json()}")
