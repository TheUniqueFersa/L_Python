# try - except
# -------------------------------------------
# APUNTES y pruebas
print("Sirve para cuando quieres manejar excepciones en tu código")

'''
digamos que tenemos una variable que es originalmente cadena
No podríamos aplicar operaciones de números si no aseguramos primero
que es un número, para ello, podremos que hacer:
'''
def parte1():
    var = input("Ingresa un número: ")
    try:
        var = int(var)
        print("Todo bien :)")
    except ValueError:
        print("Esto no es un número, ingresa de nuevo: ")
        var = input("Ingresa un número: ")
    print(var)
# parte1()
# -------------------------------------------
"""
Ahora podremos convertir esto a una función y en ciclo, para que no deje salirse
hasta que sea un número wii
"""
# Ejercicios
def lecturaNumero(entrada): # Método de los tipos (con try-except)
    var = ""
    while type(var) != int: #tal vez hay una condición más fácil
        var = input(entrada)
        try: 
            var = int(var)
            # print(type(var), int) # :Oooo
            # print("Muy bien, esto si es un número :), continua")
        except ValueError:
            print("Esto no es un número, intentalo de nuevo")
    return var

# numero = lecturaNumero("Ingresa un número entero porfi: ")
# -------------------------------------------

def lecturaEntero(entrada): # Con Métodos de str y conversión en caso de número negativo
    var = ""
    negativo = False
    while var.isdigit() != True:
        var = input(entrada)
        if var.startswith('-'):
            negativo = True
            print(f"Antes: {var}")
            var = var.lstrip("-")
            print(F"Después: {var}")
        if var.isdigit() == False:
            print("Esto no es un entero")
    var = int(var)
    if negativo:
        var = -var
    return var
# print(numero)
# print(int("XD")) # Muestra del error ValueError
# print(2/0) # Muestra del error ZeroDivisionError

numero = lecturaEntero("Ingresa: ")
print(numero)
# -------------------------------------------