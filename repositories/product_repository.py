from database.connection import Session
from database.models import Product
from sqlalchemy import select, delete

class ProductRepository:
    def cadastrar(self, produto):
        with Session() as session:
            session.add(produto)
            session.commit()

    def listar(self):
        with Session() as session:
            stmt = select(Product) # stmt abbreviation for "statement"
            return session.scalars(stmt).all()

    def atualizar(self, sku, novo_estoque):
        with Session() as session:
            stmt = select(Product).where(Product.sku == sku)
            product = session.scalar(stmt)

            if product:
                product.stock = novo_estoque
                session.commit()
                return product
            else:
                return None

    def buscar(self, sku: str):
        with Session() as session:
            stmt = select(Product).where(Product.sku == sku)
            return session.scalar(stmt)

    def remover(self, sku: str):
        with Session() as session:
            stmt = delete(Product).where(Product.sku == sku)

            result = session.execute(stmt)
            session.commit()

            return result.rowcount > 0


