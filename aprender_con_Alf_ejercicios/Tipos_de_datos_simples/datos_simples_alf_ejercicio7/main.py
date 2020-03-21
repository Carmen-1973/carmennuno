"""
Escribir un programa que pregunte al usuario por el 
número de horas trabajadas y el coste por hora. Después 
debe mostrar por pantalla la paga que le corresponde.
"""

horas = float(input("¿Cuantas horas trabajas al día? "))
paga_hora = float(input("¿Cuanto te pagan por hora? "))
print("Trabajas " + str(horas) + " y cobras " + str(paga_hora) + " por hora.")
paga_dia = horas * paga_hora
print("Al día cobras " + str(paga_dia))


