from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  POSTGRES_HOST: str
  POSTGRES_PORT: int
  POSTGRES_USER: str
  POSTGRES_PASSWORD: str
  POSTGRES_DB: str

  @property
  def get_db_url(self):
    return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

  @property
  def get_alembic_url(self) -> str:
    return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

  model_config = SettingsConfigDict(env_file=".env")

settings: Settings = Settings()