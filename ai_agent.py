# Step1 - setup API key for Groq and tavily ,addition to OpenAP


from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


# sStep2 - etup LLM and Tools


import httpx
import certifi

client = httpx.Client(verify=certifi.where())

print("LOCATION OD CERTIFICATE :::    ", client)
client = httpx.Client(
    verify="/Users/munesh.kumar/agentic-chat-boat/venv/lib/python3.13/site-packages/certifi/cacert.pem"
)


# Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt‑3.5‑turbo")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_results=2)

print("✅ LLM initialized")

# Step3: Setup AI Agent with Search tool functionality

# from langgraph.prebuilt import create_react_agent
# from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

search_tool1 = TavilySearch(max_results=3)


# Step 3- setup AI Agent with search tool functionality

# from langgraph.prebuilt import create_react_agent

from langchain_core.messages.ai import AIMessage


system_prompt = "Act as an AI Chatbot who is smart and friendly"

agent = create_agent(model=groq_llm, tools=[search_tool1], system_prompt=system_prompt)

# 1. Import OpenAI client
from openai import OpenAI

# 2. Create the client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

# questions as a promp
query = "tell me about dinald trump"

state = {"messages": query}
response = agent.invoke(state)


messages = response.get("messages")
ai_message = [message.content for message in messages if isinstance(message, AIMessage)]


print("Response from AI ----        ", ai_message[-1]),
