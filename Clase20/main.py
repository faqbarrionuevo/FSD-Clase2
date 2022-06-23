print("Practicando Python")

# input
print("Ingrese un número por consola...")
entrada = input ()  # espero entrada del usuario por consola, se queda esperando asi
# siempre devuelve string
print(f"Usted ingresó: {entrada}")
print("Ingrese otro...")
entrada2 = input ()
entrada = int(entrada) # convierto los strings a int
entrada2 = int(entrada2)
resultado = entrada + entrada2
print(f"La suma de los dos números ingresados es: {resultado}")

# lista
lista = list(input("Ingrese lista...")) # va a ser tipo vector
print(f"La lista que ingresó es: {lista}")

# tupla -> es como una lista pero definida por parentesis, pero no se puede editar
tupla = tuple(input("Ingrese una tupla..."))
print(f"La tupla que ingresó es: {tupla}")

# split
entrada = input("Ingrese una lista de numeros...")
vector_num = entrada.split() # los separo y pongo en un vector
print(f"Su lista spliteada es: {vector_num}")
# los guardo directamente en 3 variables diferentes
x, y, z = input("Ingrese 3 numeros separados por esacio...").split()
print(f"Sus valores: {x}, {y}, {z}")

dia, mes, año = input("Ingrese fecha dividida por /: ").split("/")
print(f"Dia: {dia}, Mes: {mes}, Año: {año}")
mail, proveedor = input("Ingrese mail: ").split("@")
print(f"Su proveedor es: {proveedor}")