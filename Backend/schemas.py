from pydantic import BaseModel, PositiveFloat, EmailStr, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class CategoryBase(Enum):
    categoria1 = "Ficção"
    categoria2 = "Não-ficção"
    categoria3 = "Infantojuvenil"
    categoria4 = "Acadêmico"
    categoria5 = "Religioso/Espiritual"
    categoria6 = "Arte e Entretenimento"
    categoria7 = "Culinária"
    categoria8 = "Esportes e Lazer"
    categoria9 = "Biografia"
    categoria10 = "História"
    categoria11 = "Política"
    categoria12 = "Autoajuda"
    categoria13 = "Desenvolvimento Pessoal"
    categoria14 = "Ciências Sociais"
    categoria15 = "Educação"
    categoria16 = "Filosofia"
    categoria17 = "Ciência"
    categoria18 = "Matemática"
    categoria19 = "Tecnologia"
    categoria20 = "Engenharia"

class BookBase(BaseModel):
    name: str
    category: Optional[str] = None
    publisher: str
    number_of_pages: int
    start_reading: datetime
    end_reading: datetime

    @Field("category")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoryBase]:
            return v
        raise ValueError("Categoria inválida")


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

    @Field("category", pre=True, always=True)
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoryBase]:
            return v
        raise ValueError("Categoria inválida")