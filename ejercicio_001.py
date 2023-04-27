#Declaracion Pregunta 1
pregunta_1 = input ("¿Cuál es tu nombre?")
pregunta_1_upper = pregunta_1.upper()
pregunta_1_lower = pregunta_1.lower()
#Declaracion Vocales Nombre
contador=0
for i in pregunta_1_lower:
    if i in "aeiou":
        contador=contador+1
#Declaracion Letra Nombre
contador_letras=0
for i in pregunta_1_lower:
    if i in "bcdfghjklmnñpqrstvwxyz":
        contador_letras=contador_letras+1

#Declaracion Pregunta 2
pregunta_2 = input ("¿Cuál es tu primer apellido?")
pregunta_2_upper = pregunta_2.upper()
pregunta_2_lower = pregunta_2.lower()
#Impresión Vocales primer apellido
contador_1=0
for i in pregunta_2_lower:
    if i in "aeiou":
        contador_1=contador_1+1
#Declaracion Letra Primer Apellido
contador_letras_1=0
for i in pregunta_2_lower:
    if i in "bcdfghjklmnñpqrstvwxyz":
        contador_letras_1=contador_letras_1+1

pregunta_3 = input ("¿Cuál es tu segundo apellido?")
pregunta_3_upper = pregunta_3.upper()
pregunta_3_lower = pregunta_3.lower()
#Declaracion Vocales Segundo Apellido
contador_2=0
for i in pregunta_3_lower:
    if i in "aeiou":
        contador_2=contador_2+1
#Declaracion Letra Segundo Apellido
contador_letras_2=0
for i in pregunta_3_lower:
    if i in "bcdfghjklmnñpqrstvwxyz":
        contador_letras_2=contador_letras_2+1

# Pregunta 4 ¿En qué año naciste?
Año= int(input("¿En que año naciste? "))

# Pregunta 5 ¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)
Dia_mes = input("¿En que mes y dia naciste? Usa formato mm-dd: ")
a,b,c,d,e = Dia_mes

# Inciso A
#Impresion de Nombre Mayusculas
print("Este es tu nombre completo en mayúsculas: ")
print(pregunta_1_upper, pregunta_2_upper, pregunta_3_upper)

# Inciso B
#Impresion de Nombre Minusculas
print("Este es tu nombre completo en minúsculas: ")
print(pregunta_1_lower, pregunta_2_lower, pregunta_3_lower)

# Inciso C
#Impresión de Esta es tu fecha de nacimiento "dd-mm-aaaa"
print(f"Esta es tu fecha de nacimiento: {d}{e}-{a}{b}-{Año}")

# Inciso D
#Impresión de Esta es tu edad
import datetime
edad = datetime.datetime.now().year - Año
año_actual = 2023
print ("Esta es tu edad", edad, "años" )

# Inciso E
#Nombre completo tiene __ vocales
print("Tu nombre completo tiene ", contador + contador_1 + contador_2, "vocales")

# Inciso F
#Nombre completo tiene __ letras
print("Tu nombre completo tiene ", contador_letras + contador_letras_1 + contador_letras_2,  "letras")

# Inciso G
#Impresión de ¿Tu edad es un carácter de tipo número? ___True____
entero= edad
print("¿Tu edad es un carácter de tipo número?: ", isinstance(entero, int))
print(type(entero))

# Inciso H
#Impresión de ¿Tu nombre completo es un carácter de tipo alfanumérico? ___True____
alfanumerico = (pregunta_1, pregunta_2, pregunta_3)
print("¿Tu nombre completo es un carácter de tipo alfanumérico?: ", isinstance(alfanumerico, str))

# Inciso I
#Impresión de Tu edad en 10 años será ___________
edad_10_años = edad + 10
print ("Tu edad en 10 años será", edad_10_años) 

# Inciso J
#Impresión de La media de tu edad actual y tu edad en 20 años es_____
resultado = ( edad /2 + 20)
print(" La media de tu edad actual y tu edad en 20 años es" ,resultado )