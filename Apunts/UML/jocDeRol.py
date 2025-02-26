import random

class Personatge:
    def __init__(self, nom, classe, nivell, hp, atac, items):
        self.nom = nom
        self.classe = classe
        self.nivell = nivell
        self.hp = hp
        self.atac = atac
        self.items = items
    
    def atacar(self, oponent):
        if self.esta_viu():
            dany = self.atac + random.randint(-2, 2)  # Variació aleatòria
            oponent.hp -= dany
            print(f"{self.nom} ataca {oponent.nom} i li fa {dany} de dany.")
            if oponent.hp <= 0:
                print(f"{oponent.nom} ha estat derrotat!")
        else:
            print(f"{self.nom} no pot atacar perquè està derrotat!")

    def afegir_item(self, item):
        self.items.append(item)
        print(f"{self.nom} ha obtingut un {item.nom}!")
 
    def usar_item(self, item):
        if item in self.items:
            item.usar(self)
            self.items.remove(item)
        else:
            print(f"{self.nom} no té aquest ítem.")

    def esta_viu(self):
        return self.hp > 0

    def __str__(self):
        return f"Nom: {self.nom} Classe: {self.classe} Punts de vida: {self.hp}"

class Guerrer(Personatge):
    def __init__(self, nom):
        super().__init__(nom, "Guerrer", nivell=1, hp=100, atac=10)
 
 
class Mag(Personatge):
    def __init__(self, nom):
        super().__init__(nom, "Mag", nivell=1, hp=70, atac=15)
 
 
class Arquer(Personatge):
    def __init__(self, nom):
        super().__init__(nom, "Arquer", nivell=1, hp=85, atac=12)
 


class Item:
    def __init__(self, nom):
        self.nom = nom
 
    def usar(self, personatge):
        pass  # Aquest mètode serà sobreescrit a les subclasses

class Pocio(Item):
    def __init__(self, cura):
        super().__init__("Poció de Vida")
        self.cura = cura
 
    def usar(self, personatge):
        personatge.hp += self.cura
        print(f"{personatge.nom} ha utilitzat una {self.nom} i ha recuperat {self.cura} HP!")
 
class Arma(Item):
    def __init__(self, dany):
        super().__init__("Arma poderosa")
        self.dany = dany
 
    def usar(self, personatge):
        personatge.atac += self.dany
        print(f"{personatge.nom} ha equipat una {self.nom} i ha augmentat el seu atac en {self.dany}!")
 
