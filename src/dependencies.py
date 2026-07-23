from sqlalchemy.orm import sessionmaker

from .models import db

SessionLocal = sessionmaker(bind=db)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
