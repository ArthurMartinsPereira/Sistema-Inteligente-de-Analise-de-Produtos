from repositories.product_repository import ProductRepository as PR
from database.models import Product

repository = PR()

# === Cadastrar Produto===
# produto = Product(
#     sku="TEC005",
#     name="Notebook Acer",
#     price=310000,
#     cost=150000,
#     stock=13,
# )
#
# repository.cadastrar(produto)

# === Listar produtos ===
# produtos = repository.listar()
# for p in produtos:
#     print(p)

# === Atualizar Estoque ===
# repository.atualizar(sku='TEC004', novo_estoque=28)

# === Buscar Produtos ===
# produto = repository.buscar(sku='TEC004')
# if produto:
#     print(produto.name, produto.price)
# else:
#     print("Produto não encontrado!")


# === Remover Produto ===
# repository.remover(sku='TEC005')
