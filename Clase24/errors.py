try:
    n = float(input("ingrese numero..."))
    x = 4/n
    print(f"{n} {4} {x}")
except:
    print("Error")
    n = float(input("ingrese un número correcto..."))
    x = 4/n
finally:
    print("número ingresado y procesado correctamente")
    print(x)


# loop hasta que el usuario lo haga bien, maximo de 3 intentos
print("\nCaso 2")

max_intentos = 3
intentos = 0

while intentos < max_intentos:
    try:
        n = float(input("ingrese numero..."))
        x = 4/n
        print(f"{n} {4} {x}")
        break
    except:
        print("error")
        intentos += 1
    finally:
        print("fin de la iteración")


# me guardo el except en una variable, para ver cual fue y lo printeo
print("\nCaso 3")

# me agarraría la primera excpeción que se cumpla, es como un else if
try:
    n = float(input("ingrese numero..."))
    x = 4/n
    print(f"{n} {4} {x}")
except ZeroDivisionError as e:
    print("No está permitido dividir por cero => ", e)
except ValueError as e:
    print("No está permitido ingresar una palabra => ", e)
except Exception as error:  # un error en general, cualquiera sea
    print(error)
    # veo que tipo de excpepción es
    print("Ocurrió un error => ", type(error).__name__)
    print(f"{type(error).__name__}: {error}")
finally:
    print("Salgo")

# chequeo un error custom, definido por mi
print("\nCaso 4")

# sin error cuatom


def func(x=None):
    if x in None:
        print("Error, no me pasaste nada")
        return
    return x + 10


# no le paso nada
func()


def error_custom(x=None):
    if x is None:
        raise ValueError("Error, no me pasaste nada")
    return x + 10


# no le paso nada con un error custom
error_custom()


def func2(x=None):
    if x is None:
        raise ZeroDivisionError("Error, no me pasaste nada")
    error_custom(x)


try:
    func2()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError nivel 1")
