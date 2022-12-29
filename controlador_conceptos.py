from bd import obtener_conexion

def insertar_concepto(idConcepto, responsabilidad, tipo, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO conceptos(idConcepto, responsabilidad, tipo, descripcion) VALUES (%s, %s, %s, %s)",
                       (idConcepto, responsabilidad, tipo, descripcion))
    conexion.commit()
    conexion.close()

def obtener_conceptos():
    conexion = obtener_conexion()
    conceptos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idConcepto, responsabilidad, tipo, descripcion FROM conceptos")
        conceptos = cursor.fetchall()
    conexion.close()
    return conceptos


def eliminar_concepto(idConcepto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM conceptos WHERE idConcepto = %s", (idConcepto,))
    conexion.commit()
    conexion.close()


def obtener_concepto_por_id(idConcepto):
    conexion = obtener_conexion()
    concepto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idConcepto, responsabilidad, tipo, descripcion FROM conceptos WHERE idConcepto = %s", (idConcepto,))
        concepto = cursor.fetchone()
    conexion.close()
    return concepto


def actualizar_concepto(idConcepto, responsabilidad, tipo, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE conceptos SET responsabilidad = %s, tipo = %s, descripcion = %s WHERE idConcepto = %s",
                       (responsabilidad, tipo, descripcion, idConcepto))
    conexion.commit()
    conexion.close()
