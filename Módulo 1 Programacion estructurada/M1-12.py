#basic operators: arithmetic, comparison, assignment, logical and special ** 
#operadores básico: aritmeticos, comparación, asignación, lógicos y especiales (M1-12)
#Link: https://pythones.net/operadores-basicos-en-python/

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

print("****************************************************************************************************************")

#HACER EJERCICIO DE OPERADORES (M1-12)

print("FALTA HACER EL EJERCICIO DEL FINAL 'LA FIESTA DE JORGE'")


print("****************************************************************************************************************")