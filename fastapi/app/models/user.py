from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

# 3.7 SQLAlchemy ORM
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # 3.7 Database Integration (Relationships)
    # Note: "Item" as string avoids circular import issues if Item is defined later or elsewhere
    items = relationship("Item", back_populates="owner")
