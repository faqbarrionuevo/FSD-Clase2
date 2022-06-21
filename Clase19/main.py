from traceback import print_tb


print("hola mundo con comillas dobles")
print('hola mundo con comillas simples')
print("""hola mundo con comillas triples
Hola
como
va""") # me deja poner texto de muchas lineas (con enter)

# OPERADORES

# float o int son los tipos de números en python

# no hace falta especificar tipo
x = 5
x = 1.2 
print(x + 1)

x = 5
print(x * 2)
print(x / 5)  # el operador dividido ( / ) me lo hace float (agrega el .0 en este caso)
print(x / 3)

print(x // 3) # el // me duevuelve la parte entera
print(x % 3)  # el % me da el resto

print(x**2)   # el ** es potencia 

print(int("6")) # converime el string 6 a entero
print(int(6)) # converime el int 6 a string

x = str(5)
print(type(x))
x = int(x)     # converime el string x a entero
print(type(x))

print(f"mi variable x es igual a {x}") # pongo f adelante del string para indicar que habrá variable

print("C:\nueva_carpeta")
print(r"C:\nueva_carpeta") # el \n es salto de linea, para que no lo vea pongo una r adelante -> manda texto plano, ignora los caracteres especiales

x = 1 or 0 # operaciones logicas se usan literlamente con la palabra
print(x)
y = 1 and 0
print(y)

print("hola" == "hola")
print("hola" != "hola")
print("6" == 6)         # no son del mismo tipo

print(3*"hola")
x = str(" mundo")
print("hola" + x)

x = "hola mundo"
print(x[2])
print(x[-2])
print(x[0:2])           # del 0 a la 2 sin la 2
print(x[0:7:2])         # del 0 al 5 con paso 2
print(x[0::1])          # no le puse nada me toma hasta el final con paso 1
print(x[::-1])          # al revés (doy vuelta un texto)
print(x[-2:])           # del -2 al final 

x = "HOLA MUNDO"
print(x.lower())
print(x.upper())