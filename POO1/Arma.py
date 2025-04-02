class Arma:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type
        self.active = False
        self.durability = 100
    
    def showInfo(self):
        print(f"{self.name} con {self.damage} puntos de daño , de tipo : {self.type} con una durabilidad de {self.durability} puntos.")

    def saveWeapon(self):
        if self.active == True:
            print("Guardando el arma..")
            self.active = False
        else :
            print("Error no se puede guardar el arma , ya esta guardada.")
    
    def useWeapon(self):
        if self.active == False:
            print("Sacando el arma...")
            self.active = True
        else :
            print("Error , ya estas utilizando el arma")

a1 = Arma("Cañon de fluzo", 120, "Laser")
a2 = Arma("Arco encantado", 95, "Magico")
#a1.showInfo()
#a1.useWeapon()
#a1.useWeapon()
#a1.saveWeapon()
#a1.saveWeapon()
a1.showInfo()
print()
a2.showInfo()