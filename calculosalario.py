try:
    horas = int(input("Introduce las horas trabajadas"))
    tarifa = float(input("Introduce la tarifa por hora"))

    if horas > 40 :
        salario= 40*tarifa
        tarifaExtra = tarifa * 1.5#para multiplicar las horas extras con la tarifa normal
        horasExtra=(horas-40)*tarifaExtra#rebajamos las 40 horas pagadas normales y sumamos solo las extra.
        salarioFinal=salario+horasExtra
        print(f"Tu salario es {salarioFinal}")
    
    else:
        salario=horas*tarifa
        print(f"Tu salario es {salario} ")

except:
    print("Pon un numero")
