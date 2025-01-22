class Biblioteca:
    
    def __init__(self, llibres):

        self.llibres = llibres
        
    
    def afegirLlibre(self, id, titol, autor, quantitat):

        llibres[id] = {"titol": titol, "autor": autor, "quantitat": quantitat}
        print("LLibre afegit correctament")
        print()
    
    def mostrarLlibre(self, id):
        
        if id in self.llibres:
            llibre = self.llibres[id]
            print(f"Titol : {llibre['titol']}")
            print(f"Autor : {llibre['autor']}")
            print(f"Quantitat : {llibre['quantitat']}")
            print()
        else :
            print(f"El llibre amb l' id {id} no existeix")
            print()

    def mostrarTotsLlibres(self):

        for id, llibre in self.llibres.items(): #.items per poder iterar sobre un diccionari
            print(f"ID : {id}")
            print(f"Titol : {llibre['titol']}")
            print(f"Autor : {llibre['autor']}")
            print(f"Quantitat : {llibre['quantitat']}")
            print()

    def prestecLlibre(self, id):

        if id in self.llibres:
            llibre = self.llibres[id]
            if llibre['quantitat'] > 0:
                llibre['quantitat'] -= 1
                print(f"El llibre {llibre['titol']} s' ha prestat correctament")
                print()
            else :
                print("No es pot realitzar el prestec perque els llibres estan esgotats")
                print()
        else :
            print(f"El llibre amb l' id {id} no existeix")
            print()



if __name__ == "__main__":

    llibres = {

        1: {"titol": "The C programming language", "autor": "Dennis Ritchie , Brian Kernighan", "quantitat": 4},
        2: {"titol": "Java for dummies", "autor": "Barry A.Burd", "quantitat": 2},
        3: {"titol": "Eloquent JavaScript", "autor": "Marijn Haverbeke", "quantitat": 6}

    }

    biblioteca = Biblioteca(llibres)
   
    print("Menu Interactiu de la Biblioteca")
    while True :

        print("Que vols fer ? ")
        print()
        print("Tecla 1 per afegir un nou llibre")
        print()
        print("Tecla 2 per buscar un llibre en concret")
        print()
        print("Tecla 3 per mostrat tots els llibres existents")
        print()
        print("Tecla 4 per relitzar el prestec d'un llibre")
        print()
        print("Tecla 5 per sortir del programa")
        print()
        tecla = int(input("Quina opcio vols escollir ? "))

        if tecla == 1:
            print("Has seleccionat afegir llibre")
            id = int(input("ID de llibre que vulgis introduir : "))
            titol = str(input("Titol del llibre que vulgis introduir : "))
            autor = str(input("Autor del llibre que vulgis introduir : "))
            quantitat = int(input("Quantitat de exemplars disponibles del nou llibre : "))
            biblioteca.afegirLlibre(id, titol, autor, quantitat)
        elif tecla == 2:
            print("Has seleccionat buscar un llibre")
            id = int(input("ID del llibre que vulgis cercar : "))
            biblioteca.mostrarLlibre(id)
        elif tecla == 3:
            print("Has seleccionat mostrar tots els llibres")
            biblioteca.mostrarTotsLlibres()
        elif tecla == 4:
            print("Has seleccionat realitzar un prestec")
            id = int(input("Introdueix l'id del llibre :  "))
            biblioteca.prestecLlibre(id)
        elif tecla == 5:
            print("Adeu , fins un altre")
            break
        else :
            print("Error , tecla no reconeguda")

