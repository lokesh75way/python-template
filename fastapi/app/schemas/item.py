from typing import Optional
from pydantic import BaseModel

# 3.3 Pydantic (Core of FastAPI)
# 3.3 BaseModel
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

# 3.3 Model vs Schema separation
# This uses the same base but creates the full "Schema" for returning data
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
