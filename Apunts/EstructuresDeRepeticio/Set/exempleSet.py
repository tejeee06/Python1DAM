# Crear un set d'animals
animals = {"gat", "gos", "ocell"}
print(animals)  # {'gat', 'gos', 'ocell'}

# Afegir un element
animals.add("conill")
print(animals)  # {'gat', 'gos', 'ocell', 'conill'}

# Eliminar un element existent
animals.remove("gos")
print(animals)  # {'gat', 'ocell', 'conill'}
 
# Eliminar amb seguretat (sense errors si no existeix)
animals.discard("peix")

print("gat" in animals)  # True
print("peix" in animals)  # False

# Unio de conjunts
set1 = {1, 2, 3}
set2 = {3, 4, 5}
unio = set1.union(set2)
print(unio)  # {1, 2, 3, 4, 5}

# Interseccio de conjunts
interseccio = set1.intersection(set2)
print(interseccio)  # {3}

# Diferencia de conjunts
diferencia = set1.difference(set2)
print(diferencia)  # {1, 2}

# Diferencia simetrica
# Troba els elements que son unics a a cada conjunt
diferencia_simetrica = set1.symmetric_difference(set2)
print(diferencia_simetrica)  # {1, 2, 4, 5}

# Iterar sobre un set
for animal in animals:
    print(f"L'animal és: {animal}")

# Longitud del set
print(len(animals))  # 3
 
# Esborrar tots els elements
animals.clear()
print(animals)  # set()
