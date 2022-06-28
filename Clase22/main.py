# estructuras de datos

lista = [10, "hola", [1,2,3]] #los elementos pueden ser de cual tipo en una lista, hasta otra lista

lista[0] = 15 #vale hacer esto (en strings, por ejemplo, no podría)

x = list(range(0, 10, 2)) # convierto el objeto range a lista
print(x)

nueva_lista = list("hola") # pongo cada letra en ua lista
print(nueva_lista)

y = x[0:10:2] #hago un slicing
print(y)

"1" in "1" # a la izq un valor y a la derecha un arreglo (me fijo si 1 está contenido)

if 2 in [1,2,1,4,5]: # chequeo si 2 está dentro de la lista
    print("true")

x = [1,1,2,3,4,5]

for y in x:  # itero en la lista
    print(y)

lista_0 = [1,2,3] + [4,5,6] # concateno listas
print(lista_0)

lista_1 = [1,2,3]*3 #es como concatenar 3 veces la misma lista
print(lista_1)

x = [1,2,[1,2]]

for i in x:
    print(x)

for i, value in enumerate(x):
    print(1,value)

x = "hola" #le quiero borrar la h al string x -> no pudo con del(x[0]), no puedo indexar
# string -> inmutable
# lista -> mutable
x= [1,2,3]
print(x)
del(x[1])   #borro el 2 de la lsiat x
print(x)

# podria transmofrmar el string en lista, borrar la h y luego volverla a convertir en string
x = "hola"
print(x)
x1 = list(x)
del(x1[0])
x_str = "".join(x1)  # con esto lo transformo a string
print(x_str)

x1 = [1,2,3]
x2 = x1
x2[0] = x1[:] # en la primera posicion lo pongo toda la lista concatenada
print(x2)

# colas (buffer) y pilas (stack)
pila = [1,2,3,4]
pila.append(5) # agrego al final
print(pila)
x = pila.pop() #le saco el ultimo elemento y lo guardo en x
print(pila)
print(x)

pila.append([5,6]) # le appendeo una lista dentro
print(pila)

pila.insert(5,12) # agrego un 2 en la posicion 5
pila.remove([5,6]) # le saco el elemento que le paso
pila.remove(1)
print(pila)

cola = [] # vacia
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)
cola.append(5)
x = cola.pop(0) # si le paso 0 me saca el 0 de la lista, si no le paso nada me saca el ultimo
x = cola.pop(1) # le saco lo que haya en la posicion 1

# matriz
matrix = [[0,1], [2,3]] #matriz sería una lista de listas, donde cada elemento son las filas
print(matrix)

# itero por la matriz
for i in matrix:
    for j in i:
        print(j)

# todo en una linea para definir el valor de una variable
x = 1 if 10 > 0 else 0

# con for en la misma lista lo defino los elementos de una lista
lista = [3*x for x in range(5)] # multiplos de 3 del 1 al 15
print(lista)

lista = [1 for x in range(5)] # un 1 5 veces
print(lista)

lista = [x for x in range(5)] # del 0 al 4
print(lista)

lista_2 = [i-1 for i in lista] # los elementos de la lista anterior restados uno
print(lista_2)

matrix = [(i,j) for i in range(3) for j in range(3)] # creo una matriz
print(matrix)

# tuplas -> es como una lista pero no modificable
# la usaria para cuando quiero juntar cosas (fechas, cartas)
# cuando quiero que la funcion devuelva varias cosas por ejemplo
fecha = (10,2,2022)
print(fecha)

carta_1 = (4, "espada")
print(carta_1)
carta_1[1] # vale
carta_1[-1]
nueva = carta_1[:1] # defino una nueva tupla con slicing
print(nueva)

tupla_1 = (0,) # tupla co un solo valor

# packing y unpacking
valor, palo = carta_1 #unpacking de los elementos, puedo hacerlo sobre una lista tambien
print(valor, palo)

valor = 5
palo = "oro"
carta_2 = valor, palo # packing de la tupla
print(carta_2)

def aleatoria():   #funcion que devuelva carta
    num = 2
    palo = "espada"
    return num,palo

carta_3 = aleatoria()
print(carta_3)

#genero tuplas
for i in enumerate(range(5)):
    print(i)

# diccionarios, es como un json
diccionario = {"key1": 10, "key2": 15}
print(diccionario)
x = diccionario["key1"] # para desrreferenciar, no existe el diccionario.key1
diccionario["key3"] = 20 # agrego uno nuevo
if "key4" in diccionario:
    print("key 4 está en el diccionario")
else:
    print("key4 no está en el diccionario")

x = diccionario.get("key3")

# dos en uno
mapa = {"data": {"info": "pepe"}}
x = mapa["data"]["info"]
mapa.get("data1", {}).get("info", "") # no estará data1, pero no me tirará error

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for i,value in diccionario.items(): # le hago unpacking dentro del for
    print(i, value)

