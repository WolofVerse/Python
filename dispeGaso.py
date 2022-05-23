menu= """
Que combusible quieres poner?

1- Diesel
2- Gasolina

"""

opcion = input(menu)



if opcion == "1":
    cantidad = int(input("Cuantos litros quieres poner de Diesel?"))

    precioDiesel= str(float(1.90))
    print("El precio del Diesel es " + precioDiesel)
    precioDiesel= float(precioDiesel)
    totalEuro= cantidad * precioDiesel
    totalEuro=str(totalEuro)
    print("Tienes que pagar" + totalEuro)
    
elif opcion =="2":
    cantidad =int(input("Cuantos litros quieres poner de Gasolina?"))
    
    precioGasolina = str(float(1.65))
    print("El precio de la gasolina es " + precioGasolina)
    precioGasolina=float(precioGasolina)
    totalEuro= cantidad * precioGasolina
    totalEuro=str(totalEuro)
    print("Tienes que pagar " + totalEuro)
    
    
else:
    print("Elige una opcion correcta")
    
    