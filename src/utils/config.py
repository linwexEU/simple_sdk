import os

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

env_path = find_dotenv("../.env")
load_dotenv(env_path)


class Settings(BaseSettings):
    API_KEY: str
    COOKIE_MAX_AGE: int

    model_config = SettingsConfigDict(env_file=env_path)


settings = Settings()
