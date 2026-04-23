from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

# Dependency for FastAPI DI
from functools import lru_cache

class Settings(BaseSettings):
	# FastAPI
	api_prefix: str = "/api/v1"
	debug: bool = False

	# Database
	postgres_dsn: str = Field(..., env="POSTGRES_DSN")
	pgvector_enabled: bool = True
 
    #embeddings
	embedding_model: str = Field("text-embedding-3-small", env="EMBEDDING_MODEL")  # Model selection

	# OpenRouter
	openrouter_api_key: str = Field(..., env="OPENROUTER_API_KEY")
	openrouter_base_url: str = Field("https://openrouter.ai/api/v1", env="OPENROUTER_BASE_URL")
	openrouter_model: str = Field("openai/gpt-4o-mini", env="OPENROUTER_MODEL")  # Model selection

	# Logging
	log_level: str = Field("INFO", env="LOG_LEVEL")

	class Config:
		env_file = ".env"
		env_file_encoding = "utf-8"

settings = Settings()


@lru_cache()
def get_settings():
	return settings
