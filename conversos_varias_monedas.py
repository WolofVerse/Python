menu = """
Bienvenido al conversor de moneda✔
Que quieres convertir?
1- Euros
2- Lei
3- Dolares

Elige una opción"""

opcion = input(menu)

if opcion == "1":
    dolares = float(input("Cuantos Euros tienes? "))

    valor_euro = float(1.05)
    valor_euro = str(valor_euro)
    print("El valor del dolar es " + valor_euro)
    valor_euro= float(valor_euro)

    euros = dolares / valor_euro
    euros = round(euros, 2)
    euros=str(euros)
    print("Tienes " + euros + "$")
    
    
elif opcion == "2":
    dolares = float(input("Cuantos lei tienes? "))

    valor_euro = float(52.43)
    valor_euro = str(valor_euro)
    print("El valor del lei es " + valor_euro)
    valor_euro= float(valor_euro)

    euros = dolares / valor_euro
    euros = round(euros, 2 )
    euros=str(euros)
    print("Tienes " + euros + "EUR ")
    
    
elif opcion == "3":
    #Dolar a Euro (BLOQUE DE CODIGO)
    dolares = float(input("Cuantos dolares tienes? "))

    valor_euro = float(0.95)
    valor_euro = str(valor_euro)
    print("El valor del euro es " + valor_euro)
    valor_euro= float(valor_euro)

    euros = dolares / valor_euro
    euros = round(euros, 2 )
    euros=str(euros)
    print("Tienes " + euros + "€")
    
    
else :
    print("Pon una opcion correcta")







