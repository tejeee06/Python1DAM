class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def parlar(self ):
        print(f"{self.nom} esta parlant.")
    
    def DiguesEdat(self):
        print(f"Tinc {self.edat} anys.")
    

persona_pepe = Persona(nom= 'Pepe', edat= '18')

persona_pepe.parlar()
persona_pepe.DiguesEdat()

class Estudiant(Persona):
    def __init__(self, nom, edat, estudi):
        super().__init__(nom, edat)
        self.estudi = estudi

    def estudiar(self):
        print(f"{self.nom} està estudiant {self.estudi}.")

estudiant_pepe = Estudiant(nom='Pepe', edat='18', estudi= 'ADE')
estudiant_pepe.estudiar()
estudiant_pepe.parlar()

class Professor(Persona):
    def __init__(self, nom, edat, sou):
        super().__init__(nom, edat)
        self.sou = sou

    def cobrar(self ):
        print(f"El professor {self.nom} cobra {self.sou}")

professor_ignasi = Professor(nom='Igansi', edat='19', sou='4000 €')
professor_ignasi.cobrar()