#Garcia Cuevas Jorge Armando
#Version 1.0.0
#Python 3.9.5
#Fecha 19/06/2023
"""Descripcion: Programa que calcula el tiempo de caida libre y la distancia recorrida 
por un objeto en movimiento uniformemente acelerado
"""
#LIBRERIAS
import math
import matplotlib
import matplotlib.pyplot as plt

#Se piden los datos al usuario
d = float(input("Ingrese la distancia en metros: "))
g = 9.8

#Calcular el tiempo en caida libre
t = math.sqrt((2*d)/g)

#t = math.sqrt((-4*g/2*d))/g

#Calculamos la velocidad final
vf = g*t

#Mostramos el resultado con solo dos decimales
print("El tiempo en caida libre es de: ", round(t,2), "segundos")
print("La velocidad final del objeto es de: ", round(vf,2), "m/s")

#Pedimos los datos al usuario
a = float(input("Ingrese la aceleración en m/s2: "))
vi = float(input("Ingrese la velocidad inicial en m/s: "))
vf = float(input("Ingrese la velocidad final en m/s: "))

#Calculamos el tiempo
t = (vf-vi)/a

#Calculamos la distancia
d = (vi*t)+(a*(t**2))/2

#Mostramos el resultado con solo dos decimales
print("El tiempo en caida libre es de: ", round(t,2), "segundos")
print("La distancia recorrida es de: ", round(d,2), "metros")


#Definimos los valores de x, y, z
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Definir el tamaño de la grafica
plt.figure(figsize=(10,10))

#Definir el titulo de la grafica
plt.title("Caida libre y movimiento uniformemente acelerado")

#Definir el nombre de los ejes
plt.xlabel("Tiempo")
plt.ylabel("Distancia")

#Definimos el tipo de grafica
plt.plot(x, y, color="red", linewidth=2, linestyle="-")
plt.plot(x, z, color="blue", linewidth=2, linestyle="-")

#Mostramos la grafica
plt.show()

#Fin del programa
print("Fin del programa")
"""
#sumar la distancia recorrida en caida libre y la distancia recorrida en movimiento uniformemente acelerado y el tiempo total de caida libre y movimiento uniformemente acelerado
"""""
#Pedimos los datos al usuario

#Calculamos el tiempo
tf= t+t2    

#Calculamos la distancia
df= d+d2

#Mostramos el resultado con solo dos decimales
print("El tiempo total de caida libre y movimiento uniformemente acelerado es de: ", round(tf,2), "segundos")
print("La distancia total recorrida es de: ", round(df,2), "metros")


input("Presione enter para salir")

