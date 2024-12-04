# Creem la classe Projecte
class Projecte:

    # Metode Constructor
    def __init__(self, nom, durada, llenguatgePrincipal):
        self.nom = nom
        self.durada = durada
        self.llenguatgePrincipal = llenguatgePrincipal

    # Metode per mostrar la informació de la classe projecte
    def mostrar_informacio(self):
        return f"Projecte: {self.nom}, Duració: {self.durada} mesos, Llenguatge: {self.llenguatgePrincipal}"

# Creem la classe ProjecteIntern , classe filla de la classe Projecte
class ProjecteIntern(Projecte):

    # Metode Constructor
    def __init__(self, nom, durada, llenguatgePrincipal, responsables, departament):
        # Heredem els atributs de la classe pare
        super().__init__(nom, durada, llenguatgePrincipal)
        # Declarem la resta d'atributs
        self.responsables = responsables
        self.departament = departament
        self.tasques = [] # Creem un Array (list a Python) per poder afegir diferentes tasques

    # Metode per afegir dades a l'Array utilitzant .append
    def afegir_tasca(self, tasca):
        self.tasques.append(tasca)
    
    # Metode per mostrar les dades de l' Array
    def mostrar_tasques(self):
        tasques_info = [
            f"Tasca: {tasca.nom}, Estat: {tasca.estat}, Responsable: {tasca.responsable.nom}"
            for tasca in self.tasques
        ]
        return "\n".join(tasques_info)

    # Metode per mostrar la informació de la classe ProjecteIntern
    def mostrar_informacio(self):
        base_info = super().mostrar_informacio()
        return f"{base_info}, Responsable: {self.responsables}, Departament: {self.departament}"

# Definim la classe ProjecteExtern , clasese filla de la classe Projecte
class ProjecteExtern(Projecte):

    # Metode Constructor
    def __init__(self, nom, durada, llenguatgePrincipal, client, pressupost):
        # Heredem els atributs de la classe pare
        super().__init__(nom, durada, llenguatgePrincipal)
        # Declarem la resta d'atributs de la classe
        self.client = client
        self.pressupost = pressupost

    # Mostrem la informació de la classe ProjecteExtern
    def mostrar_informacio(self):
        base_info = super().mostrar_informacio()
        return f"{base_info}, Client: {self.client}, Pressupost: {self.pressupost}K€"

# Definim la classe Equip
class Equip:

    # Metode Constructor
    def __init__(self, nom):
        self.nom = nom
        self.membres = [] # Creem un Array per poder afegir diferents membres
    
    # Metode per afegir membres al Array utilitzant .append
    def afegir_membre(self, membre):
        self.membres.append(membre)

    # Metode per mostrar les dades del Array
    def mostrar_membres(self):
        membres_info = [
            f"Membre: {membre.nom}, Rol: {membre.rol}, Experiència: {membre.experiencia} anys"
            for membre in self.membres
        ]
        return "\n".join(membres_info)

    # Metode per mostrar la informació de la classe equip
    def mostrar_informacio(self):
        return f"Equip: {self.nom}, Membres: {len(self.membres)}"

# Definim la classe Membre
class Membre:

    # Metode Constructor
    def __init__(self, nom, rol, experiencia):
        self.nom = nom
        self.rol = rol
        self.experiencia = experiencia

    # Mostrem la informació de la classe Membre
    def mostrar_informacio(self):
        return f"Nom: {self.nom}, Rol: {self.rol}, Anys d'experiència: {self.experiencia}"

# Definim la classe Tasca
class Tasca:

    # Metode Constructor
    def __init__(self, nom, estat, responsable):
        self.nom = nom
        self.estat = estat
        self.responsable = responsable

    # Metode per mostrar la informació de la classe Tasca
    def mostrar_informacio(self):
        return f"Nom de la tasca: {self.nom}, Estat de la tasca: {self.estat}, Responsable: {self.responsable.nom}"


if __name__ == "__main__":
    
    # Crear un projecte intern
    projecte_intern = ProjecteIntern(
        nom="Aplicació CRM Interna",
        durada=12,
        llenguatgePrincipal="Python",
        responsables="Joan Rovira",
        departament="IT"
    )

    # Crear un projecte extern
    projecte_extern = ProjecteExtern(
        nom="Plataforma E-learning",
        durada=18,
        llenguatgePrincipal="Java",
        client="Educorp",
        pressupost=300
    )

    # Crear un equip i membres
    equip = Equip("Equip Desenvolupament")
    membre1 = Membre("Anna", "Desenvolupadora", 3)
    membre2 = Membre("Marc", "Tester", 2)
    equip.afegir_membre(membre1)
    equip.afegir_membre(membre2)

    # Afegir tasques al projecte intern
    tasca1 = Tasca("Definir requeriments", "pendent", membre1)
    tasca2 = Tasca("Provar funcionalitats", "pendent", membre2)
    projecte_intern.afegir_tasca(tasca1)
    projecte_intern.afegir_tasca(tasca2)

    # Mostrar informació del projecte intern
    print("Informació del projecte intern:")
    print(projecte_intern.mostrar_informacio())
    print("\nTasques del projecte intern:")
    print(projecte_intern.mostrar_tasques())

    # Mostrar informació de l'equip
    print("\nInformació de l'equip:")
    print(equip.mostrar_informacio())
    print("\nMembres de l'equip:")
    print(equip.mostrar_membres())

    # Mostrar informació del projecte extern
    print("\nInformació del projecte extern:")
    print(projecte_extern.mostrar_informacio())