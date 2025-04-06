class Inventari:
    def __init__(self):
        self.objectes = []
    
    def afegirObjecte(self, nom, cantitat):
        if cantitat <= 0:
            print("Error , la cantidad ha de ser positiva")
            return
        
        for objecte in self.objectes:
            if objecte['nom'] == nom:
                objecte['cantidad'] += cantitat
                print(f"Se han añadido {cantitat} unidades de {nom}")
                return
        
        self.objectes.append({'nom': nom, 'cantitat': cantitat})
        print(f"Se ha añadido {nom} al inventario")
    
    def eliminarObjecte(self, nom, cantitat):
        if cantitat <= 0:
            print("Error , la cantidad ha de ser positiva")
            return False
        
        for objecte in self.objectes:
            if objecte['nom'] == nom:
                if objecte['cantitat'] < cantitat:
                    print(f"Error , no hay suficiente cantidad de {nom} para eliminar")
                    return False
                
                objecte['cantitat'] -= cantitat
                if objecte['cantitat'] == 0:
                    self.objectes.remove(objecte)
                    print(f"Se ha eliminado {nom} completamente del inventario")
                else:
                    print(f"Se ha eliminado {cantitat} unidades de {nom} del inventario")
                return True
        print(f"Error : {nom} no existe en el inventario")
        return False
    
    def llistarInventari(self):
        if not self.objectes:
            print("El inventario esta vacio")
            return
        
        print("Inventari : ")
        for i, objecte in enumerate(self.objectes, 1):
            print(f"{i}. {objecte['nom']} - {objecte['cantitat']} unidades")

i = Inventari()
i.llistarInventari()
i.afegirObjecte("Pocion de curacion", 4)
i.afegirObjecte("Espada de Fierro", 1)
i.llistarInventari()
i.eliminarObjecte("Pocion de curacion",1)
i.eliminarObjecte("Espada de Fierro", 3)
i.llistarInventari()