# loops, solo existen for y while

n = 10

while n<10:
    print(n)

for i in [1,2,5,6]:   # i toma el valor del elemento de la lista, no el indice
    print(i)

enumerate([1,2,3,4])
for i, value in enumerate([5,4,6,2]):
    print(i,value)

range(10) #devuelve una lista con los numeros del 0 al 10 en este caso
for n in range(0,10):  # para hacer un for que quiero n veces
    print(n)

range(0,10,1) # del 0 al 10 con paso de 1
range(0,10,-1) # del 10 al 0

for i in "hola": #itero por cada letra del string
    print(i)

for i in range(20):  # salgo a la quinta iteracion
    print(i)
    if i ==5:
        break

for i in range(10):      # for anidado, dos dimensiones
    for j in range(i,10):
        print(i,j)
        if i == 2:
            break

for i in range(3):      # 3 dimensiones
    for j in range(3):
        for k in range(3):
            print(i,j,k)
        break # breakeo en el for de j
