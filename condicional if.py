print("Evaluacion alumnos")

nota_alumno=input()

def evaluacion(nota):#evaluacion es una funcion
    valoracion="aprobado"#esto es una variable
    
    if nota<5:#if es una condicion
        valoracion="suspenso"
    return valoracion


print(evaluacion(int(nota_alumno)))