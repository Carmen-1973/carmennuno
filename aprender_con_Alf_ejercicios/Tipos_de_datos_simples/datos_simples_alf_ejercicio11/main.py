"""
Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión.

"""

inversion = float(input("Introduce tu inversión: "))
interes = float(input("Introduce el interés anual: "))
años = float(input("Introduce el número de años: "))


capital_final = round(inversion * (interes / 100 + 1) ** años,2)

print("Tu capital obtenido en la inversión es: " + str(capital_final))


