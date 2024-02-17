#Exception in python > Error handling (Try / Except / Finally)
#Link: https://pythones.net/manejo-de-errores-y-excepciones-en-python-try-except-finally/

print("****************************************************************************************************************")

#try/except block

print("****************************************************************************************************************")
"""
def sumar(a, b):
    x = a + b
    print("Resultado = ",x)

def restar(a, b):
    x = a - b
    print("Resultado = ",x)

def multiplicar(a, b):
    x = a * b
    print("Resultado = ",x)

def dividir(a, b):
    x = a / b
    print("Resultado = ",x)

while True:
    try:
        a = int(input("Introduzca el primer operando: \n"))
        b = int(input("Introduzca el segundo operando: \n"))
        print("¿Que operacion desea realizar entre ", a , " y ", b ,"?")
        operacion=str(input(""""""
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n""""""))

    except:
        print("ERROR")
        operacion='?'
    
    if operacion == '1':#Si el usuario elige opción 1 llamamos a sumar
        sumar(a,b)
        break
    elif operacion == '2':#Si el usuario elige opción 1 llamamos a restar
        restar(a,b)
        break
    elif operacion == '3':#Si el usuario elige opción 1 llamamos a multiplicar
        multiplicar(a,b)
        break
    elif operacion == '4':#Si el usuario elige opción 1 llamamos a dividir
        dividir(a,b)
        break
    else:
        print ("Has ingresado un numero de opcion erroneo")"""

print("****************************************************************************************************************")

#ZeroDivisionError and Finally

print("****************************************************************************************************************")

def sumar(a, b):
    x = a + b
    print("Resultado = ",x)

def restar(a, b):
    x = a - b
    print("Resultado = ",x)

def multiplicar(a, b):
    x = a * b
    print("Resultado = ",x)

def dividir(a, b):
    x = a / b
    print("Resultado = ",x)

while True:
    try:
        a = int(input("Introduzca el primer operando: \n"))
        b = int(input("Introduzca el segundo operando: \n"))
        print("¿Que operacion desea realizar entre ", a , " y ", b ,"?")
        operacion=str(input("""
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
    
        if operacion == '1':#Si el usuario elige opción 1 llamamos a sumar
            sumar(a,b)
            break
        elif operacion == '2':#Si el usuario elige opción 1 llamamos a restar
            restar(a,b)
            break
        elif operacion == '3':#Si el usuario elige opción 1 llamamos a multiplicar
            multiplicar(a,b)
            break
        elif operacion == '4':#Si el usuario elige opción 1 llamamos a dividir
            dividir(a,b)
            break
        else:
            print ("Has ingresado un numero de opcion erroneo")

    
#ZeroDivisionError
 
    except ZeroDivisionError:
        print ("This program can´t divide by 0, try another calculation. // Este programa no puede dividir entre 0, pruebe otro calculo")
    
    except ValueError:
        print ("El valor introducido no es correcto")

    except Exception as e:
        tipo_error = type(e).__name__
        print("OTRO TIPO DE ERROR", tipo_error)    
        operacion='?'

#Finally

    finally:
        print ("Gracias por usar este programa")