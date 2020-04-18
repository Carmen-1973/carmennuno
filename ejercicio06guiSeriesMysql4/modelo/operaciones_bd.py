import mysql.connector
from modelo import constantes_sql, clases

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

def borrar_serie(id):
    sql = constantes_sql.SQL_BORRAR_SERIE
    mydb = conectar()
    cursor = mydb.cursor()
    val = (id,)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_serie_por_id(id):
    sql = constantes_sql.SQL_OBTENER_SERIE_POR_ID
    mydb = conectar()
    cursor = mydb.cursor()
    val = (id,)
    cursor.execute(sql,val)
    serie_obtenida = cursor.fetchone()
    print(serie_obtenida)
    mydb.disconnect()
    objeto_serie = clases.Serie(id = serie_obtenida[0], titulo = serie_obtenida[1], \
        sinopsis = serie_obtenida[2], temporadas = serie_obtenida[3], \
        lanzamiento = serie_obtenida[4], vista = serie_obtenida[5])
    return objeto_serie    

def guardar_cambios_serie(serie):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_SERIE
    mydb = conectar()
    cursor = mydb.cursor()
    val = (serie.titulo, serie.sinopsis, serie.temporadas, serie.lanzamiento, serie.vista, serie.id)
    cursor.execute(sql,val)
    mydb.commit()
    mydb.disconnect()
