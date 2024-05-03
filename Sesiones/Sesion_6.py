# # Try - except
# -------------------------------------------------------------------------------
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
"""
print("no".isdigit()) # Devuelve False
print("-2".isdigit()) # Devuelve False
print("3.1".isdigit()) # Devuelve False
print("²".isdigit()) # True
print("۵".isdigit()) # True
print("Ⅳ".isdigit()) # False 
print("⅓".isdigit()) # False

print('-'*25) #separador
print("no".isnumeric()) # False
print("-2".isnumeric()) # False
print("3.1".isnumeric()) # False
print("²".isnumeric()) # True
print("۵".isnumeric()) # True
print("Ⅳ".isnumeric()) # True
print("⅓".isnumeric()) # True
"""

# -------------------------------------------------------------------------------
# Ejercicios
def lecturaNumero(entrada): # Método de los tipos (con try-except)
    var = ""
    while type(var) != int: #tal vez hay una condición más fácil
        var = input(entrada)
        try: 
            var = int(var)
            # print(type(var), int) # :Oooo
            # print("Muy bien, esto si es un número :), continua")
        except ValueError: #Si no se escribe el tipo de error, el bloque entrará en cualquier tipo de error
            print("Esto no es un número, intentalo de nuevo")
    return var

# numero = lecturaNumero("Ingresa un número entero porfi: ")
# -------------------------------------------

def lecturaEntero(entrada): # Con Métodos de str y conversión en caso de número negativo
    var = ""
    negativo = False #Declara booleano para poder determinar si es negativo
    while var.isdigit() != True:
        var = input(entrada)
        negativo = False #Reinicia negativo para que en cada ciclo sea borron y cuenta nueva
        if var.startswith('-'): #Si la cadena proporcionada empieza con '-' puede que sea negativo
            negativo = True #Dice que si es negativo
            print(f"Antes: {var}") #DEP
            var = var.lstrip("-") # le quita a la cadena todos los caracteres del principio que sean '-' -> tal vez allá una mejor manera
            print(F"Después: {var}") #DEP
        if var.isdigit() == False: # Con el negativo removido, verifica si la cadena restante es un número
            print("Esto no es un entero")
    var = int(var) #Una vez que sale del ciclo es porque ya verificó que var es un dígito, por lo que se hace la conversión que ya no tendría ErrorValue
    if negativo: # Si negativo salió con True, entonces var se vuelve negativo
        var = -var
    return var
# print(numero)
# print(int("XD")) # Muestra del error ValueError
# print(2/0) # Muestra del error ZeroDivisionError

numero = lecturaEntero("Ingresa: ")
print(numero)
# -------------------------------------------