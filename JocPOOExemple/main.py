import random

class Personatge:
    def __init__(self, nom, vida, atac, defensa):
        self.nom = nom
        self.vida = vida
        self.atac = atac
        self.defensa = defensa
        self.experiencia = 0
    
    def estaViu(self):
        return self.vida > 0

    def rebreDany(self, dany):
        self.vida -= max(0, dany - self.defensa)
        if self.vida < 0:
            self.vida = 0
    
    def atacar(self, altrePersonatge):
        dany = random.randint(0, self.atac)
        print(f"{self.nom} ataca a {altrePersonatge} y fa {dany} de dany")
        altrePersonatge.rebreDany(dany)

    def mostrarEstadistiques(self):
        print(f"{self.nom} te vida {self.vida} , te de defensa {self.defensa} i te d' atac {self.atac}")

class Joc(Personatge):
    def __init__(self, personatge1, personatge2):
        self.personatge1 = personatge1
        self.presonatge2 = personatge2
    
    def combat(self):
        while self.personatge1.estaViu() and self.presonatge2.estaViu():
            print("Personatge 1 ataca a Personatge 2")
            self.personatge1.atacar(self.presonatge2)
            self.versus()
            print("Personatge 2 ataca a Personatge 1")
            self.presonatge2.atacar(self.personatge1)
            self.versus()
        if self.personatge1.estaViu():
            print("El personatge 1 ha gunayat")
        else:
            print("Personatge 2 ha guanyat")        

    def vs(self):
        print(f"{self.personatge1.nom} te {self.vida} punts de vida , {self.presonatge2.nom} te {self.vida} punts de vida")

p1 = Personatge("p1", 100, 100, 2)
p2 = Personatge("p2", 100, 12, 3)

joc1 = Joc(p1, p2)
joc1.combat()