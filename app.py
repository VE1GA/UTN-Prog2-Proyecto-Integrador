from src import create_app, db
from src.productos import productos
#from flask import Flask, render_template

app = create_app()

with app.app_context():
    db.create_all() #Base de datos

if __name__ == '__main__':
    app.run(debug = True)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/remeras')
# def remeras():
#     remeras = [producto for producto in productos if producto['categoria'] == 'Remeras']
#     return render_template('remeras.html', productos=remeras)

# @app.route('/buzos')
# def buzos():
#     buzos = [producto for producto in productos if producto['categoria'] == 'Buzos']
#     return render_template('buzos.html', productos=buzos)

# @app.route('/pantalones')
# def pantalones():
#     pantalones = [producto for producto in productos if producto['categoria'] == 'Pantalones']
#     return render_template('pantalones.html', productos=pantalones)

# @app.route('/accesorios')
# def accesorios():
#     accesorios = [producto for producto in productos if producto['categoria'] == 'Accesorios']
#     return render_template('accesorios.html', productos=accesorios)

# @app.route('/form')
# def form():
#     return render_template('form.html')
