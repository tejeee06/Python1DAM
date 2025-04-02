class Personage:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def greetings(self):
        print(f"Saludos {self.name} nivel {self.level}")
    

p1 = Personage("Alex el guerrero", 18)
p2 = Personage("Avril la sanadora", 20)

p1.greetings()
p2.greetings()