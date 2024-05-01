# try - except
print("Sirve para cuando quieres manejar excepciones en tu código")

'''
digamos que tenemos una variable que es originalmente cadena
No podríamos aplicar operaciones de números si no aseguramos primero
que es un número, para ello, podremos que hacer:
'''
var = input("Ingresa un número: ")
try:
    var = int(var)
    print("Todo bien :)")
except ValueError:
    print("Esto no es un número, ingresa de nuevo: ")
    var = input("Ingresa un número: ")
print(var)
