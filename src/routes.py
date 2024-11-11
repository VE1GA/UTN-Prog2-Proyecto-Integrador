from flask import render_template, Blueprint, session, request, jsonify
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

# @productos_bp.route('/carrito')
# def carrito():
#     carrito = []
#     return render_template('carrito.html')

@productos_bp.route('/form')
def form():
    return render_template('form.html')


@productos_bp.route('/agregar_carrito', methods=['POST'])
def agregar_carrito(): 
        carrito_actual = session.get('carrito', []) #Trae la info de carritos si es que tiene
        datos_carrito = request.get_json() #Va agarrando los productos que se van agregando
        carrito_actual.extend(datos_carrito)
        session['carrito'] = carrito_actual #Actualiza constantemente la Lista 
        return jsonify({'status': 'success'})
    

@productos_bp.route('/carrito') 
def carrito(): 
    carrito = session.get('carrito', []) 
    return render_template('carrito.html', carrito=carrito)

@productos_bp.route('/eliminar_carrito', methods=['POST'])
def eliminar_carrito():

    data = request.get_json()
    productoid = data.get('id')

    carrito_actual = session.get('carrito', [])

    carrito_actual = [producto for producto in carrito_actual if producto['id'] != productoid]

    session['carrito'] = carrito_actual

    return jsonify({'status': 'success'})