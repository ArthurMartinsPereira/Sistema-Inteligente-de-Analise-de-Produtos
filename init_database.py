from database.connection import init_db, engine
from sqlalchemy import inspect

init_db()

inspector = inspect(engine)

print("Tabelas Encontradas:")
print(inspector.get_table_names())