from flask import Flask, render_template, request, redirect

import controlador_conceptos
import controlador_parametros

app = Flask(__name__, template_folder='templates')

@app.route("/agregar_parametro")
def formulario_agregar_parametro():
    return render_template("agregar_parametro.html")


@app.route("/guardar_parametro", methods=["POST"])
def guardar_parametro():
    idParametro = request.form["idParametro"]
    valorParametro = request.form["valorParametro"]
    controlador_parametros.insertar_parametro(idParametro, valorParametro)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/parametros")


#@app.route("/")
@app.route("/parametros")
def parametros():
    parametros = controlador_parametros.obtener_parametros()
    return render_template("parametros.html", parametros=parametros)


@app.route("/eliminar_parametro", methods=["POST"])
def eliminar_parametro():
    controlador_parametros.eliminar_parametro(request.form["idParametro"])
    return redirect("/parametros")


@app.route("/formulario_editar_parametro/<int:idParametro>")
def editar_parametro(idParametro):
    # Obtener el parametro por ID
    parametro = controlador_parametros.obtener_parametro_por_id(idParametro)
    return render_template("editar_parametro.html", parametro=parametro)


@app.route("/actualizar_parametro", methods=["POST"])
def actualizar_parametro():
    idParametro = request.form["idParametro"]
    valorParametro = request.form["valorParametro"]
    controlador_parametros.actualizar_parametro(idParametro, valorParametro)
    return redirect("/parametros")

@app.route("/agregar_concepto")
def formulario_agregar_concepto():
    return render_template("agregar_concepto.html")


@app.route("/guardar_concepto", methods=["POST"])
def guardar_concepto():
    idConcepto = request.form["idConcepto"]
    responsabilidad = request.form["responsabilidad"]
    tipo = request.form["tipo"]
    descripcion = request.form["descripcion"]
    controlador_conceptos.insertar_concepto(idConcepto, responsabilidad, tipo, descripcion)
    return redirect("/conceptos")


#@app.route("/")
@app.route("/conceptos")
def conceptos():
    conceptos = controlador_conceptos.obtener_conceptos()
    return render_template("conceptos.html", conceptos=conceptos)


@app.route("/eliminar_concepto", methods=["POST"])
def eliminar_concepto():
    controlador_conceptos.eliminar_concepto(request.form["idConcepto"])
    return redirect("/conceptos")


@app.route("/formulario_editar_concepto/<int:idConcepto>")
def editar_concepto(idConcepto):
    # Obtener el concepto por ID
    concepto = controlador_conceptos.obtener_concepto_por_id(idConcepto)
    return render_template("editar_concepto.html", concepto=concepto)


@app.route("/actualizar_concepto", methods=["POST"])
def actualizar_concepto():
    idConcepto = request.form["idConcepto"]
    responsabilidad = request.form["responsabilidad"]
    tipo = request.form["tipo"]
    descripcion = request.form["descripcion"]
    controlador_conceptos.actualizar_concepto(idConcepto, responsabilidad, tipo, descripcion)
    return redirect("/conceptos")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
