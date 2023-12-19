#Conditional Statements in Python ** condicionales: if, else, elif (M1-11)
#Link: https://pythones.net/if-else-elif-condicionales/


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