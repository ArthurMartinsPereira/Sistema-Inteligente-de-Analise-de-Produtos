from database.models import Category
from database.connection import Session
from sqlalchemy import select, delete

class CategoryRepository:
    def listar(self):
        with Session() as session:
            stmt = select(Category)
            return session.scalars(stmt).all()

    def buscar(self, name: str):
        with Session() as session:
            stmt = select(Category).where(Category.category_name == name)
            return session.scalar(stmt)

    def remover(self, name: str):
        with Session() as session:
            stmt = delete(Category).where(Category.category_name == name)
            result = session.execute(stmt)
            session.commit()
            return result.rowcount > 0
