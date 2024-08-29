import  os
from dotenv import load_dotenv
from pydantic.types import SecretStr
from pydantic_settings import BaseSettings
from pydantic import Field

load_dotenv()
ENV = os.environ.get("ENV", "default")



class _Settings(BaseSettings):
    OPENAI_API_KEY: str
    # LANGCHAIN_TRACING_V2="true"
    # LANGCHAIN_API_KEY="..."

class Development(_Settings):
    ENV: str = "development"


config = {
    "default": Development,
}

SETTINGS:_Settings = config[ENV]()