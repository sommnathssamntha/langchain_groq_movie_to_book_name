from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_groq import ChatGroq
from langchain_core.tracers.langchain import LangChainTracer

from dotenv import load_dotenv
import os
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
groq_model = ChatGroq(groq_api_key=groq_api_key, model="llama-3.3-70b-versatile")

## create prompt template
system_prompt = """You are a helpful assistant that gives the name of a novel or book from 
the following movie is based {title}"""
user_prompt = """Movie Title: {title}"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", user_prompt)
])


output_parser = StrOutputParser()

chain = prompt_template | groq_model | output_parser

# initialize langchain tracer
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")
print("LangSmith API Key:", langsmith_api_key) 

tracer = LangChainTracer()
chain = chain.with_config({"callback": [tracer]})

## fast api server
app = FastAPI(title="LangServe with Groq and LangChain", version="0.1",
              description="An example server that connects LangChain with Groq using FastAPI")

## define addroutes that connectes langxhain to langserve
add_routes(app, chain, path="/get_book_name")

@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)