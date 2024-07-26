from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

#Criação da tabela no banco e seus atributos
class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    publisher = Column(String)
    number_of_pages = Column(Integer)
    start_reading = Column(DateTime)
    end_reading = Column(DateTime)
    created_at = Column(DateTime(timezone=True), default=func.now())