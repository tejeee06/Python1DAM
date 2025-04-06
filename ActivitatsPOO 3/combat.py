import random

class Personage:
    def __init__(self, nom, vida, atac):
        self.nom = nom
        self.vida = vida
        self.atac = atac
    
    def isAlive(self):
        return self.vida > 0
    
    def atacar(self, enemic):
        dany = self.atac + random.randint(1, 7)
        enemic.vida -= dany
        print(f"{self.nom} realiza un ataque a {enemic.nom} y le hace {dany} puntos de daño")
        
        if not enemic.isAlive():
            print(f"{self.nom} ha derrotado a {enemic.nom}")
    
    def accioTorn(self, enemic):
        self.atacar(enemic)

class SistemaCombat:
    def __init__(self, atacant, defensor):
        self.atacant = atacant
        self.defensor = defensor
    
    def iniciarCombat(self):
        print("Comienza el combate")
        torn = 1

        while self.atacant.isAlive() and self.defensor.isAlive():
            print(f"Torn {torn}")
            self.atacant.accioTorn(self.defensor)
            if not self.defensor.isAlive():
                break

            self.defensor.accioTorn(self.atacant)
            if not self.atacant.isAlive():
                break

            torn +=1

p1 = Personage("Antonio", 50, 10)
p2 = Personage("Ignasi", 55, 8)
combat = SistemaCombat(p1, p2)
combat.iniciarCombat()