class Cotxe:

    def __init__(self, TipusMotor, Combustible, Portes):
        self.TipusMotor = TipusMotor
        self.Combustible = Combustible
        self.Portes = Portes
    
    def get_TipusMotor(self):
        print(f"El tipus de motor es: {self.TipusMotor}")
    
    def get_Combustible(self):
        print(f"El combustible es: {self.Combustible}")
    
    def get_Portes(self):
        print(f"Te {self.Portes} portes")
    
    def set_Portes(self, NumeroPortes):
        self.Portes=NumeroPortes


class Audi(Cotxe):

    def __init__(self, CV, Longitud, Amplitud):
        self.CV = CV
        self.Longitud = Longitud
        self.Amplitud = Amplitud
    
    def get_CV(self):
        print(f"El cotxe te {self.CV} caballs")
    
    def get_Longitud(self):
        print(f"La longitud del cotxe es: {self.Longitud}")
    
    def get_Amplitud(self):
        print(f"L'amplitud del cotxe es {self.Amplitud}")

class Mercedes(Cotxe):

    def __init__(self, TipusAcabat):
        self.TipusAcabat = TipusAcabat
    
    def get_TipusAcabat(self):
        print(f"El tipus d'acabat es: {self.TipusAcabat}")

cotxeAudi1=Audi(CV="200", Longitud="5", Amplitud="2")
cotxeAudi1.get_Amplitud()
cotxeMercedes1=Mercedes(TipusAcabat="Luxury")
cotxeMercedes1.get_TipusAcabat()
cotxeMercedes1.set_Portes("4")
cotxeMercedes1.get_Portes()