# itero sobre lista

# espero a que el usuario ponga "enter"
data = [] #lista

while True:
    line = input()
    if line:
        data.append(int(line)) # si el usuario escribe algo lo meto en la lista en forma de numero
    else:
        break

print(f"Lista ingresada: {data}")