from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal, listado_series, registro_series
from modelo.clases import Serie
from modelo import operaciones_bd
from PyQt5.QtWidgets import QMessageBox
from modelo.operaciones_bd import obtener_series


#metodos de la ventana de registro:
def registrar_serie():
    serie = Serie()
    serie.titulo = ui_registro_series.entrada_titulo.text()
    serie.sinopsis = ui_registro_series.entrada_sinopsis.text()
    serie.temporadas = ui_registro_series.entrada_temporadas.text()
    serie.lanzamiento = ui_registro_series.entrada_lanzamiento.text()
    serie.vista = ui_registro_series.entrada_vista.text()
    
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
    

#arranque de la apliccacion principal
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()    

#creo los interfaces
ui_principal = ventana_principal.Ui_MainWindow()
ui_registro_series = registro_series.Ui_MainWindow()
ui_listado_series = listado_series.Ui_MainWindow()

ui_principal.setupUi(MainWindow)

#preparar submenus
ui_principal.submenu_Registrar_Serie.triggered.connect(mostrar_registro_serie)
ui_principal.submenu_Listar_Series.triggered.connect(mostrar_listado_series)

#mostrar ventana y cerrar aplicacion cuando se cierra
MainWindow.show()
sys.exit(app.exec_())


    

    
