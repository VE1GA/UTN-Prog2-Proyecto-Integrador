from src import create_app, db
from src.productos import productos
from src.models import Producto

app = create_app()

with app.app_context():
    db.create_all() #Base de datos

    def cargar_datos(productos):
        for item in productos:
            producto = Producto(
                nombre=item['nombre'],
                imagen=item['imagen'],
                categoria=item['categoria'],
                precio=item['precio']
        )
        db.session.add(producto)
    db.session.commit()
    
if __name__ == '__main__':
    app.run(debug = True)


