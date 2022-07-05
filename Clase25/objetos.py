# si no usaramos objetos (poo)

# clientes = [
#     {"nombre": "leo", "apellido": "messi", "dni": "12345678"},
#     {"nombre": "angel", "apellido": "di maria", "dni": "23456789"},
# ]

# def print_clientes(clientes, dni):
#     for c in clientes:
#         if c['dni'] == dni:
#             print(f"{c['nombre']} {c['apellido']}")
#             break

# def eliminar_clientes(clientes, dni):
#     for i,c in enumerate(clientes):
#         if c['dni'] == dni:
#             print(f"{c['nombre']} {c['apellido']} -> borrado")
#             del(clientes[i])
#             break

# print_clientes(clientes, "12345678")
# eliminar_clientes(clientes, "23456789")
# print(clientes)

# --------------------------------------------------------------

# utilizando poo
# creo la clase Clientes y luego el objeto messi de la clase cliente
class Cliente:
    
    def __init__(self, dni = "00000000", nombre = "pordefecto", apellido = "pordef", dinero="0"): #init es el metodo constructor, se inicializa
        self.dni = dni 
        self.nombre = nombre
        self.apellido = apellido
        self.dinero = dinero

    def __str__(self): #siempre que se usa print se llama a este metodo
        return "Hola soy un cliente"

    def reemplazo_plata(self, plata):
        try: # chequeo que sea un numero
            plata = plata + 1
            self.dinero = plata - 1
        except:
            raise Exception("No ingesaste un numero")
    
    def cargar_plata(self, mas_plata):
        self.dinero += mas_plata

    def descripcion(): # no recibe nada, entonces para llamarlo lo tengo que hacer directamente con el método de la clase, no con un objeto
        print("Esto es un cliente, recibe DNI, nombre, apellido y dinero")

    def desc(self): # este si lo puedo llamar con el objeto, tiene self
        print(f"Soy {self.nombre} {self.apellido}")


messi = Cliente(nombre = "leo", apellido = "messi", dni = "12345678", dinero = 10)
dimaria = Cliente(nombre = "angel", apellido = "di maria", dni = "23456789", dinero = 5)
depaul = Cliente() # me deja crearlo sin pasarle nada porque agregué los por defecto, entonces si no le paso nada configura cn esos
print(messi)
print(messi.dinero)
print(Cliente.descripcion())
print(messi.desc())
#print(type(messi))
dimaria.dinero = 15
dimaria.cargar_plata(15) # sería lo mismo que arriba, pero esta es la forma correcta de hacrlo / para modificar un atributo se hace con un metodo
#dimaria.reemplazo_plata("hola")

class Cliente2:
    pass

x1 = Cliente2()
x2 = Cliente2()

#print(x1)
#print(dir(x1)) #el dir me muestra los atributos y los metodos del objeto x1

class Prueba:
    var = "test"
    def change_var(self, nuevo_var):
        self.var = nuevo_var

test = Prueba()
test.change_var("test2") # cambio el valor de var