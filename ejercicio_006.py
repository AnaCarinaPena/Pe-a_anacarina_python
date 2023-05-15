#Deberás escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

import math
def circle_area(pi, radio,altura):

#Formula
    resultado =   pi * (radio ** 2 ) * altura
    return resultado
#Operacion
r = float(input ("¿Cual es el radio?: "))
p = 3.1415
h = float(input ("¿Cual es el altura?: "))
calcula = circle_area(p, r, h)

# Imprime Total
print (calcula)