from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_NAME: str = "your-database-name"
    PROJECT_ID: str = "your-project-id"
    API_KEY: str = "your-api-key"

    @property
    def sqlite_cloud_url(self) -> str:
        return f"sqlitecloud://{self.PROJECT_ID}.sqlite.cloud:8860/{self.DATABASE_NAME}?apikey={self.API_KEY}"


settings = Settings()
