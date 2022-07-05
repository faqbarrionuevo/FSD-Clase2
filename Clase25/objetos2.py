
class Cliente:
    
    def __init__(self, dni = "00000000", nombre = "pordefecto", apellido = "pordef", dinero=0): #init es el metodo constructor, se inicializa
        self.dni = dni 
        self.nombre = nombre
        self.apellido = apellido
        self.dinero = dinero

    def __str__(self): #siempre que se usa print se llama a este metodo
        return f"{self.dni} - {self.apellido} {self.nombre}"

    def __init__(self):
        return self.dinero
    
    def __float__(self):
        return float(self.dinero)

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


class Agenda:
    clientes = []

    def __init__(self, clientes):
        self.clientes = clientes
    
    def __str__(self): # que me imprima la lista de clientes
        lista_str = ""
        for client in self.clientes:
            lista_str += (f"{client}, {float(client)}\n")
        return lista_str

    def print_cliente(self, dni):
        ret_value = "No existe ese dni en la agenda"
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                ret_value = str(c)
                break
        print(ret_value)
    
    def eliminar_cliente(self, dni):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                break

messi = Cliente(nombre = "leo", apellido = "messi", dni = "12345678", dinero = 10)
dimaria = Cliente()
print(f"{messi} \n{dimaria}")

Cliente.descripcion()

agenda = Agenda([messi, dimaria])
print(agenda)

agenda.print_cliente(messi.dni)
agenda.print_cliente("40392736")

agenda.eliminar_cliente(dimaria.dni)
print(agenda)
