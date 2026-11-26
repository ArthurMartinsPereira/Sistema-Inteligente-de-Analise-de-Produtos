from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.connection import Base


class Product(Base):
    __tablename__= 'products'

    def __repr__(self):
        return (f"<Product(id={self.id}, sku='{self.sku}', name='{self.name}', "
                f"price={self.price}, cost={self.cost}, stock={self.stock})>")

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

    category_id: Mapped[int] = mapped_column(
        ForeignKey('categories.category_id'),
        nullable=False,
    )

    category: Mapped["Category"] = relationship(
        back_populates='products',
    )

class Category(Base):
    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    category_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
    )

    category_description: Mapped[str] = mapped_column(
        String(200),
    )

    products: Mapped[list["Product"]] = relationship(
        back_populates="category",
    )