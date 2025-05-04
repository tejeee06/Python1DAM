# Classe Motor
class Motor:
    # Constructora de la classe Motor
    def __init__(self, tipoMotor, potencia):
        self.tipoMotor = tipoMotor
        self.potencia = potencia
        self.motorEncendido = False
    
    # Metodos de la classe Motor
    def encender(self):
        if not self.motorEncendido:
            self.motorEncendido = True
            print("Encendideno el motor......")
        else :
            print("Error , el motor ya esta encendido")
    
    def apagar(self):
        if self.motorEncendido:
            self.motorEncendido = False
            print("Apagando el motor.....")
        else :
            print("Error , el motor ya esta apagado")
    
# Classe Coche
class Coche:
    # Constructora de la classe Coche
    def __init__(self, marca, modelo, año, tipoMotor, potencia):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.motor = Motor(tipoMotor, potencia) # Composicion
        self.enMarcha = False
    
    # Metodos de la classe Coche
    def arrancar(self):
        if not self.enMarcha:
            self.motor.encender()
            self.enMarcha = True
            print(f"Coche {self.marca} {self.modelo} arrancado.")
        else :
            print("Error , el coche ya esta arrancado")
    
    def detener(self):
        if self.enMarcha:
            self.enMarcha = False
            print(f"Coche {self.marca} {self.modelo} detenido.")
            self.motor.apagar()
        else :
            print("Error , el coche ya esta detenido")

c = Coche("Alfa Romeo", "Stelvio", 2023, "V6 Bi-Turbo", "280cv")
c.arrancar()
c.arrancar()
c.detener()
c.detener()