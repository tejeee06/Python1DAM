estudiants = ["Anna", "Joan", "Marta", "Pere"]
print(estudiants)

# Accés a elements individuals
print(estudiants[0])  # Anna
print(estudiants[2])  # Marta
 
# Accés invers (índex negatiu)
print(estudiants[-1])  # Pere (últim element)
 
# Subllistes (slicing)
print(estudiants[1:3])  # ['Joan', 'Marta']

# Afegir al final
estudiants.append("Laura")
print(estudiants)  # ['Anna', 'Joan', 'Marta', 'Pere', 'Laura']
 
# Afegir en una posició específica
estudiants.insert(2, "Sergi")
print(estudiants)  # ['Anna', 'Joan', 'Sergi', 'Marta', 'Pere', 'Laura']

# Eliminar un element específic
estudiants.remove("Joan")
print(estudiants)  # ['Anna', 'Sergi', 'Marta', 'Pere', 'Laura']
 
# Eliminar per índex
eliminat = estudiants.pop(1)
print(eliminat)  # Sergi
print(estudiants)  # ['Anna', 'Marta', 'Pere', 'Laura']

# Modificar un element per índex
estudiants[1] = "Marc"
print(estudiants)  # ['Anna', 'Marc', 'Pere', 'Laura']

# Iterar amb un bucle for
for estudiant in estudiants:
    print(f"Hola, {estudiant}!")

# Longitud de la llista
print(len(estudiants))  # 4
 
# Ordenar la llista
estudiants.sort()
print(estudiants)  # ['Anna', 'Laura', 'Marc', 'Pere']
 
# Invertir l'ordre
estudiants.reverse()
print(estudiants)  # ['Pere', 'Marc', 'Laura', 'Anna']
