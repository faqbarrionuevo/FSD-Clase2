# defino funcion
def test_fun():
    print("Funcion de test")
    print("Funcion de test 2da linea")

# la llamo
test_fun()

# funcion que recibe parametro, con documentación
def saludo(nombre):
    """Imprime un saludo. Recibe un string con un nombre"""  # para documentacion
    print(f"Hola {nombre}!")

# La llamo con un nombre que ingrese el usuario
nombre = input("Ingrese su nombre...")
saludo(nombre)
# quiero ver que hace la fuiuncion saludo
print("Que hace la función saludo ? ...")
help(saludo)

# funcion que retorne dos valores y tambien reciba 2
def suma_resta(x,y):
    """Recibe dos valores. Retorna la suma y la resta de ellos"""
    suma = x + y
    resta = x - y
    return (suma, resta)


suma, resta = suma_resta(10,5)
print(f"La suma es: {suma} La resta es: {resta}")
suma, resta = suma_resta(y = 3, x = 4) # tambien funciona asi diciendole cada uno
print(f"La suma es: {suma} La resta es: {resta}")

# funcion con valor por defecto
def saludo2 (name = "Facu"):
    print(f"Hola {name}!")

saludo2()  # si no le paso nada me imprime el por defecto
saludo2("Lau") # si le paso algo me imprime lo que le pasé
