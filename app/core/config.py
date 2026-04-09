from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SERVICE_PORT :str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  
    )

settings = Settings()