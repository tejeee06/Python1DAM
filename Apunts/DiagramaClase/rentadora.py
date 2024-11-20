class Rentadora:

    def __init__(self, carrega, estat):
        self.carrega = carrega
        self.estat = estat
    
    def apagat(self):
        self.estat="apagat"
        print("La rentadora s'ha apagat")
    
    def encendre(self):
        if self.estat=="ences":
            print("La rentadora esta encesa")
        else:
            self.estat="ences"
            print("La rentadora s'acaba d encendre")
    
    def treureRoba(self):
        if self.estat=="apagat":
            self.carrega=0
            print("La rentadora s'ha buidat")
        else:
            print("La rentadora esta encesa , no es pot retirar la roba")
    
    def posarRoba(self, kg):
        if self.estat=="apagat":
            if self.carrega+kg<=8:
                self.carrega+=kg
                print(f"La rentadora te {kg} kg")
            else:
                print("Hi ha massa roba a la rentadora")
        else:
            print("Larentadora esta encesa")
    

rentadora1 = Rentadora(carrega=9, estat="apagat")
rentadora1.encendre()
rentadora1.apagat()
rentadora1.treureRoba()