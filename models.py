from datetime import datetime
from sqlmodel import Field, SQLModel


class SensorData(SQLModel, table=True):
    __tablename__ = "sensor_data"

    id: int | None = Field(default=None, primary_key=True)
    temperature: float
    humidity: float
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
