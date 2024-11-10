from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/remeras')
def remeras():
    return render_template('remeras.html')

@app.route('/buzos')
def buzos():
    return render_template('buzos.html')

@app.route('/pantalones')
def pantalones():
    return render_template('pantalones.html')

@app.route('/accesorios')
def accesorios():
    return render_template('accesorios.html')

@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug = True)