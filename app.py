from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Función para leer los datos del CSV
def cargar_clientes():
    with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

@app.route('/', methods=['GET', 'POST'])
def index():
    clientes = []
    if request.method == 'POST':
        dni_buscado = request.form['dni']
        todos = cargar_clientes()
        clientes = [c for c in todos if c['dni'] == dni_buscado]
    return render_template('index.html', clientes=clientes)

@app.route('/detalle/<dni>')
def detalle(dni):
    clientes = cargar_clientes()
    cliente = next((c for c in clientes if c['dni'] == dni), None)
    return render_template('detalle.html', cliente=cliente)

if __name__ == '__main__':
    app.run(debug=True)