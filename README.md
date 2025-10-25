# 🎬 Movie-to-Book API Service

This project is a FastAPI web service powered by LangChain, Groq LLMs, and LangSmith tracing. It infers the book behind a given movie title, showcasing AI-powered content analysis with a clean API interface and full observability.

## 🚀 Live Demo

- 🔗 FastAPI backend: [https://sekhar-fastapi-app.azurewebsites.net](https://sekhar-fastapi-app.azurewebsites.net)
- 🌐 Streamlit frontend: [Streamlit Cloud link here]
- 📊 LangSmith trace: [View sample trace](https://eu.smith.langchain.com/public/trace/your-trace-id)

## 🧠 Features

- 🔗 FastAPI microservice with modular LangChain chains
- 🧠 Groq-powered LLM inference (Mixtral 8x7B)
- 📈 LangSmith observability with EU endpoint
- 🎛️ Streamlit UI for recruiter-friendly interaction
- 🎬 Cinematic storytelling and multilingual chain support
- ☁️ Azure App Service deployment (F1 tier)

## 🧪 Chains Included

- `get_book_name`: Infers the book behind a movie
- `spoiler_chain`: Reveals plot twists (optional)
- `translator_chain`: Translates movie titles (optional)
- `emotion_chain`: Detects emotional tone (optional)

## 📦 Project Structure

```
├── server.py        # FastAPI app with LangChain chains
├── app.py          # Streamlit frontend
├── requirements.txt # Python dependencies
├── .env.example    # Environment variable template
└── .gitignore      # Secure Git setup
```

## 🔐 Environment Variables

Create a `.env` file based on `.env.example` and set the following:

```env
OPENAI_API_KEY=your-open-api-key-here
CLAUDE_API_KEY=your-claude-api-key-here
GROQ_API_KEY=your-groq-api-key-here
LANGCHAIN_API_KEY=your-langchain-api-key-here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=your-project-name-here
LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
```

---

🧭 Azure Deployment Note When deploying to Azure App Service, set these variables manually under: App Service → Configuration → Application Settings

This ensures your app runs securely in the cloud without exposing secrets in GitHub.

## 🛠️ How to Run Locally

1. Clone the repo
2. Create `.env` from `.env.example`
3. Start FastAPI backend:

```bash
uvicorn server:app --reload
```

4. Start Streamlit frontend:

```bash
streamlit run app.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
