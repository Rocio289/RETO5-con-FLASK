from flask import render_template, request, abort
from miapp.utils import leer_clientes

def init_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def index():
        clientes = []
        mensaje = None

        if request.method == "POST":
            dni = request.form.get("dni", "").strip()

            if not dni:
                mensaje = "Por favor, introduce un DNI válido."
            else:
                for cliente in leer_clientes():
                    if cliente.get("dni") == dni:   
                        clientes.append(cliente)
                        break
                if not clientes:
                    mensaje = f"No se encontró cliente con DNI: {dni}"

        return render_template("index.html", clientes=clientes, mensaje=mensaje)

    @app.route("/cliente/<dni>")
    def cliente(dni):
        for cliente in leer_clientes():
            if cliente.get("dni") == dni:   
                return render_template("detalle.html", cliente=cliente)
        abort(404)

    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return render_template("404.html"), 404