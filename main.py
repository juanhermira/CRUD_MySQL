from flask import Flask, render_template, request, redirect
import controlador_juegos

app = Flask(__name__, template_folder='templates')

@app.route("/agregar_parametro")
def formulario_agregar_parametro():
    return render_template("agregar_juego.html")


@app.route("/guardar_parametro", methods=["POST"])
def guardar_parametro():
    idParametro = request.form["idParametro"]
    valorParametro = request.form["valorParametro"]
    controlador_juegos.insertar_parametro(idParametro, valorParametro)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/parametros")


@app.route("/")
@app.route("/parametros")
def parametros():
    parametros = controlador_juegos.obtener_parametros()
    return render_template("juegos.html", parametros=parametros)


@app.route("/eliminar_parametro", methods=["POST"])
def eliminar_parametro():
    controlador_juegos.eliminar_parametro(request.form["idParametro"])
    return redirect("/parametros")


@app.route("/formulario_editar_parametro/<int:idParametro>")
def editar_parametro(idParametro):
    # Obtener el parametro por ID
    parametro = controlador_juegos.obtener_parametro_por_id(idParametro)
    return render_template("editar_juego.html", parametro=parametro)


@app.route("/actualizar_parametro", methods=["POST"])
def actualizar_parametro():
    idParametro = request.form["idParametro"]
    valorParametro = request.form["valorParametro"]
    controlador_juegos.actualizar_parametro(idParametro, valorParametro)
    return redirect("/parametros")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
