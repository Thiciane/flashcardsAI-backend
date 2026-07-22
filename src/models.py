from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType


# cria a conexão do seu banco 
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

# cria as classes/tabelas do banco
class Category(Base):    
    __tablename__ = "categorys"
    
    """NAME_CATEGORY = (
        ("Adjetivo", "Adjetivo"),
        ("Advérbio", "Advérbio"),
        ("Conjunção", "Conjunção"),
        ("Interjeição", "Interjeição"),
        ("Substantivo", "Substantivo"),
        ("Artigo", "Artigo"),
        ("Preposição", "Preposição"),
        ("Numeral", "Numeral"),
        ("Pronome", "Pronome"),
        ("Verbo", "Verbo"),
        ("Outro", "Outro")
        
    )"""
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    
    def __init__(self, name):
        self.name = name

class Word(Base):
    __tablename__ = "words"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    word = Column("word", String, nullable=False)
    translation = Column("translation", String, nullable=False)
    category_id = Column("category_id", Integer, ForeignKey("categorys.id"))
    
    def __init__(self, word, translation, category_id):
        self.word = word
        self.translation = translation
        self.category_id = category_id
    
class Deck(Base):
    __tablename__ = "decks"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String, nullable=False)
    description = Column("description", String, nullable=False)
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        
class Deck_Word(Base):
    __tablename__= "deck_word"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    deck_id = Column("deck_id", Integer, ForeignKey("decks.id"))
    word_id = Column("word_id", Integer, ForeignKey("words.id"))
    
    def __init__(self, deck_id, word_id ):
        self.deck_id = deck_id
        self.word_id = word_id

# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)