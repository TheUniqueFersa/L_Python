#Por fin python!! Comentario de línea

#Declarar una función:

def saluda(nombre):
    #edad = input ("¿Cuál es tu edad? ")
    edad = 23
    k=0
        
    print(id(nombre), id(edad))

def suma(x):
    print(id(x))
    x = x+[10, 20, 30]
    print(id(x))
    r=0
    for valor in x:
        r = r+valor
    return r,x
v = [1,2,3,4,5,6]
res = suma(v)
print(type(res))
print(res)
#---------------------------------
#Comentario de bloque


"""
Q
"""

nombre = 'fersa'
#print("XDDDDD")

#Imprimir con formato
print(f"Hola {nombre}")
#Nótese que la f indica un formato


cadena = "Soy una cadena"
#cadena2 = `Papu no soy cadena :v`

#Input te añade un salto de línea implicito:
print("ID original: ", id(nombre))
saluda(nombre)



#Estructuras de control básicas:
#For
    #El range es un objeto
for k in range(0,3):
    print("XD")
for k in [0,1,0,1,0,1]:
    print("XD")
    #Hace 6 impresiones
for k in [0,1,2.5,"que onda", 0]:
    print(f"Apoco si tilin: {k}")

k=0
#while  
while k<3:
    print(f"El tilinazo de {nombre}", end=' ')

#if
if k<30:
    print(f"Nombre")

#no esxiste switch pipIPI, pero existen los DICCIONARIOS :)

#Listas
[0,1,2]
["El papu", 1, 'punto com', id(nombre), "lol", 5.4]

#Sets
