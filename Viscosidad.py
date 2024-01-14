import math
import time

print("      -------- Proyecto Final -------- \n")
print("      Calculadora de Viscocidad en cilindros         \n")
print("      Juan Camilo Pantoja Villarreal  (221033041)      \n")
print("      Jefferson Duvan Ñañez Portillo  (221033021)      \n")

g = 9.8

W = float(input("Ingrese la fuerza en Newtons: "))

answer = input("Si tiene el valor de la masa pulsar 1, si no, pulsar 2\n")

if answer == "1":
    m = float(input("Poner el valor de la masa en [N/m*s^2]: "))
elif answer == "2":
    m = W / g
else:
    print("Respuesta invalida. Reinicia el programa.\n")
    exit()  # Salir del programa si la respuesta no es válida

a = float(input("ingresa el valor de la desaceleracion [m/s^2]: "))

aws = input("Si tiene el valor del Area pulse 1, sino, pulse 2\n")

if aws == "1":
    A = float(input("Poner el valor del area en [m^2]: "))
elif aws == "2":
    r = float(input("Inserte el valor del radio en [m]: "))
    h = float(input("Inserte el valor de la altura en [m]: "))
    A = r * h * 2 * math.pi
else:
    print("Respuesta invalida. Reinicia el programa.\n")
    exit()  # Salir del programa si la respuesta no es válida

v = float(input("ingrese el valor de la velocidad en [m/s]: "))
l = float(input("ingrese el valor de la capa del lubricante en [m]: "))

niu = ((W + m * a) / (A * v)) * l

for i in range(1, 11):
    time.sleep(0.5)
    print(f"proceso : {'#' * i}{'.' * (10 - i)}{i * 10}% completado", end='\r', flush=True)
print("\nProceso completado")



print("La viscosidad del lubricante es:  " + str(niu) + "  \n")
