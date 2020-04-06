import mysql.connector
from modelo import constantes_sql
from modelo.clases import Serie

def conectar():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_series"
    )
    return mydb

#metodo que recibe un objeto de la clase Revista para
#registrarla en base de dato
def registro_serie(serie):
    sql = constantes_sql.SQL_INSERCION_SERIE
    mydb = conectar()
    cursor = mydb.cursor()
    #mirando el orden de insert de la sql formo la siguiente
    #tupla con los valores a insertar en base de datos
    val = (serie.titulo, serie.sinopsis, serie.temporadas, serie.lanzamiento, serie.vista)
    
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_series():
    sql = constantes_sql.SQL_LISTADO_SERIES
    mydb = conectar()
    cursor = mydb.cursor()
    cursor.execute(sql)
    resultado_lista = cursor.fetchall() #esto obtiene el resultado de la select
    mydb.disconnect()
    return resultado_lista



