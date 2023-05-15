# Deberás escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese 
# número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello

frutas = {"Platano":1.35, 
          "Manzana":0.80, 
          "Pera":0.85, 
          "Naranja":0.70}


usuario = input('¿Qué fruta quiere comprar? (Platano, Manzana, Pera, Naranja) ').title()
kilogramos = float(input('¿Cuantos kilogramos comprara? '))

if usuario in frutas:
    print ('El costo de', usuario, 'es de', frutas[usuario]*kilogramos, 'Pesos')

else:
    print("La fruta", usuario, "no se encuentra en existencia")
