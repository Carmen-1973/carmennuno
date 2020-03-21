"""
Imagina que acabas de abrir una nueva cuenta de ahorros 
que te ofrece el 4% de interés al año. Estos ahorros 
debido a intereses, que no se cobran hasta finales de 
año, se te añaden al balance final de tu cuenta de 
ahorros. Escribir un programa que comience leyendo la 
cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe 
calcular y mostrar por pantalla la cantidad de ahorros 
tras el primer, segundo y tercer años. Redondear cada 
cantidad a dos decimales.

"""

saldo_inicial = float(input("Introduce tu saldo inicial: "))
interes = 4

saldo_year1 = round(saldo_inicial * (interes / 100 + 1),2)
saldo_year2 = round(saldo_year1 * (interes / 100 + 1), 2)
saldo_year3 = round(saldo_year2 * (interes / 100 + 1), 2)


print("Tu saldo final del primer año es: " + str(saldo_year1))
print("Tu saldo final del segundo año es: " + str(saldo_year2))
print("Tu saldo final del tercer año es: " + str(saldo_year3))

