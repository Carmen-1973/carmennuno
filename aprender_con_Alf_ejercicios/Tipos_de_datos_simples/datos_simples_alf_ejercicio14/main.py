"""
Una panadería vende barras de pan a 3.49€ cada una. El 
pan que no es el día tiene un descuento del 60%. Escribir 
un programa que comience leyendo el número de barras 
vendidas que no son del día. Después el programa debe 
mostrar el precio habitual de una barra de pan, el 
descuento que se le hace por no ser fresca y el coste 
final total.

"""
precio_pan = 3.49
dia_anterior = round(precio_pan - (precio_pan * 0.60), 2)
barras_dia_anterior = int(input("¿Cuantas barras vendidas no son del día?"))
print("El precio de una barra del día es " + str(precio_pan) + " euros")
print("Si el pan no es del día tiene un descuento del 60%.")
print("El precio de una barra que no es del día es: " + str(dia_anterior) + " euros")
print("El coste total de las " + str(barras_dia_anterior) + " barras vendidas del día anterior es: " + str(dia_anterior * barras_dia_anterior) + " euros")

