import json

class Personatge :
    def __init__(self, name, lvl, exp, inventory):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.inventory = inventory
    
    def save(self, arxiu):
        dades = {
            'nombre': self.name,
            'nivel': self.lvl,
            'experiencia': self.exp,
            'inventario': self.inventory
        }

        with open(arxiu, 'w') as f :
            json.dump(dades, f, indent=4)
    
    @classmethod
    def charge(cls, arxiu):
        with open(arxiu, 'r') as f:
            dades = json.load(f)
            return cls(
                dades['nombre'],
                dades['nivel'],
                dades['experiencia'],
                dades['inventario']
            )

p1 = Personatge("Hechizero", 8, 120, ["Arco encantado", "Pocion de curacion"])
p1.save("Hechizero.json")
p1Carregat = p1.charge("Hechizero.json")
print(f"Nombre :   {p1Carregat.name}")
print(f"Nivel : {p1Carregat.lvl}")
print(f"Experiencia : {p1Carregat.exp}")
print(f"Inventario : {p1Carregat.inventory}")