from http import HTTPStatus
from fastapi import HTTPException,Response


def result(callback):
    try:
       return callback
    
    except Exception as e:
         raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":str(e)})  