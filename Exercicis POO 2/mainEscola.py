class Persones:
    def __init__(self, nom, cognom, dni):
        self.nom = nom
        self.cognom = cognom
        self.dni = dni
    
    def presentar(self):
        print(f"El meu nom es : {self.nom} , el meu cognom es : {self.cognom} , i el meu dni es : {self.dni} " )

class Estudiant(Persones):
    def __init__(self, curs, nom, cognom, dni):
        super().__init__(self, nom, cognom, dni)
        self.curs = curs
    
    def presentar(self):
        super().presentar()
        print(f"Soc estudiant de {self.curs}")

class Professor(Persones):
    def __init__(self, assignatures, nom, cognom, dni):
        super().__init__(self, nom, cognom, dni)
        self.assignatures = assignatures
    
    def presentar(self):
       super().presentar()
       print(f"Soc professor de {self.assignatures}") 

class Escola():
    def __init__(self):
        self.llistaProfes = []
        self.llistaEstudiants = []
    
    def afegirEstudiants(self, estudiant):
        self.llistaEstudiants.append(estudiant)
    
    def afegirProfessor(self, professor):
        self.llistaProfes.append(professor)