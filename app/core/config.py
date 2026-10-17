from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from sqlalchemy.engine import URL
class Settings(BaseSettings):

    APP_NAME: str = "Sales Agent"
    DEBUG: bool = False
    DB_HOST: str="localhost"
    DB_PORT: int=5432
    DB_USER: str="postgres"
    DB_PASSWORD: str="54wx9vdn"
    DB_NAME: str="sales-agent-db"
    
    @proterty
    def DATABASE_URL(self) -> URL:
        return URL.create(
            drivername="postgresql+psycopg2",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
            query={"options":{f"-c search_path={self.DB_SCHEMA}"}}
        )

    model_config= SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
        )

@lru_cache()
def get_settings() -> Settings:
    return Settings()