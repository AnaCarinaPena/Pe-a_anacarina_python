#Deberás escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
Pass = input("Ingrese nueva contraseña: ")

cont = 1
nombre = input("Ingresar contraseña: ")
while Pass:
    if  nombre == Pass: 
        print ("ACCESO CONCEDIDO")
        break
    else:
        print ("Contraseña incorrecta")
    nombre = input ("Digite nuevamente la contraseña: ")
  