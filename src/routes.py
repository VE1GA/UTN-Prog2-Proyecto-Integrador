from flask import render_template, Blueprint, url_for, jsonify
from src.productos import productos

productos_bp = Blueprint('productos_bp', __name__)

@productos_bp.route('/')
def index() -> str:
    return render_template('index.html')


@productos_bp.route('/remeras')
def remeras():
    remeras = [producto for producto in productos if producto['categoria'] == 'Remeras']
    return render_template('remeras.html', productos=remeras)

@productos_bp.route('/buzos')
def buzos():
    buzos = [producto for producto in productos if producto['categoria'] == 'Buzos']
    return render_template('buzos.html', productos=buzos)

@productos_bp.route('/pantalones')
def pantalones():
    pantalones = [producto for producto in productos if producto['categoria'] == 'Pantalones']
    return render_template('pantalones.html', productos=pantalones)

@productos_bp.route('/accesorios')
def accesorios():
    accesorios = [producto for producto in productos if producto['categoria'] == 'Accesorios']
    return render_template('accesorios.html', productos=accesorios)

@productos_bp.route('/form')
def form():
    return render_template('form.html')