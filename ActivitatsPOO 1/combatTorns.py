import random

class Personaje:
    def __init__(self, nom, vida, atac):
        self.nom = nom
        self.vida = vida
        self.atac = atac
    
    def isAlive(self):
        return self.vida > 0
    
    def atacar(self, enemic):
        dany = self.atac + random.randint(5, 15)
        enemic.vida -= dany
        print(f"{self.nom} ataca a {enemic.nom} y le hace {dany} puntos de daño")
        if not enemic.isAlive():
            print(f"{self.nom} ha derrotado a {enemic.nom}")
    
    def accio_torn(self, enemic):
        self.atacar(enemic)

class Guerrer(Personaje):
    def __init__(self, nom):
        super().__init__(nom, vida=120, atac=15)
    
    def habilidad_especial(self, enemic):
        print(f"{self.nom} utiliza golpe con espada")
        dany = int(self.atac * 1.5) + random.randint(0, 5)
        enemic.vida -= dany
        print(f"Causa {dany} puntos de daño")

class Mago(Personaje):
    def __init__(self, nom):
        super().__init__(nom, vida=80, atac=12)
        self.mana = 100
    
    def habilidad_especial(self, enemic):
        if self.mana >= 20:
            print(f"{self.nom} lanza una bola de fuego")
            dany = self.atac + random.randint(5, 10)
            enemic.vida -= dany
            self.mana -= 20
            print(f"Causa {dany} puntos de daño")
        else:
            print("¡No tienes suficiente mana! Usando ataque normal.")
            self.atacar(enemic)

class Arquer(Personaje):
    def __init__(self, nom):
        super().__init__(nom, vida=100, atac=13)
    
    def habilidad_especial(self, enemic):
        print(f"{self.nom} realiza un disparo rápido")
        self.atacar(enemic)
        if random.random() < 0.5:
            self.atacar(enemic)

class SistemaCombat:
    def __init__(self, jugador, enemic):
        self.jugador = jugador
        self.enemic = enemic
    
    def iniciarCombat(self):
        print("¡Comienza el combate!")
        torn = 1

        while self.jugador.isAlive() and self.enemic.isAlive():
            print(f"\n--- Turno {torn} ---")
            print(f"Jugador: {self.jugador.vida} HP")
            print(f"Enemigo: {self.enemic.vida} HP")

            self.torn_jugador()
            if not self.enemic.isAlive():
                break

            self.torn_enemic()
            torn += 1
        
        if self.jugador.isAlive():
            print("\n¡Has ganado el combate!")
        else:
            print("\n¡El enemigo te ha derrotado!")

    def torn_jugador(self):
        print("\nTu turno:")
        print("1. Ataque normal")
        print("2. Habilidad especial")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            self.jugador.atacar(self.enemic)
        elif opcion == "2":
            self.jugador.habilidad_especial(self.enemic)
        else:
            print("Opción inválida. Pierdes tu turno.")

    def torn_enemic(self):
        print("\nTurno del enemigo:")
        self.enemic.accio_torn(self.jugador)

if __name__ == "__main__":
    jugador = Mago("Mago Azul")
    enemic = Guerrer("Guerrero Espartano")

    combat = SistemaCombat(jugador, enemic)
    combat.iniciarCombat()