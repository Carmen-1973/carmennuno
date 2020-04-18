import re

validacion_titulo = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ]{1,50}$"
validacion_sinopsis = "^[0-9a-zA-Z áéíóúÁÉÍÓÚñÑ,\.]{1,150}$"
validacion_temporadas = "^[0-9]{1,9}$"
validacion_lanzamiento = "^[0-9,\.]{1,4}$"
validacion_vista = "^[siSInoNO]{1,2}$"

def validar_titulo(titulo):
    validador_titulo = re.compile(validacion_titulo)
    return validador_titulo.match(titulo)

def validar_sinopsis(sinopsis):
    validador_sinopsis = re.compile(validacion_sinopsis)
    return validador_sinopsis.match(sinopsis)

def validar_temporadas(temporadas):
    validador_temporadas = re.compile(validacion_temporadas)
    return validador_temporadas.match(temporadas)

def validar_lanzamiento(lanzamiento):
    validador_lanzamiento = re.compile(validacion_lanzamiento)
    return validador_lanzamiento.match(lanzamiento)

def validar_vista(vista):
    validador_vista = re.compile(validacion_vista)
    return validador_vista.match(vista)