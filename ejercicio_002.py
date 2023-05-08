# Deberás escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input("¿Cual es tu nombre? ")
sexo = input("¿Cual es tu sexo M o H? ")
nombre = nombre.lower

if sexo == "M":
    if nombre() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Tu grupo es " + grupo)