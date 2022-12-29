from bd import obtener_conexion

def insertar_parametro(idParametro, valorParametro):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO parametros(idParametro, valorParametro) VALUES (%s, %s)",
                       (idParametro, valorParametro))
    conexion.commit()
    conexion.close()

def obtener_parametros():
    conexion = obtener_conexion()
    parametros = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idParametro, valorParametro FROM parametros")
        parametros = cursor.fetchall()
    conexion.close()
    return parametros


def eliminar_parametro(idParametro):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM parametros WHERE idParametro = %s", (idParametro,))
    conexion.commit()
    conexion.close()


def obtener_parametro_por_id(idParametro):
    conexion = obtener_conexion()
    parametro = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idParametro, valorParametro FROM parametros WHERE idParametro = %s", (idParametro,))
        parametro = cursor.fetchone()
    conexion.close()
    return parametro


def actualizar_parametro(idParametro, valorParametro):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE parametros SET valorParametro = %s WHERE idParametro = %s",
                       (valorParametro, idParametro))
    conexion.commit()
    conexion.close()
