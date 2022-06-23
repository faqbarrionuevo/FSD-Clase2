# funciones pre definidas en el lenguaje, incluyendo modulos
import math
import re
import socket

raiz = math.sqrt(25)
print(f"Raiz cuadrada: {raiz}")

# metodos del modulo
seno = math.sin(25)
expon = math.exp(30) # e a la 30

# variables definidas dentro del modulo
pi = math.pi
e = math.e

# si no quiero el modulo entero, solo quiero sqrt
# para que no me coma tantos recursos el modulo entero por una funcion
from math import sqrt
raiz = sqrt(25) # y la puedo usar sin el punto

from math import sqrt as raiz_cuadrada # y la puedo usar con ese nombre
raiz = raiz_cuadrada(25)

# funcion dentro de otra funcion - no la podria usar de afuera
def cuadrado(x):
    def potencia(y, z):
        return y**z
    return potencia(x,2)

