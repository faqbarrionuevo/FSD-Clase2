# Archivos

f = open("archivo.txt", "w") # si no existe lo crea, con la w le digo que lo abra en modo lectura
# con modo w me inicia a escribir al principio, para escirbir atras es modo append

f.write("Mi primera linea\n")
f.write("otra cosa\n")

f.writelines("Holi")

f = open("archivo.txt", "a") # para que me escriba atras
f.write("mas lineas")

f = open("archivo.txt", "a+") # con el más lo abro en modo write + read,y le pngo la a para escribir atras
#print(f.readlines())
print(f.read(6)) # me lee hasta 6 caracteres, me lee al final porq ahí está el puntero, ya que le abrí con "a", append

f = open("archivo.txt", "r") # lo abro con r para que el puintero esté al ppio
print(f.read(6)) # me lee hasta 6 caracteres

# Funcion que me copie de un archivo a otro
def copiar(file1_name, file2_name): # que copie de un archivo al otro
    f1 = open(file1_name, "r")
    f2 = open(file2_name, "w")

    text = None

    while text != "":        #cuando termina de leer el archivo me va a devolver un string vacio
        text = f1.read(1)
        f2.write(text)
    f1.close()
    f2.close()

copiar("archivo.txt", "copia.txt")

f = open("copia.txt", "a+")
print(f.readlines())   # el read lines devuelve una lista donde cada elemento es una linea del archivo (devuelve todas las lineas)
# los elementos tienen el barra n, lo tendría que sacar luego

#escribo 10 lineas iguales en el archivo
f = open("newfile.txt", "w")
f.write("".join(["Probando\n" for x in range(10)]))

# otra forma de hacer lo mismo
f = open("newfile.txt", "w")
for i in range(10):
    f.write("Probando\n")

f = open("newfile.txt", "r")
print(f.readline()) # una sola linea + el enter
print(f.readline(5)) # leo 5 caracteres

# voy imprimiendo todas las lineas
for i in range(10):
    print(f.readline())

#otra forma
for line in f:
    print(line)

#otra forma y abriendo el archivo de una nueva forma, con with
with open("copia.txt", "r") as f:
    for line in f:
        print(line)

# abrir un archivo y borrarle los comments, crear uno nuevo sin los comments
def sacarComentario(file = "func.txt"):
    pure = open("sincomments.txt", "w")
    with open(file, "r") as f:
        for i in f: #itero por las lineas
            if i.strip().startswith("#"): # la borraría solo si empieza con # / strip me devuelve una copia del sting sin los espacios del principio
                pass #podria poner continue tamb
            else:
                pure.write(i) #escribo la linea en el nuevo (en el q tndré sin comment)



sacarComentario()

# trabajando con un csv
with open("phonebook.csv") as f:
    for line in f:
        print(line.split(','))

#otra forma
import csv

friends = []
f = open("phonebook.csv", "r")
file = csv.reader(f)
print(file)
for Nombre, Apellido, Telefono, Cumpleaños in file:
    friends.append((Nombre, Apellido, Telefono, Cumpleaños))
f.close()

print(friends)

# escribir con la libreria csv
nuevos = [("Maxi","Zitelli","1234-3456","12-12-1222")] #creo una lista de tuplas
filenew = open("phonebook.csv", "a")
file = csv.writer(filenew)
file.writerow([])
file.writerows(nuevos)
filenew.close()

#sin liberia
with open("phonebook.csv", "a") as f:
    for people in nuevos:
        f.write(f"{people[0]},{people[1]},{people[2]},{people[3]}")