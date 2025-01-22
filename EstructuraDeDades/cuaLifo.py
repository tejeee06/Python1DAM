class cuaLifo:

    # Creem una llista buida per despres afegir els elemts
    def __init__(self):
        self.llista = []
    
    # Metode per afefgir un element a la llista
    def push(self, element):
        self.llista.append(element) # Afegeix un element a la part superior de la pila

    # Metode per eliminar l'ultim element agegit a la pila
    def pop(self):
        if not self.buit():
            return self.llista.pop()
        else :
            print("La pila esta buida , no es pot fer pop")
    
    # Metode per veure el darrer numero sense extreure'l
    def veureDarrer(self):
        if not self.buit():
            return self.llista[-1]
        else:
            print("La pila esta buida")

    # Metode per saber si la pila es buida o no 
    def buit(self):
        return len(self.llista) == 0 # Si esta buida retorna True , sino retorna False
    
    # Metode per saber la longitud actual de la pila
    def longitud(self):
        return len(self.llista)

if __name__ == "__main__":

    pila = cuaLifo()

    pila.push(1)
    pila.push(2)
    pila.push(3)

    print(pila.veureDarrer())
    print(pila.pop())
    print(pila.veureDarrer())
    print(pila.longitud())
    print(pila.buit())
    print(pila.pop())
    print(pila.pop())
    print(pila.buit())
    pila.push(7)
    print(pila.buit())
    print(pila.veureDarrer())