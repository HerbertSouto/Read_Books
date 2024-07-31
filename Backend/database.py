from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da conexão
host_name = os.getenv('HOST_NAME')
database_name = os.getenv('DATABASE_NAME')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

POSTGRES_DATABASE_URL = f"postgresql://{user_name}:{password}@{host_name}/{database_name}"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    