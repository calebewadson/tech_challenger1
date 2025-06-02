from fastapi import FastAPI
from api.routes import router as data_router 
from auth.jwt import verify_token, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from datetime import timedelta

app = FastAPI()

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "user" or form_data.password != "password":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário/Senha inválidos")
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type":"bearer"}

app.include_router(data_router, prefix="/data", dependencies=[Depends(verify_token)])
