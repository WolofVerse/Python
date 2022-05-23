euros = int(input("Cuantos euros tienes? "))
#podemos hacer sin el float primero y despues poner
# euros = float(euros)
valor_dolar = str(1.83)
print("El valor del dolar es : "+ valor_dolar)
valor_dolar = float(valor_dolar)
dolares = euros / valor_dolar
#rebajamos las decimales a 2
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes " + dolares + "dolares $")






