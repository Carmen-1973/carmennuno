

"""
Escribir un programa que pida al usuario dos números 
enteros y muestre por pantalla la <n> entre <m> da un 
cociente <c> y un resto <r> donde <n> y <m> son los 
números introducidos por el usuario, y <c> y <r> son 
el cociente y el resto de la división entera 
respectivamente.

"""

n = int(input("Introduce un número entero n: "))
m = int(input("Introduce otro número entero m: "))
c = n / m
r = n % m
print("El cociente de n/m es: " + str(c))
print("El resto de la division entera n/m es: " + str(r))
