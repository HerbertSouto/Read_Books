from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional


class BookBase(BaseModel):
    name: str
    category: Optional[str] = None
    publisher: str
    number_of_pages: int
    start_reading: datetime
    end_reading: datetime

class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    publisher: Optional[str] = None
    number_of_pages: Optional[int] = None
    start_reading: Optional[datetime] = None
    end_reading: Optional[datetime] = None
