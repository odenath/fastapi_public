from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
               
DATABASE_URL = 'postgresql://postgres:nova_senha@localhost:5432/bruto'
DESTINATION_DATABASE_URL = 'postgresql://postgres:nova_senha@localhost:5432/zerado'
# postgresql://postgres:nova_senha@localhost:5432/bruto

source_engine = create_engine(DATABASE_URL)
destination_engine = create_engine(DESTINATION_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=source_engine)
DestinationSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=destination_engine)

def get_source_session():
    """
    Retorna uma nova sessão do banco de dados de origem.
    """
    return SessionLocal()

def get_destination_session():
    """
    Retorna uma nova sessão do banco de dados de destino.
    """
    return DestinationSessionLocal()

