class Serie():
    
    def __init__(self, titulo = "", sinopsis = "", temporadas = 0, lanzamiento = 0, vista = "", id = 0):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.temporadas = temporadas
        self.lanzamiento = lanzamiento
        self.vista = vista
        self.id = id
        
    def a_texto(self):
        return "titulo: {} sinopsis: {} temporadas: {} año lanzamiento: {} vista: {}".format(self.titulo, self.sinopsis, self.temporadas, self.lanzamiento, self.vista)
    
 
    