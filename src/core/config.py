from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = find_dotenv("src/.env")
load_dotenv(env_path)


class Settings(BaseSettings):
    COOKIE_MAX_AGE: int

    HUNTER_API_KEY: str
    BIG_BOOK_API_KEY: str

    model_config = SettingsConfigDict(env_file=env_path)


settings = Settings()
