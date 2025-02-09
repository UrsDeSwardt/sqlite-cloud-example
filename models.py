from datetime import datetime
from sqlmodel import Field, SQLModel
from settings import settings


class SensorData(SQLModel, table=True):
    __tablename__ = settings.TABLE_NAME

    id: int | None = Field(default=None, primary_key=True)
    temperature: float
    humidity: float
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
