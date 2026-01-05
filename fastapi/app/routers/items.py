from fastapi import APIRouter, Depends, HTTPException, status, Header, Cookie, Response
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, dependencies

router = APIRouter()

# Items CRUD
# 3.4 Dependency Injection (Shared DB sessions, Auth dependencies)
@router.post("/items/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED, tags=["items"])
def create_item(
    item: schemas.ItemCreate, 
    db: Session = Depends(dependencies.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    # 3.7 SQL Alchemy ORM
    db_item = models.Item(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/", response_model=List[schemas.Item], tags=["items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

# 3.2 Request & Response Handling
# 3.2 Path params, query params
@router.get("/items/{item_id}", tags=["items"])
def read_item(
    item_id: int, 
    q: Optional[str] = None, 
    short: bool = False
):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# 3.2 Headers & cookies
@router.get("/headers-and-cookies/", tags=["items"])
def read_headers_and_cookies(
    user_agent: Optional[str] = Header(None),
    ads_id: Optional[str] = Cookie(None)
):
    return {"User-Agent": user_agent, "ads_id": ads_id}

# 3.2 Status codes & error responses
@router.get("/items-header/{item_id}", status_code=status.HTTP_200_OK, tags=["items"])
def read_item_header(item_id: int, response: Response):
    if item_id == 0:
        raise HTTPException(status_code=418, detail="I'm a teapot (Item 0 is forbidden)")
    response.headers["X-Custom-Header"] = "Custom Value"
    return {"item_id": item_id, "message": "Custom header added"}
