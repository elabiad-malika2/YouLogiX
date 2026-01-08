from fastapi import HTTPException ,status

def raise_not_found(entity_name:str,entity_id:int):

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity_name} avec l'ID {entity_id} n'existe pas dans le systeme"
    )
    
def raise_error_creation(e):
    raise HTTPException(status_code=400,
        detail=f"Error lors de la creation: {str(e)}"
    )
    
    
def raise_error_update(e):
    raise HTTPException(status_code=407,
        detail=f"Error lors de la modification: {str(e)}"
    )
