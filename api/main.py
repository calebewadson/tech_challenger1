from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from api.routes import router as data_router
from auth.jwt import create_access_token, verify_token
from datetime import timedelta

app = FastAPI(title="Embrapa Wine Data API")

app.include_router(data_router)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validação de usuário
    if form_data.username != "user" or form_data.password != "password":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos")
    access_token_expires = timedelta(minutes=30)
    token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}
