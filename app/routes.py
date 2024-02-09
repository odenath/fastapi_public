from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from crud import migrate_data, update_data
from database import get_source_session, get_destination_session

router = APIRouter()

@router.post("/migrate")
async def migrate_data_route():
    """
    Rota para migrar dados do banco de dados de origem para o banco de dados de destino.
    """
    source_session = get_source_session()
    destination_session = get_destination_session()

    if not source_session or not destination_session:
        raise HTTPException(status_code=500, detail="Erro ao obter sessões do banco de dados")

    migrate_data(source_session, destination_session)

    return {"message": "Data migration successful"}

@router.post("/atualization")
async def atualization_data_route():
    """
    Rota para atualizar dados do banco de dados de origem para o banco de dados de destino.
    """
    source_session = get_source_session()
    destination_session = get_destination_session()

    if not source_session or not destination_session:
        raise HTTPException(status_code=500, detail="Erro ao obter sessões do banco de dados")

    update_data(source_session, destination_session)

    return {"message": "Data atualization successful"}
