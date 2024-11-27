# Apend per afegir coses a les funcions

class Llibre:
    def __init__(self, titol, autor, any_publicacio):
        self.titol = titol
        self.autor = autor
        self.any_publicacio = any_publicacio

    def mostrar_informacio(self):
        return f"Títol: {self.titol}, Autor: {self.autor}, Any de publicació: {self.any_publicacio}"


# Subclasses
class LlibreFiccio(Llibre):
    def __init__(self, titol, autor, any_publicacio, genere):
        super().__init__(titol, autor, any_publicacio)
        self.genere = genere

    def mostrar_informacio(self):
        base_info = super().mostrar_informacio()
        return f"{base_info}, Gènere: {self.genere}"


class LlibreNoFiccio(Llibre):
    def __init__(self, titol, autor, any_publicacio, area_coneixement):
        super().__init__(titol, autor, any_publicacio)
        self.area_coneixement = area_coneixement

    def mostrar_informacio(self):
        base_info = super().mostrar_informacio()
        return f"{base_info}, Àrea de coneixement: {self.area_coneixement}"


# Classe Soci
class Soci:
    def __init__(self, nom, dni):
        self.nom = nom
        self.dni = dni
        self.lloguers = []

    def afegir_lloguer(self, llibre):
        self.lloguers.append(llibre)

    def mostrar_lloguers(self):
        resultat = ""
        for llibre in self.lloguers:
            resultat += llibre.mostrar_informacio() + "\n"
        return resultat.strip()


    def __str__(self):
        return f"Soci: {self.nom}, DNI: {self.dni}"


# Classe Biblioteca
class Biblioteca:
    def __init__(self, nom):
        self.nom = nom
        self.llista_llibres = []
        self.socis = []

    def afegir_llibre(self, llibre):
        self.llista_llibres.append(llibre)

    def afegir_soci(self, soci):
        self.socis.append(soci)

    def mostrar_llibres(self):
        resultat = ""
        for llibre in self.llista_llibres:
            resultat += llibre.mostrar_informacio() + "\n"
        return resultat.strip()


    def __str__(self):
        return f"Biblioteca: {self.nom}"


# Programa principal
if __name__ == "__main__":
    # Creació de llibres
    llibre1 = LlibreFiccio("El senyor dels anells", "J.R.R. Tolkien", 1954, "Fantasia")
    llibre2 = LlibreNoFiccio("Sapiens", "Yuval Noah Harari", 2011, "Història")

    # Creació de la biblioteca
    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.afegir_llibre(llibre1)
    biblioteca.afegir_llibre(llibre2)

    # Creació de socis
    soci1 = Soci("Maria", "12345678A")
    soci2 = Soci("Joan", "87654321B")
    biblioteca.afegir_soci(soci1)
    biblioteca.afegir_soci(soci2)

    # Assignació de lloguers
    soci1.afegir_lloguer(llibre1)
    soci2.afegir_lloguer(llibre2)

    # Mostra informació     print("Informació de la biblioteca:")
    print(biblioteca)
    print("\nLlibres disponibles:")
    print(biblioteca.mostrar_llibres())

    print("\nInformació dels socis i lloguers:")
    for soci in biblioteca.socis:
        print(f"\n{soci}")
        print("Llibres llogats:")
        print(soci.mostrar_lloguers())
