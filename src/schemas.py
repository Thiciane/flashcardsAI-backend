from pydantic import BaseModel
from typing import Optional

class CategorySchema(BaseModel):
    name: str
    
    class Config:
        from_attributes = True

class WordSchema(BaseModel):
    word: str
    translation: str
    category_id: int
    
    class Config:
        from_attributes = True
        
class DeckSchema(BaseModel):
    title: str
    description: str
    
    class Config: 
        from_attributes = True