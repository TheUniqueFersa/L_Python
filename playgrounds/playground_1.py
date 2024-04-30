def tipo(dato, cadena):
    print(f"-> El dato {cadena}, es un {type(dato)}")
    return 0
# Las operaciones si respetan tipos de datos, es decir, deben ser entre los mismos tipos de datos, 
#por lo menos lo menciono porque str con int no se puede concatenar así nada más
age = input("Ingresa una edad: ")
print("tipo de 'age' {}".format(type(age)))
#total = age + 10 #no se puede hacer, lanza error

age = int(age) #cast a int
print("tipo de 'age' actualizado: {}".format(type(age)))

total = age + 10
print(f"En 10 años, tendré {total} años")

#enteros
entero = 25
tipo(entero, "entero")
#flotantes
flotante = 16.77
tipo(flotante, "flotante")
#bool
booleano = False
print(booleano)
booleano = not booleano
print(booleano)

if type(type(booleano)) == type(type(type(booleano))):
    print("Efectivamente, soy igual")
else :
    print("Nel, al final si soy diferente")

#Operaciones
suma = 10+10 
print(f"{suma} es de tipo {type(suma)}")
resta = 10-10
print(f"{resta} es de tipo {type(resta)}")
multip = 10*2
print(f"{multip} es de tipo {type(multip)}")
division = 10/3
print(f"{division} es de tipo {type(division)}")
division = 10/2 #Devuelve un class 'float' (5.0) :o
print(f"{division} es de tipo {type(division)}")
modulo = 10%2 
print(f"{modulo} es de tipo {type(modulo)}")
division_natural = 10//3 #Devuelve un class 'int' :o
print(f"{division_natural} es de tipo {type(division_natural)}")
potencia = 10**2 #Devuelve un class='int'
print(f"{potencia} es de tipo {type(potencia)}")

#Repeticion de una cadena lol
guat = "Fersi" * 5 #Devuelve un class='str'
print(f"{guat} es de tipo {type(guat)}")

#TIPOS DE DATOS

cadena = "Soy una cadena"
cadena_2 = 'yo tambien'
entero = 16
booleano = True
flotante = 4.2
flout = 0.00000000004 #notación científica
flout_2 = 500000000000000000.0 #notación científica

print("Los tipos de datos son: ")
print(type(cadena), type(entero), type(booleano), type(flotante), type(flout), type(flout_2))
print(flout, flout_2)