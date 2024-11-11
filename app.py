from src import create_app, db
from src.productos import productos
from src.models import Producto

app = create_app()

with app.app_context():
    db.create_all()  #Creacion De la base de datos

    def cargar_datos(productos):
        for item in productos:
            producto_existente = Producto.query.filter_by(nombre=item['nombre']).first()
            if not producto_existente:
                producto = Producto(
                    nombre=item['nombre'],
                    imagen=item['imagen'],
                    categoria=item['categoria'],
                    precio=item['precio']
                )
                db.session.add(producto)
        db.session.commit()

    cargar_datos(productos)

if __name__ == '__main__':
    app.run(debug=True)
