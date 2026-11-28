from repositories.product_repository import ProductRepository as PR
from repositories.category_repository import CategoryRepository as CR
from database.models import Product, Category

repository = PR()
cat_repository = CR()

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


# === Cadastrar Categoria ===
categoria = Category(
    # o category_id já é aoutoincrementado
    category_name="Limpeza",
    category_description="Todos os produtos de Limpeza"
)

cat_repository.cadastrar(categoria)

# === Listar Categorias ===
categorias = cat_repository.listar()
for c in categorias:
    print(c.category_name, c.category_description)

# === Buscar por Categoria ===
categoria = cat_repository.buscar("Limpeza")
if categoria:
    print(categoria.category_name, categoria.category_description)
else: print("Categoria não encontrada!")

# === Remover Categoria ===
# cat_repository.remover('Limpeza')
