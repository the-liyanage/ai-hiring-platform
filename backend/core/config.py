# Reads the .env file and make those values available to every other file in the project

# Imports the class that knows how to read .env files
from pydantic_settings import BaseSettings 
from pydantic import Field 

# Pydantic - is a data validation library. it makes sure data has the right shape and type before the code uses it
# BaseSettings - validates and loads .env config
# BaseModel - validates API request and response data

class Settings(BaseSettings):
    # the(...) means required. App won't start without it. It reads the value from the .env automatically
    GROQ_API_KEY: str = Field(..., description = "Groq API key")

    APP_NAME: str = "AI Hiring Intelligence Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True


    CHROMA_PERSIST_DIR: str = "./chroma_data"
    UPLOAD_DIR: str = "./uploads"

    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    TOP_K_RESULTS: int = 50

    # tells pydantic where the .env file is
    class Config:
        env_file = ".env"
        env_file_encoding = "utf=8"

settings = Settings()