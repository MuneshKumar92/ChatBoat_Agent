# Use official Python image
FROM python:3.13-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt && \
    python -c 'import langchain, uvicorn, aiohttp; print("All good!")'


# Copy the rest of the code
COPY . .

# Expose port
EXPOSE 8000

# Environment variables
ENV GROQ_API_KEY="your_groq_key"
ENV OPENAI_API_KEY="your_openai_key"
ENV TAVILY_API_KEY="your_tavily_key"

# Start FastAPI
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
