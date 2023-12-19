#lists, tuples and range ** listas, tuplas y range (M1-9)
#Link: https://pythones.net/listas-tuplas-python/


print("****************************************************************************************************************")

#listas

Objetos=["casa", "coche", "puerta"]

Numero=[111,222, 333, 444, 555, 666]

List1=[]

#tuplas

Cosas=("casa", "puerta", "reloj", "mesa", "silla", "banco", "cuadro", "alfombra")

Numeros=(1, 2, 3, 4, 55)


#acceso a listas y tuplas

print(Objetos[1])

print(Numero[1])

print(Cosas[1])

print(Numeros[1])

print("****************************************************************************************************************")
#trozos de listas y tuplas

print(Objetos[1:3])

print(Numero[1:3])

print(Cosas[1:3])

print(Numeros[1:3])

print(Numeros[:-3])

print("****************************************************************************************************************")
#modificacion append

Lista1=["Marcos", "Roberto", 'Celeste', 'Margarita']

print(Lista1)

Lista1.append('Alex')

print(Lista1)

print("****************************************************************************************************************")
#modificacion extend

Lista2=["Marcos", "Roberto", 'Celeste', 'Margarita']

print(Lista2)

Lista2.extend('JOSE')

print(Lista2)

Lista11=[1, 2, 3]
Lista22=[4, 5, 6]

Lista11.extend(Lista22)

print(Lista11)

print("****************************************************************************************************************")
#modificacion insert

Lista1=["Marcos", "Roberto", 'Celeste', 'Margarita']

print(Lista1)

Lista1.insert(1, 'Alex')

print(Lista1)

print("****************************************************************************************************************")
#eliminacion pop

Lista1=["Marcos", "Roberto", 'Celeste', 'Margarita']

print(Lista1)

Lista1.pop(1)

print(Lista1)

print("****************************************************************************************************************")
#eliminacion remove

print(Lista1)

Lista1.remove("Marcos")

print(Lista1)

print("****************************************************************************************************************")
#range

x=list(range(5))

print(x)

y=list(range(2,20,2))

print(y)

y.insert(0,1)

print(y)

print("****************************************************************************************************************")