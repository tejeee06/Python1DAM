# Classe Persona
class Persona :
    # Metodo constructor de la classe Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Metodos de la classe Persona
    def hablar(self):
        print(f"{self.nombre} esta hablando")
    
    def caminar(self):
        print(f"{self.nombre} esta caminando")

# Classe Estudiante Heredada de la classe Persona
class Estudiante(Persona):
    # Metodo constructor de la classe Estudiante
    def __init__(self,nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
    
    # Metodo de la classe Estudiante
    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

p1 = Persona("Alex", 18)
e1 = Estudiante("Carlos", 21, "0284932049203")
p1.hablar()
p1.caminar()
e1.estudiar()
e1.hablar()
e1.caminar()