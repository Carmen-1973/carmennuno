from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal, listado_series, registro_series,\
    ventana_list_widget, ventana_table_widget, ventana_modificar_series
from modelo.clases import Serie
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton
from modelo.operaciones_bd import obtener_series, guardar_cambios_serie
from _functools import partial
from validaciones import validaciones_series

#variable global
series = None

#metodos de la ventana de registro:
def registrar_serie():
    serie = Serie()
    #recogemos titulo y validación
    serie.titulo = ui_registro_series.entrada_titulo.text()
    if not validaciones_series.validar_titulo(serie.titulo):
        ui_registro_series.label_error_titulo.setText("Error!!!")
        return
    else:
        ui_registro_series.label_error_titulo.clear()
        
    #recogemos sinopsis y validación    
    serie.sinopsis = ui_registro_series.entrada_sinopsis.text()
    if not validaciones_series.validar_sinopsis(serie.sinopsis):
        ui_registro_series.label_error_sinopsis.setText("Error!!!")
        return
    else:
        ui_registro_series.label_error_sinopsis.clear()
        
    #recogemos temporadas y validación
    serie.temporadas = ui_registro_series.entrada_temporadas.text()
    if not validaciones_series.validar_temporadas(serie.temporadas):
        ui_registro_series.label_error_temporadas.setText("Error!!!")
        return
    else:
        ui_registro_series.label_error_temporadas.clear()
        
    #recogemos año de lanzamiento y validación
    serie.lanzamiento = ui_registro_series.entrada_lanzamiento.text()
    if not validaciones_series.validar_lanzamiento(serie.lanzamiento):
        ui_registro_series.label_error_lanzamiento.setText("Error!!!")
        return
    else:
        ui_registro_series.label_error_lanzamiento.clear()
        
    #recogemos si se ha visto o no y validamos    
    serie.vista = ui_registro_series.entrada_vista.text()
    if not validaciones_series.validar_vista(serie.vista):
        ui_registro_series.label_error_vista.setText("Error!!!")
        return
    else:
        ui_registro_series.label_error_vista.clear()
        
    
    #validarla y dar errores
    operaciones_bd.registro_serie(serie)
    
    #limpio los controles
    ui_registro_series.entrada_titulo.setText("")
    ui_registro_series.entrada_sinopsis.setText("")
    ui_registro_series.entrada_temporadas.setText("")
    ui_registro_series.entrada_lanzamiento.setText("")
    ui_registro_series.entrada_vista.setText("")
    
    #indicamos registro ok al usuario
    QMessageBox.about(MainWindow, "Info","Registro serie OK")
    
#metodos del submenu
def mostrar_registro_serie():
    ui_registro_series.setupUi(MainWindow)
    ui_registro_series.btn_registrar_serie.clicked.connect(registrar_serie)
    
def mostrar_listado_series():
    ui_listado_series.setupUi(MainWindow)
    series = obtener_series()
    texto = ""
    for s in series:
        texto += str(s[0]) + "\n" + "Titulo: " + s[1] + "\n" + "Sinopsis:  " + s[2] + "\n" + "Temporadas: " + str(s[3]) + "\n" + "Año Lanzamiento: " + str(s[4]) + "\n" + "Vista(si o no): " + s[5] + "\n"        
    ui_listado_series.listado_series.setText(texto)    
    
def mostrar_listado_list_widget_series():
    global series
    ui_listado_series_list_widget.setupUi(MainWindow)
    series = obtener_series()
    for s in series:
        ui_listado_series_list_widget.listado_series_list_widget.addItem(str(s[1]) + " Temporadas: " + str(s[3]))
    ui_listado_series_list_widget.listado_series_list_widget.itemClicked.connect(ver_detalles_serie)
    
def ver_detalles_serie():
    indice_seleccionado = ui_listado_series_list_widget.listado_series_list_widget.currentRow()
    serie = series[indice_seleccionado]
    texto = ""
    texto += "Título: " + str(serie[1]) + "\n"
    texto += "Sinopsis: " + str(serie[2]) + "\n"
    texto += "Temporadas: " + str(serie[3]) + "\n"
    texto += "Año lanzamiento: " + str(serie[3]) + "\n"
    texto += "Vista: " + str(serie[3]) + "\n"
    
    QMessageBox.about(MainWindow, "Info", texto)
    
def mostrar_table_widget_series():
    ui_listado_series_table_widget.setupUi(MainWindow)
    series = operaciones_bd.obtener_series()
    fila = 0
    for s in series:
        ui_listado_series_table_widget.listado_series_table_widget.insertRow(fila)
        
        indice_celda= 0
        for valor in s:
            celda = QTableWidgetItem(str(valor))
            ui_listado_series_table_widget.listado_series_table_widget.setItem(fila,indice_celda,celda)
            indice_celda += 1
        #agregamos el boton borrar
        boton_borrar = QPushButton("BORRAR")
        boton_borrar.clicked.connect(partial(borrar_serie,s[0]))
        ui_listado_series_table_widget.listado_series_table_widget.setCellWidget(fila,indice_celda,boton_borrar)
        #agregamos el boton editar
        boton_editar = QPushButton("EDITAR")
        boton_editar.clicked.connect(partial(editar_serie,s[0]))
        ui_listado_series_table_widget.listado_series_table_widget.setCellWidget(fila,indice_celda + 1,boton_editar)
        
        fila += 1
        
def borrar_serie(id_a_borrar):
    res = QMessageBox.question(MainWindow, "Alerta!!!", "Vas a borrar el registro con id: " + str(id_a_borrar))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_serie(id_a_borrar)
        mostrar_table_widget_series()
        
def editar_serie(id_a_editar):
    QMessageBox.about(MainWindow, "Info", "Vas a editar el id: " + str(id_a_editar))
    ui_editar_serie.setupUi(MainWindow)
    serie_a_editar = operaciones_bd.obtener_serie_por_id(id_a_editar)
    ui_editar_serie.entrada_titulo.setText(str(serie_a_editar.titulo))
    ui_editar_serie.entrada_sinopsis.setText(str(serie_a_editar.sinopsis))
    ui_editar_serie.entrada_temporadas.setText(str(serie_a_editar.temporadas))
    ui_editar_serie.entrada_lanzamiento.setText(str(serie_a_editar.lanzamiento))
    ui_editar_serie.entrada_vista.setText(str(serie_a_editar.vista))
    
    ui_editar_serie.btn_guardar_cambios.clicked.connect(partial(guardar_cambios_serie, serie_a_editar.id))
     
def guardar_cambios_serie(id_a_guardarCambios):
    QMessageBox.about(MainWindow, "Info", "Guardando cambios en el registro con id: " + str(id_a_guardarCambios))
    serie_a_guardar_Cambios = Serie()
    serie_a_guardar_Cambios.id = id_a_guardarCambios
    serie_a_guardar_Cambios.titulo = ui_editar_serie.entrada_titulo.text()
    serie_a_guardar_Cambios.sinopsis = ui_editar_serie.entrada_sinopsis.text()
    serie_a_guardar_Cambios.temporadas = ui_editar_serie.entrada_temporadas.text()
    serie_a_guardar_Cambios.lanzamiento = ui_editar_serie.entrada_lanzamiento.text()
    serie_a_guardar_Cambios.vista = ui_editar_serie.entrada_vista.text()
    operaciones_bd.guardar_cambios_serie(serie_a_guardar_Cambios)
   
    mostrar_table_widget_series()
    
    

#arranque de la apliccacion principal
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()    

#creo los interfaces
ui_principal = ventana_principal.Ui_MainWindow()
ui_registro_series = registro_series.Ui_MainWindow()
ui_listado_series = listado_series.Ui_MainWindow()
ui_listado_series_list_widget = ventana_list_widget.Ui_MainWindow()
ui_listado_series_table_widget = ventana_table_widget.Ui_MainWindow()
ui_editar_serie = ventana_modificar_series.Ui_MainWindow()


ui_principal.setupUi(MainWindow)

#preparar submenus
ui_principal.submenu_Registrar_Serie.triggered.connect(mostrar_registro_serie)
ui_principal.submenu_Listar_Series.triggered.connect(mostrar_listado_series)
ui_principal.submenu_List_Widget.triggered.connect(mostrar_listado_list_widget_series)
ui_principal.submenu_Table_Widget.triggered.connect(mostrar_table_widget_series)

#mostrar ventana y cerrar aplicacion cuando se cierra
MainWindow.show()
sys.exit(app.exec_())


    

    
