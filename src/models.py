from . import db
 
class Producto(db.Model): 
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    imagen = db.Column(db.String, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Producto {self.nombre}>"
    
