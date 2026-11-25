from repositories.product_repository import ProductRepository as PR
from database.models import Product

repository = PR()

# === Cadastrar Produto===
# produto = Product(
#     sku="TEC004",
#     name="Placa de Vídeo NVidia",
#     price=31000,
#     cost=12000,
#     stock=25,
# )
#
# repository.cadastrar(produto)

# === Listar produtos ===
list = repository.listar()
for p in list:
    print(p)

# === Buscar Produtos ===
repository.buscar(sku='1')

