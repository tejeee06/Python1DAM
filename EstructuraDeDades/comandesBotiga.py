# Creem la classe botiga per gestionar les comandes dels clients
class Botiga:

    # Metode constructor
    def __init__(self):
        self.comandes = {}
    
    # Metode per calcular el cost total de les comandes de cada client
    def costTotalComanda(self, client):
 
        total = 0.0

        for comanda in self.comandes[client]:

            quantitat = comanda[1]
            preuUnitari = comanda[2]

            if quantitat > 1:

                total += quantitat * preuUnitari
            else:
                
                total += preuUnitari
            
        return total # Retorna el cost total de la comanda de cada client
    
    # Metode per obtenir els clients que han fet una comanda de mes de 100€
    def comanda100(self):
 
        clients = []

        for client in self.comandes:

            total = self.costTotalComanda(client)
            
            if total > 100:

                clients.append(client)
        
        return clients # Retorna una llista amb tots els clients que tenen una comanda de mes de 100€
    
    # Metode per imprimir totes les comandes de un client especific
    def comandesClientEspecific(self, client):

        if client in self.comandes:

            print(f"Comanda/es de {client}")

            for comanda in self.comandes[client]:

                print(f"Producte: {comanda[0]}, Quantitat: {comanda[1]}, Preu {comanda[2]}€")
        else:
            print(f"Client {client}, no es troba als registres")

# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    # Iniciem una nova instancia de la classe Botiga
    botiga = Botiga()

    #Definim les comandes dels clients en un diccionari
    botiga.comandes = {

        "Alex": [("Manga", 2, 7,5), ("Logitech Driving Force", 1, 234.3) ],
        "Eric": [("EAFC25", 1, 60.0)],
        "Valeria": [("Protector pantalla", 1, 19.5), ("Clauer", 2, 5.6)],
        "Nerea": [("Iphone 16 pro max", 1, 1458.6)]

    }

    print("Benvolgut al programa de comandes de la botiga")
    print()

    # Menu prinicpal del programa
    while(True):

        print("Que vol fer ?")
        print()
        print("Si vol veure el cost total de comandes de cada client premi la tecla 1")
        print()
        print("Si vol veure els noms dels clients amb comandes superiors a 100€ premi la tecla 2")
        print()
        print("Si vol veure les comandes d'un client especific premi la tecla 3")
        print()
        print("Si vol sortit premi la tecla 4")
        print()

        tecla = int(input("Selecciona una opcio "))

        if tecla == 1:
            # Si l'usuari introdueix la tecla 1 mostra el cost total de les comandes de cada client
            for client in botiga.comandes:
                total = botiga.costTotalComanda(client)
                print(f"El cost total de les comandes de {client} es de {total}€")
        elif tecla == 2:
            # Si l'usuari introdueix la tecla 2 mostra una llista amb tots els clients que tenen una comanda de mes de 100€ 
            clients = botiga.comanda100()
            print(f"Els clients que tenen una comanda de mes de 100€ son :{clients}")
        elif tecla == 3:
            # Si l'usuari introdueix la tecla 3
            client = input("Introdueix el nom del client : ")
            botiga.comandesClientEspecific(client)
        elif tecla == 4:
            # Si l'usuari introdueix la tecla 4
            print("Adeu , fins un altre")
            break

        print()