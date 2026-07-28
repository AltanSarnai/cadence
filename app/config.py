from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    anthropic_api_key: str #matches ANTHROPIC_API_KEY from 
                            #.env case-insensitive

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.joinpath('.env'),
        extra="ignore"
    )
    
settings = Settings()    