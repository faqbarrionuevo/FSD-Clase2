# ------------------------ Herencia -------------------------------------
class Producto:
    def __init__(self, referencia, nombre, precio): #no necesariamente tiene autor, si no es un libre no
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto - {self.nombre}"


manzana = Producto(referencia="000", nombre="manzana", precio=10)

print(manzana)

# hacemos clase que herede de la clase producto

class Fruta(Producto):
    def __init__(self, estacion, referencia, nombre, precio):
        self.estacion = estacion
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Fruta - {self.nombre} - {self.estacion}"

    def pelar(self):
        print(f"Pelando la {self.nombre}...")

naranja = Fruta(referencia="001", nombre="naranja", precio=10, estacion="invierno")

print(naranja) 
naranja.pelar()

print(isinstance(manzana,Producto))
print(isinstance(manzana,Fruta))
print(isinstance(naranja,Producto))
print(isinstance(naranja,Fruta))

productos = [manzana, naranja] # una lista de productos, son del mismo tipo ya que son Productos (auqne ademas naranaja en Fruta)

for x in productos:
    print(x)

# clase base "vehiculo", después hago otras clases que hereden de esta"
class Vehiculo():
    def __init__(self, precio):
        self.precio = precio

    def mover(self):
        pass

class Auto(Vehiculo):
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio
    
    def __str__(self):
        return f"Auto - {self.marca}"

    def mover(self):
        print("Mover las 4 ruedas del auto")

class Camioneta(Vehiculo):
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio
    
    def __str__(self):
        return f"Camioneta - {self.marca}"

    def mover(self):
        print("Mover las 4 ruedas de la camioneta")

class Concesionario():
    def __init__(self, vehiculos):
        self.vehiculos = vehiculos
    
    def __str__(self):
        return "".join([f"{x}\n" for x in self.vehiculos])

    def __lt__(self, concesionario):
        precio1 = sum([x.precio for x in self.vehiculos])
        precio2 = sum([x.precio for x in concesionario.vehiculos])
        return precio1 < precio2
    
    def __gt__(self, concesionario):
        precio1 = sum([x.precio for x in self.vehiculos])
        precio2 = sum([x.precio for x in concesionario.vehiculos])
        return precio1 > precio2

    def __add__ (self, concesionario):
        return Concesionario(self.vehiculos + concesionario.vehiculos)

    def mudar (self):
        for x in self.vehiculos:
            x.mover()

cons = Concesionario([Auto("Audi", 1000), Camioneta("BMW", 1400)])
print(cons)
cons2 = Concesionario([Auto("Mercedes", 1200), Camioneta("Ferrari", 1250)])
print(cons > cons2) # aqui utilizo __lt__: lower than y __gt__: grater than 
cons3 = cons + cons2
print("Fusion: ", cons3) # aqui utilizo __add__

cons.mudar()

from copy import copy
x = Auto("Ford", 130)

y = copy(x) # no puedo usar y = x -> tengo que usar copy
y.marca = "Chevrolet"
print(x,y)

print(x == y)
