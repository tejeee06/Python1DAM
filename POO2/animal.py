class Animal:
    def __init__(self, name):
        self.name = name
    
    def defaultSound(self):
        print(f"El animal {self.name} hace un sonido generico.")

class Gos(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def defaultSound(self):
        print(f"El perro {self.name} hace Guau.")

class Gat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def defaultSound(self):
        print(f"El gato {self.name} hace Miau.")

def soAnimal(animal):
    animal.defaultSound()

a1 = Animal("Pepito")
go1 = Gos("Rex")
ga1 = Gat("Mishu")

soAnimal(a1)
soAnimal(go1)
soAnimal(ga1)
