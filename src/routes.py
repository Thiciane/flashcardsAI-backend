from fastapi import APIRouter
router = APIRouter(prefix="/api", tags=["API"])

@router.get("/words")
async def list_words():
    return {"message": "Você acessou a rota de palavras!"}

@router.get("/decks")
async def list_decks():
    return {"message": "Você acessou a rota de decks!"}

@router.post("/words")
async def create_word():
    return {"message": "Você criou uma nova palavra!"}

@router.post("/decks")
async def create_deck():
    return {"message": "Você criou um novo deck!"}

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