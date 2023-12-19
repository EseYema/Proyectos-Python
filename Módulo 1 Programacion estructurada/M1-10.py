#dictionaries ** diccionarios (M1-10)
#Link: https://pythones.net/diccionarios-en-python/


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