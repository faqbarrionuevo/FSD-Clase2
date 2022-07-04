#me guardo el except en una variable, para ver cual fue y lo printeo

try:
    n = float(input("ingrese numero..."))
    x = 4/n
    print(f"{n} {4} {x}")
except Exception as error:
    print(error)
    print("Ocurrió un error => ", type(error).__name__)