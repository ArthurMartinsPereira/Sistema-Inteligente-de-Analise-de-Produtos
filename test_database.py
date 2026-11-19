from database.connection import Session, init_db
from database.models import Product
from sqlalchemy import select

init_db()

produto = Product(
    sku="TEC002",
    name="Mouse Gamer",
    price=15000,
    cost=8000,
    stock=20,
)

with Session() as session:
    session.add(produto)
    session.commit()

with Session() as session:
    comando = select(Product)

    resultado = session.execute(comando)

    produtos = resultado.scalars().all()

    for produto in produtos:
        print(produto.name)