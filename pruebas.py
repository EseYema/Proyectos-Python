#crear y ejecutar archivo .py (M1-6)
print("****************************************************************************************************************")

print("Este es un archivo.py creado en Visual Studio Code.")

print("****************************************************************************************************************")

#declaracion de variables (M1-8)

print("****************************************************************************************************************")

caja1="Hola Pin Pon"
caja2=18
caja3=18.1
caja4=True

print("La variable caja1 es de tipo ", type(caja1),"y contiene: ", caja1)

print("La variable caja2 es de tipo ", type(caja2), "y contiene: ", caja2)

print("La variable caja3 es de tipo ", type(caja3), "y contiene: ", caja3)

print("La variable caja4 es de tipo ", type(caja4), "y contiene: ", caja4)

print("****************************************************************************************************************")
print("****************************************************************************************************************")

caja1=22
caja2=105.9
caja3=False
caja4="True"

print("La variable caja1 es de tipo ", type(caja1),"y contiene: ", caja1)

print("La variable caja2 es de tipo ", type(caja2), "y contiene: ", caja2)

print("La variable caja3 es de tipo ", type(caja3), "y contiene: ", caja3)

print("La variable caja4 es de tipo ", type(caja4), "y contiene: ", caja4)

print("****************************************************************************************************************")

#listas, tuplas y range (M1-9)

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

#diccionarios (M1-10)

print("****************************************************************************************************************")

MiDiccionario={
    'Nombre' : 'Margarita',
    'Edad' : 55,
    'Genero' : 'Femenino'
}

#acceso a diccionarios

MiMarga={
    'Nombre' : 'Margarita',
    'Apellido' : 'Filosa',
    'Alias' : 'Cuchillos',
    'Padres' : ["Maria Chaira", "Carlos Cortez"],
    'Edad' : 55,
    'Genero' : 'Femenino',
    'Estado Civil' : 'Soltera',
    'Hijos' : 'Ninguno/a',
    'Mascotas' : 'Gatos',
    'Nombres de mascotas' : ["Mango", "Doble Filo"]
}

print(MiMarga['Apellido'])

print("****************************************************************************************************************")
#acceso a listas dentro de diccionarios

print(MiMarga['Padres'][0:2])

print("****************************************************************************************************************")
#modificar datos de diccionarios: agregar, reemplazar y modificar elementos

MiMarga['Ingresos'] = '16000'

#modificar valor de clave

MiMarga['Ingresos'] = '20000'

#modificar nombre de la clave

MiMarga['Salario'] = MiMarga.pop('Ingresos')

#eliminar par clave:valor

#del(MiMarga['Nombre'])

print("****************************************************************************************************************")

#metodos
#get()

print(MiMarga.get('Nombre', "Valor por defecto"))

apellido=MiMarga.get('Apellido', "Valor por defecto")

print(apellido)

#keys() y values()

claves = MiMarga.keys()

print(claves)

valores = MiMarga.values()

print(valores)

print("****************************************************************************************************************")

#condicionales: if, else, elif (M1-11)

print("****************************************************************************************************************")

#IF

a= 2 + 2
b= 4

if a == b:
    print("A es igual a ", b)

#IF y ELSE

a= 2 + 3
b= 4

if a == b:
    print("A es igual a ", b)

else:
    print("A no es igual a 4, es igual a ", a)

#IF, ELIF y ELSE

a= 3 + 4
b= 4
c= 5
d= 6

if a == b:
    print("A es igual a ", b)

elif a == c:
    print("A no es igual a", b, ", es igual a ", c)

elif a == d:
    print("A no es igual a", b, ", ni a ", c , ", es igual a ", d)

else:
    print("A no es igual ni a ", b, ", ni a ", c, ", ni a ", d)

print("****************************************************************************************************************")

#operadores: aritmeticos, comparacion, asignacion, logicos y especiales (M1-12)

print("****************************************************************************************************************")

#aritmeticos: suma (+), resta (-), multiplicacion (*), division (/), modulo (%) [devuelve el resto de la division], 
#exponente (**) [exponencial de un numero], division (//) [devuelve el entero de la division]

print((12), ('+'), (14))
print((12), ("es un operando,"), ('+ es un operador y'), (14), ("es un operando"))
print("resultado: ", (12+14))

a= 15
b= 14
print(a, ('+'), b)
print(a, ("es un operando,"), ('+ es un operador y'), b, ("es un operando"))
print("resultado: ", (a+b)) #los demas operadores funcionan igual que la suma (+), pero arrojan resultados distintos

print("****************************************************************************************************************")

#comparacion [devuelven True/False]: igual (==), diferente (!=), mayor que (>), menor que (<), mayor o igual que (>=) y
#menor o igual que (<=)

dinero_comprador= 100

if(dinero_comprador >= 25):
    print("Compra realizada")
    dinero_comprador= dinero_comprador - 25
    print("Tu saldo es", dinero_comprador)
else:
    print("No tienes saldo suficiente.")

print("****************************************************************************************************************")

#asignacion: = asigna valor, += suma al primer elemento el segundo, -= resta al primer elemento el segundo, *= multiplica el
#primer elemento por el segundo, /= divide el primer elemento entre el segundo, %= el primer elemento es igual al modulo del 
#primer elemento entre el segundo, **= el primer elemento es igual al resultado del exponente del primer elemento.

#ejemplos

a = 10
print(a)
a += 1 # a = a+1 es decir a=11
print(a)
a -= 1 # a = a-1 es decir a=10; es igual a 10 porque antes se le sumó 1 y ahora se le resta
print(a)
a *= 2 # a = a*2 es decir a=20
print(a)
a /= 2 # a = a/2 es decir a=10
print(a)
a %= 2 # a = a%2 es decir a=0
print(a)
a = 10 # restauro el valor inicial de a para poder seguir con un valor mayor que 0
print(a)
a **= 2 # a = a**2 es decir a=100
print(a)

#otro ejemplo

año_nacimiento = 1991
mes_nacimiento = 8
año_actual = 2023
mes_actual = 9

if mes_actual<mes_nacimiento:
    edad = año_actual - año_nacimiento
    edad -=1
    print("edad",edad)
elif mes_actual>=mes_nacimiento:
    edad = año_actual - año_nacimiento
    print("edad",edad)

print("****************************************************************************************************************")

#logicos: and, or, not (devuelven true o false)

#ejemplo mayoria edad

hombres_edad = 21
mujeres_edad = 18
carlos_edad = 23
juan_edad = 18
marita_edad = 29

if carlos_edad > hombres_edad and juan_edad > hombres_edad and marita_edad > mujeres_edad:
    print("Pueden pasar los 3 porque cumplen la edad minima")

else:
    print("Alguno no tiene la edad minima")

if carlos_edad < hombres_edad or juan_edad < hombres_edad or marita_edad < mujeres_edad:
    print("No pueden pasar los 3 porque alguno no cumplen la edad minima") 

else:
    print("Pueden pasar los 3 porque cumplen la edad minima")

if juan_edad > hombres_edad:
    print("Juan puede pasar, tiene", juan_edad)

else:
    print("Juan no puede pasar porque tiene", juan_edad)

if marita_edad > mujeres_edad:
    print("Marita puede pasar, tiene", marita_edad)

else:
    print("Marita no puede pasar porque tiene", mujeres_edad)

if carlos_edad > hombres_edad:
    print("Carlos puede pasar, tiene", carlos_edad)

else:
    print("Carlos no puede pasar porque tiene", carlos_edad)

print("****************************************************************************************************************")

#especiales: in, not in, is, not is (devuelven true o false)

#ejemplo comprobacion lista

lista_invitados = ['Marcos', 'Angelica', 'Matias', 'Jose', 'Gaston', 'Nahuel', 'Ricardo', 'Roberto', 'Mariano', 'Mauricio',
'Leonel', 'Leonardo', 'Aldo', 'Raquel', 'Hernan', 'Sofia', 'Juan', 'Antonio', 'Marcelo', 'Juan cruz', 'Pedro', 'Pepe', 'Luisina',
'Celeste', 'Zulma', 'Irma', 'Diana', 'Daiana', 'Wally', 'Ruben', 'Rosendo', 'Joaquin']

x = 'Alberto'

if x in lista_invitados:
    print (x + " " + "si está en la lista, puede pasar")
else:
    print(x + " " + "no está en la lista, no puede pasar")


#HACER EJERCICIO DE OPERADORES (M1-12)




print("****************************************************************************************************************")

#Funciones predefinidas en Python (M1-13)

print("****************************************************************************************************************")

print("****************************************************************************************************************")