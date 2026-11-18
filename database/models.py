from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base, engine


class Product(Base):
    __tablename__= 'products'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    sku: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    cost: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    stock: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )
