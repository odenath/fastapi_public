from database import get_source_session, get_destination_session
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import select
from sqlalchemy import select, and_

def copy_schema(source_session, destination_session):
    """
    Copia os schemas das tabelas do banco de dados de origem para o banco de dados de destino.
    """
    metadata = MetaData()
    metadata.reflect(bind=source_session.bind)
    metadata.create_all(bind=destination_session.bind, checkfirst=True)
    
def insert_data(source_session: Session, destination_session: Session):
    """
    Insere os dados do banco de dados de origem para o banco de dados de destino.
    """
    metadata = MetaData()
    metadata.reflect(bind=source_session.bind)

    for table_name in metadata.tables.keys():
        table = Table(table_name, metadata, autoload_with=source_session.bind)
        rows = source_session.execute(select(table)).fetchall()

        for row in rows:
            # Cria um novo objeto de linha com os mesmos dados
            destination_session.execute(table.insert().values(row))
            
    destination_session.commit()

def migrate_data(source_session: Session, destination_session: Session):
    """
    Migrates data from source database to destination database.
    """
    source_session = get_source_session()
    destination_session = get_destination_session()

    if not source_session or not destination_session:
        raise ValueError("Failed to get database sessions")

    copy_schema(source_session, destination_session)
    insert_data(source_session, destination_session)

    source_session.close()
    destination_session.close()


def update_data(source_session: Session, destination_session: Session):
    """
    Atualiza os dados do banco de dados de destino com os dados do banco de dados de origem.
    """
    source_session = get_source_session()
    destination_session = get_destination_session()


    metadata = MetaData(bind=source_session.bind)
    metadata.reflect()

    for table_name in metadata.tables.keys():
        table = Table(table_name, metadata, autoload_with=source_session.bind)

        # Verifica se a tabela tem uma coluna chamada 'data'
        if 'data' in table.columns:
            data_column = table.columns['data']

            # Obtém todos os registros da tabela de origem
            source_rows = source_session.query(table).all()

            for row in source_rows:
                # Verifica se o registro existe no banco de dados de destino
                exists = destination_session.query(table).filter(and_(data_column == row.data)).first()

                if not exists:
                    # Se o registro não existir no banco de dados de destino, insere-o
                    new_row = table(**row._asdict())
                    try:
                        destination_session.add(new_row)
                        destination_session.commit()
                    except Exception as e:
                        print(f"Erro ao atualizar dados: {e}")
                        return False
                    

    destination_session.commit()

    source_session.close()
    destination_session.close()

    return True






































# from sqlalchemy.orm import Session
# from sqlalchemy import inspect
# from database import get_source_session, get_destination_session
# from sqlalchemy import create_engine, MetaData, Table
# from sqlalchemy.orm import Session, sessionmaker


# def copy_schema(source_engine, destination_engine):
#     """
#     Copia os schemas das tabelas do banco de dados de origem para o banco de dados de destino.
#     """
#     metadata = MetaData(bind=source_engine)
#     metadata.reflect()

#     metadata.create_all(bind=destination_engine, checkfirst=True)

# def insert_data(source_session: Session, destination_session: Session):
#     """
#     Insere os dados do banco de dados de origem para o banco de dados de destino.
#     """
#     metadata = MetaData(bind=source_session.bind)
#     metadata.reflect()

#     for table_name in metadata.tables.keys():
#         table = Table(table_name, metadata, autoload_with=source_session.bind)
#         rows = source_session.query(table).all()

#         for row in rows:
#             # Cria um novo objeto de linha com os mesmos dados
#             new_row = table(**row._asdict())
#             destination_session.add(new_row)
 

# def migrate_data():
#     """
#     Migrates data from source database to destination database.
#     """
#     source_session = get_source_session()
#     destination_session = get_destination_session()

#     if not source_session or not destination_session:
#         raise ValueError("Failed to get database sessions")

#     copy_schema(source_session, destination_session)
#     insert_data(source_session, destination_session)

#     source_session.close()
#     destination_session.close()


# def copy_schema(source_session: Session, destination_session: Session):
#     """
#     Copia os schemas das tabelas do banco de dados de origem para o banco de dados de destino.
#     """
#     inspector = inspect(source_session.bind)
#     tables = inspector.get_table_names()

#     for table_name in tables:
#         table = inspector.get_table(table_name)
#         table.create(destination_session.bind, checkfirst=True)

# def insert_data(source_session: Session, destination_session: Session):
#        """
#     Insere os dados do banco de dados de origem para o banco de dados de destino.
#     """
#     inspector = inspect(source_session.bind)
#     tables = inspector.get_table_names()

#     for table_name in tables:
#         query = source_session.query(inspector.get_table(table_name))
#         data = query.all()

#         for row in data:
#             destination_session.add(row)

#     destination_session.commit()