from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  POSTGRES_HOST: str
  POSTGRES_PORT: int
  POSTGRES_USER: str
  POSTGRES_PASSWORD: str
  POSTGRES_DB: str

  REDIS_HOST: str
  REDIS_PORT: int
  REDIS_PASSWORD: str
  REDIS_USER: str
  REDIS_DB: int
  CACHE_TTL_SECONDS: int
  CACHE_KEY_TASKS: str

  @property
  def get_db_url(self) -> str:
    return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

  @property
  def get_alembic_url(self) -> str:
    return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

  @property
  def get_redis_url(self) -> str:
    return f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

  model_config = SettingsConfigDict(env_file=".env")

settings: Settings = Settings()