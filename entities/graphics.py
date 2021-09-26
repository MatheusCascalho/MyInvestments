from pydantic import BaseModel


class Point(BaseModel):
    date: str
    value: float