'''Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que 
la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el 
programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>” '''

from math import sqrt
a = int(input('Ingrese Valor "a": '))
b = int(input('Ingrese Valor "b": '))
c = int(input('Ingrese Valor "c": '))
x = 0
x1 = 0

if((b**2)-(4*a*c))< 0:
    print("No se puede realizar por que no se puede sacar raiz a un numero")
else:
    x = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x1 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
print("La solucion es: \nx=",x, "\nx1=", x1)



