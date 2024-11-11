from flask import render_template, Blueprint
from src.models import Producto

productos_bp = Blueprint('productos_bp', __name__)

@productos_bp.route('/')
def index() -> str:
    return render_template('index.html')


@productos_bp.route('/remeras')
def remeras():
    remeras = Producto.query.filter_by(categoria='Remeras').all()
    return render_template('remeras.html', productos=remeras)    

@productos_bp.route('/buzos')
def buzos():
    buzos = Producto.query.filter_by(categoria='Buzos').all()
    return render_template('buzos.html', productos=buzos)

@productos_bp.route('/pantalones')
def pantalones():
    pantalones = Producto.query.filter_by(categoria='Pantalones').all()
    return render_template('pantalones.html', productos=pantalones)

@productos_bp.route('/accesorios')
def accesorios():
    accesorios = Producto.query.filter_by(categoria='Accesorios').all()
    return render_template('accesorios.html', productos=accesorios)

@productos_bp.route('/carrito')
def carrito():
    carrito = []
    return render_template('carrito.html')

@productos_bp.route('/form')
def form():
    return render_template('form.html')
