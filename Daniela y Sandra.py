from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

if __name__ == "__main__":
    app.run(debug=True)
    
