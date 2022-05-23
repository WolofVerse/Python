try:#Para que el try se ejecute, tenemos que poner las variables que el usuario nos devuelve dentro del try, no fuera.
    calificacion=float(input("Dime tu calificacion: "))



    if calificacion <0.6: 
        print("Insuficiente")
    elif calificacion >=0.6 and calificacion <=0.7:
        print("Suficiente")
    elif calificacion >=0.7 and calificacion <0.8:
        print("Bien")
    elif calificacion >=0.8 and calificacion <0.9:
        print("Notable")
    elif calificacion >=0.9 and calificacion <=1.0:
        print("Sobresaliente")
    else:
        print("Pon una calificacion entre 0.0 y 1.0")
        
        
except:
    print("Error.Pon un numero")