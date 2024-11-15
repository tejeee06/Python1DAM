
# Primer de tot generarem un numero aleatori.

import random
numeroAleatori = random.randint(1, 100)
# En el cas de que volguem saber el numero aleatori descomentar la linea d'abaix.
#print(f"El numero aleatori es {numeroAleatori}")

# Introduccio.
print("Començem el joc.")
print("Has d'endivinar un valor entre l'1 i el 100 , tens 10 intents per aconseguir-ho.")

# Li demanarem a l'usuari que introdueixi un numero.

print("Quin valor creus que es ? ")
numeroIntroduit=int(input()) #Ens asegurem que el tipus de dades que reculli l'input sigui un Int

# Abans d'entrar al bucle declararem les variables.

vides= 10 # Aixo son les vides que tindra l'usuari.
gunayadorExist= False # Aixo ens facilitara a que l'usuari pugi sortir del bucle quan encerti el numero.

"""
 Cremm el bucle , mentre que la variable vides sigui mes gran que 0 i la variable gunayadorExist sigui
 False fara el seguent:  
"""

while vides > 0 and gunayadorExist == False:

    """
    Primer evaluarem aquesta condicio , en el cas de que l'usuari hagi encertat el numero , el valor de
    la variable gunayadorExist caviara a True llavorens l'usuari sortira del bucle.
    """

    if numeroIntroduit == numeroAleatori:
        gunayadorExist= True    
    else:
        # Si no s'ha complit la condicio anterior lo primer que farem sera restar una vida a l'usuari i li direm que ha fallat.
        vides = vides - 1
        print("Has fallat , aquest no es el valor que estas buscant.")

        """
        El segon pas que farem es avisar a l'usuari si el numero que ha introduit es mes gran que
        el numero a endivinar o si per el contrari el numero que ha introduit es mes petit.
        """

        if numeroIntroduit > numeroAleatori:
            print("El numero que has introduit es mes gran que el numero que estas buscant.")
        else:
            print("El numero que has introduit es mes petit que el numero que estas buscant.")
        
        # A continuacio , comprobarem que l'usuari continua tenint vides i si te vides fara un  altre intent.

        if vides > 0:
            print("Torna a intentar-ho , quin valor creus que es ? ")
            numeroIntroduit=int(input())
        """
        Ara es tornara a repetir el bucle , en el cas de que l'usuari hagi encertat en aquest intent el guanyadorExist
        sera True i sortira del bucle sino es tornara a repetir tot el proces fins que l'usuari encerti el numero o 
        es quedi sense vides.
        """
    
"""
Un cop hem sortit del bucle , si la variable de l'usuari es guanyadorExist = True es a dir que ha encertat el numero
li comunicarem que ha encertat , en el cas contrari li comunicarem que ha perdut.
"""
if gunayadorExist:
    print("Felicitats , has encertat el numero.")
else:
    print(f"Has perdut , el numero que estabes buscant es {numeroAleatori}")

