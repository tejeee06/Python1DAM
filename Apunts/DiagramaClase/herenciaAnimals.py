class Animal:

    def __init__(self, nom):
        self.nom = nom
    
    def parla(self):
        print(f"{self.nom} esta parlant")

class Gos(Animal):

    def parla(self):
        print(f"{self.nom} esta lladrant")

class Gat(Animal):

    def parla(self):
        print(f"{self.nom} esta fent miau" )
    
gos1 = Gos("Rex")
gos1.parla()
gat1 = Gat("Mishu")
gat1.parla()