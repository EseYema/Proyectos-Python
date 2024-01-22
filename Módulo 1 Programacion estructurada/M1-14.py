#For and While loops in python
#Link: https://pythones.net/bucles-for-while-sintaxis-ejemplos/

print("****************************************************************************************************************")

#For loop

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for num in numeros:
    if num % 2 == 0: 
        print (num)

print("****************************************************************************************************************")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for num in numeros:
    if num % 2 != 0: 
        print (num)

print("****************************************************************************************************************")

#common uses of For loop
#iterate list

palabras = ['Peine', 'Pelo', 'Ventana', 'Refrigerador', 'Adolescente', 'Dentista', 'Asesino']

for caracteres in palabras:
    print((caracteres), ('###Longitud:'), (len(caracteres)))

print("****************************************************************************************************************")

#iterate dictionaries

agenda = {
    'Marcelo' : '3443456993', 
    'Gaston' : '3443456992', 
    'Lucas' : '3443456991', 
    'Angela' : '3443456990', 
    'Lucio' : '3443456989'}

for (k, v) in agenda.items():
    print(k,':', v)

print("****************************************************************************************************************")

#iterate strings

entrada = "hola estoy programando en python"
contador = 0
cuentaletra = 'a'

for letra in entrada:
    if letra == cuentaletra:
        contador = contador + 1

print((cuentaletra), ':', (contador))

print("****************************************************************************************************************")

#While Loops

#Counter using while

i = 0

while (i<=9):
    i = i +1
    print(i)

#Break
    
while True:
    opcion = (input("""Elige una fruta para tu desayuno:
                    1- manzana
                    2- bananas
                    3- nada
                    """))
    
    if opcion == '1':
        print ( "Has seleccionado manzanas")
        break
    elif opcion == '2':
        print (" Has seleccionado bananas")
        break
    elif opcion == '3':
        print ("Has seleccionado nada")
        break
    else:
        print("Debes seleccionar una opcion (1, 2 o 3)")

print("has llegado al final del programa")

#Continue

"""while True:
    opcion = (input(""""""Elige una fruta para tu desayuno:
                    1- manzana
                    2- bananas
                    3- nada
                    """"""))
    
    if opcion == '1':
        print ( "Has seleccionado manzanas")
        #continue
        break
    elif opcion == '2':
        print (" Has seleccionado bananas")
        break
    elif opcion == '3':
        print ("Has seleccionado nada")
        break
    else:
        print("Debes seleccionar una opcion (1, 2 o 3)")

print("has llegado al final del programa")"""

#Pass

"""while True:
    opcion = (input(""""""Elige una fruta para tu desayuno:
                    1- manzana
                    2- bananas
                    3- nada
                    """"""))
    
    if opcion == '1':
        print ( "Has seleccionado manzanas")
        #pass
        break
    elif opcion == '2':
        print (" Has seleccionado bananas")
        break
    elif opcion == '3':
        print ("Has seleccionado nada")
        break
    else:
        print("Debes seleccionar una opcion (1, 2 o 3)")

print("has llegado al final del programa")"""