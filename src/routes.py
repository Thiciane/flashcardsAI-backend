from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import get_session
from .schemas import CategorySchema, DeckSchema, WordSchema
from .models import Category, Deck, Word

router = APIRouter(prefix="/api", tags=["API"])

@router.get("/words")
async def list_words():
    return {"message": "Você acessou a rota de palavras!"}

@router.get("/decks")
async def list_decks():
    return {"message": "Você acessou a rota de decks!"}

@router.post("/category")
async def create_category(category_schema: CategorySchema, session: Session = Depends(get_session)):
    new_category = Category(category_schema.name)
    session.add(new_category)
    session.commit()
    session.refresh(new_category)
    return {"message": f"Você criou uma nova categoria! ID: {new_category.id}"}

@router.post("/words")
async def create_word(word_schema: WordSchema, session: Session = Depends(get_session)):
    new_word = Word(
        word_schema.word,
        word_schema.translation,
        word_schema.category_id,
    )
    session.add(new_word)
    session.commit()
    session.refresh(new_word)
    return {"message": f"Você criou uma nova palavra! ID: {new_word.id}"}

@router.post("/decks")
async def create_deck(deck_schema: DeckSchema, session: Session = Depends(get_session)):
    new_deck = Deck(
        deck_schema.title,
        deck_schema.description
    )
    session.add(new_deck)
    session.commit()
    session.refresh(new_deck)
    return {"message": f"Você criou uma novo baralho! ID: {new_deck.id}"}

@router.get("/words/{word_id}")
async def get_word(word_id: int):
    return {"message": f"Você acessou a palavra com ID {word_id}!"}

@router.get("/decks/{deck_id}")
async def get_deck(deck_id: int):
    return {"message": f"Você acessou o deck com ID {deck_id}!"}

@router.put("/words/{word_id}")
async def update_word(word_id: int):
    return {"message": f"Você atualizou a palavra com ID {word_id}!"}

@router.put("/decks/{deck_id}")
async def update_deck(deck_id: int):
    return {"message": f"Você atualizou o deck com ID {deck_id}!"}
