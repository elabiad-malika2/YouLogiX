from fastapi import HTTPException ,status

def raise_not_found(entity_name:str,entity_id:int):

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity_name} avec l'ID {entity_id} n'existe pas dans le systeme"
    )