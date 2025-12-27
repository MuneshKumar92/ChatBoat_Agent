# step1 - Setup API key for Groq and tavily
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


# Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

openai_llm = ChatOpenAI(model="gpt-3.5-turbo")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")


# Step3: Setup AI Agent with Search tool functionality

# from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain_core.messages.ai import AIMessage

search_tool1 = TavilySearch(max_results=3)

system_prompt = "Act as an AI Chatbot who is smart and friendly"


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):

    if provider == "groq":
        llmName = ChatGroq(model=llm_id)
    elif provider == "openAi":
        llmName = ChatOpenAI(model=llm_id)

    print(
        "DEBUG provider:",
        provider,
        "llm_id:",
        llm_id,
        "system promt:",
        system_prompt,
        "Qery is : ",
        query,
        "search flag : ",
        allow_search,
    )

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent = create_agent(model=llmName, tools=tools, system_prompt=system_prompt)
    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [
        message.content for message in messages if isinstance(message, AIMessage)
    ]
    return ai_messages[-1]


email_body = "** Final Response: ** The current Indian PM is Narendra Modi."


def send_email_gmail(to_email, subject, body):
    msg = MIMEText(body)
    msg["From"] = "munesh.applicationdeveloper@gmail.com"
    msg["To"] = to_email
    msg["Subject"] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("munesh.applicationdeveloper@gmail.com", "fndo kykb yscy rhba")
        server.send_message(msg)
