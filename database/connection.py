from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine, expire_on_commit=False)


def init_db():
    from database.models import Product
    Base.metadata.create_all(engine)