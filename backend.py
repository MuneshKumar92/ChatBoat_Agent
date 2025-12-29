from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Step2 Setup AI Agent from FrontEnd Request

from fastapi import FastAPI
from ao_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "llama-3.3-70b-8192",
    "gpt-4o-mini",
    "gpt-3.5-turbo",
]

app = FastAPI(title="LangGraph AI Agent")


@app.get("/agent")
def get_agent():
    return {"Message": "Hello From the Agent"}


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to intract with the chatbot using langgraph and search tolls.
    it select model dynamically based on requests
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name . kindly select a valid AI model"}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it!

    response = get_response_from_ai_agent(
        llm_id,
        query,
        allow_search,
        system_prompt,
        provider.lower().strip(),
    )
    return response


# Step3 Run app & Explore Swagger UI Docs

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9999)

    # Swagger UI will give UI for test the Fast API request.
    # strat the server , just run backend.py file.
    # http://127.0.0.1:9999/chat
    # http://127.0.0.1:9999/docs
