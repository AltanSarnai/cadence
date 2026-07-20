from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_key: str = "sk-ant-api03-esnothererightnow"

    model_config = SettingsConfigDict(
        env_file='.env',
        extra="ignore"
    )

settings = Settings()    