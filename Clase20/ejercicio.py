
n1 = 2
n2 = 2

while True:
    opcion = input("Ingrese opcion...")
    opcion = int(opcion)
    if opcion == 1:
      print("La suma de",n1,"+",n2,"es",n1 + n2)
    elif opcion == 2:
       print("La resta de",n1,"-",n2,"es",n1 - n2)
    elif opcion == 3:
       print("El producto de",n1,"*",n2,"es",n1 * n2)
    else:
       print("Opcion incorrecta")
       break