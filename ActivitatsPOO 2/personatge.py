class Personatge:
    def __init__(self, name, hp, atac, defense):
        self.name = name
        self.hp = hp
        self.atac = atac
        self.defense = defense
    
    def isAlive(self):
        return self.hp > 0
    
    def rebreDany(self, dany):
        self.hp = max(self.hp - dany, 0)
    
    def atacar(self, enemic):
        dany = max(self.atac - enemic.defense, 1)
        enemic.rebreDany(dany)
        return dany

def main(p1, p2):
    print("Que comience la batalla !!!")
    torn = 0

    while p1.isAlive() and p2.isAlive():
        atacant = p1 if torn %2 == 0 else p2
        defensor = p2 if torn %2 == 0 else p1
        print(f"Turno {torn + 1}: ")
        print(f"{atacant.name} (Vida: {atacant.hp} puntos de salud) vs {defensor.name} (Vida: {defensor.hp} puntos de salud)")

        dany = atacant.atacar(defensor)
        print(f"{atacant.name} ataca a {defensor.name} y le hace {dany} puntos de daño.")
        torn +=1
        print()
    
    guanyador = p1 if p1.isAlive() else p2
    print(f"{guanyador.name} ha ganado la batalla con {guanyador.hp} puntos de vida restantes.")

p1 = Personatge("Mago Azul", 15, 10, 5)
p2 = Personatge("Guerrero Barbaro", 10, 5, 10)
main(p1, p2)
