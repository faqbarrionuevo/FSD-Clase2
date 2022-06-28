
# imprimir triangulo rectangulo de altura que ingrese el usuario
# |\
# | \
# |  \
# |___\

numero = int(input("Ingrese altura del triangulo..."))
for i in range(numero):
    if i == numero - 1:
        print("|"+i*"_"+"\\")
    else:
       print("|"+i*" "+"\\") 


