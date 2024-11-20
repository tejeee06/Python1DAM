class Cotxe:
    def __init__(self, estat, velocitat):
        self.estat = estat
        self.velocitat = velocitat

    def engegar(self):
        if self.estat=="on":
            print("Ja està en marxa.")
        else:
            self.estat="on"
    def apagar(self):
        if self.estat=="off":
            print("Ja està parat")
        else:
            self.estat="off"

    def accelerar(self,km):
        if self.velocitat+km<=120:
            self.velocitat+=km
        else:
            self.velocitat=120
            print("No pots pasar dels 120km/h")

    def frenar(self, km):
        if self.velocitat-km<0:
            self.velocitat=0
            print("Cotxe aturat")
        else:
            self.velocitat-=km

    def donam_velocitat(self):
        print(f"La velocitat és: {self.velocitat}")

cotxe1=Cotxe("off",0)
cotxe1.engegar()
cotxe1.accelerar(50)
cotxe1.accelerar(100)
cotxe1.donam_velocitat()
cotxe1.frenar(110)
cotxe1.donam_velocitat()
cotxe1.frenar(20)
cotxe1.donam_velocitat()


