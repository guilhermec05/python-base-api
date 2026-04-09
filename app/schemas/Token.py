from pydantic import BaseModel

class TokenReponse(BaseModel):
    token:str
    expiration:str
