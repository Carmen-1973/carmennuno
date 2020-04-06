class Serie():
    
    def __init__(self):
        self.titulo = ""
        self.sinopsis = ""
        self.temporadas = 0
        self.lanzamiento = 0
        self.vista = ""
        
    def a_texto(self):
        return "titulo: {} sinopsis: {} temporadas: {} año lanzamiento: {} vista {}".format(self.titulo, self.sinopsis, self.temporadas, self.lanzamiento, self.vista)
    
 
    