import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='MySQLH3rm1r@j',
                                db='calculadora')
