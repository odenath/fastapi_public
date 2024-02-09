# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Corrija a senha, host e porta conforme necessário
# DATABASE_URL = 'postgresql://postgres:nova_senha@localhost:5432/bruto'

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# try:
#     engine.connect()
#     print("Conexão bem-sucedida!")
# except Exception as e:
#     print(f"Erro ao conectar ao banco de dados: {e}")