from dotenv import load_dotenv

load_dotenv()
import os

class Settings:
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY")
    QDRANT_CLUSTER_URL: str = os.getenv("QDRANT_CLUSTER_URL")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    
settings = Settings()    