from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, APIKeyHeader
from sqlalchemy.orm import Session
from .. import models, schemas, auth, dependencies

router = APIRouter(
    tags=["authentication"]
)

# 3.5 OAuth2 password flow
@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependencies.get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 3.5 API key authentication
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

@router.get("/api-key-protected")
async def api_key_protected(api_key: str = Depends(api_key_header)):
    if api_key != "secret-api-key":
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return {"message": "You are authenticated with API Key"}
