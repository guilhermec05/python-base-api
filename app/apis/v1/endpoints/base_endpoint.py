from http import HTTPStatus
from fastapi import HTTPException


def result(callback):
    try:
       return callback()
    
    except Exception as e:
         raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR , detail= {"mensagem":e})  