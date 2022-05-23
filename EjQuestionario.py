'''
Salut: 
L’usuari haurà de respondre tres preguntes:
- Fumes diàriament?     –Beus begudes no naturals?      -Ets sedentari/a?
Si tots les respostes són negatives, li apareixerà un missatge que dirà “La salut et
somriu, pero la vida no”. Si només respon afirmativament a una de les preguntes, el
missatge serà “No et queixis tant, que tens corda per estona”. Si dues de les respostes
són afirmatives, apareixerà “Vius al límit, no juguis amb la salut”. Si totes són
afirmatives, directament “No pintis de negre el teu futur, no val la pena”


Diners: 
L’usuari introduirà un nombre obligatòriament entre 1.0 i 10.0 i aleatòriament es
generarà un nombre de 3 xifres. El programa mostrarà un missatge indicant que
aviat li oferiran una oferta laboral amb un salari mensual resultat del producte dels
dos nombres anteriors.

Amor: 
Necessites conèixer el dia, el mes i l’any en què va nèixer l’usuari (en aquest cas
suposarem que l’usuari no introduirà valors invàlids) i si es considera romàntic o no.
Si la suma de les xifres de l’any és superior a la resta del dia i el mes i és considera
romàntic/a, tindrà molta fortuna en l’amor. D’altra forma, dis-li que no perdi l’esperança,
que la vida el pot sorprendre.
'''

menu = """
Sobre que quieres saber?

1- Salud
2- Dineros
3- Amor
4- Sortir


"""



final = False
opcion = 0;


#               FUNCIONES
def salud():
    respuesta = "";
    contador = 0;
    
    print("Estamos dentro de salud")
    respuesta = input("Fumas diariamente?")
    if respuesta == "si":
        contador += 1;
        
    respuesta = input("Bebes gaseosas?")
    if respuesta == "si":
        contador += 1;
        
    respuesta = input("Eres sedentario?")
    if respuesta == "si":
        contador += 1;

        #if respuesta == "si":
         

def dineros():   
    print("Has entrado en Dineros")         
            
def amor():
    print("Has entrado en amor")

    
    
#               MAIN    
while final == False:
    opcion = int(input(menu));
    
    if   opcion == 1:salud(); 
    elif opcion == 2:dineros();
    elif opcion == 3:amor();
    elif opcion == 4:opcion = True ;
   

