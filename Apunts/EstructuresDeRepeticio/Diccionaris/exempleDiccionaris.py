# Informació d'un producte
producte = {
    "nom": "Portàtil",
    "preu": 799.99,
    "en_estoc": True
}
print(producte)

# Accedir a valors
print(producte["nom"])  # Portàtil
print(producte["preu"])  # 799.99
 
# Accés segur amb .get() (evita errors si la clau no existeix)
print(producte.get("descripció", "No disponible"))  # No disponible

# Afegir una nova clau-valor
producte["marca"] = "HP"
print(producte)
 
# Modificar un valor existent
producte["preu"] = 749.99
print(producte)

# Eliminar un element
del producte["en_estoc"]
print(producte)
 
# Utilitzar .pop() per eliminar i obtenir el valor
preu = producte.pop("preu")
print(preu)  # 749.99

print("marca" in producte)  # True
print("preu" in producte)  # False

# Iterar sobre les claus
for clau in producte:
    print(clau)
 
# Iterar sobre valors
for valor in producte.values():
    print(valor)
 
# Iterar sobre parells clau-valor
for clau, valor in producte.items():
    print(f"{clau}: {valor}")

# Obtenir només les claus o els valors
claus = producte.keys()
valors = producte.values()
print(claus)  # dict_keys(['nom', 'marca'])
print(valors)  # dict_values(['Portàtil', 'HP'])
 
# Longitud del diccionari
print(len(producte))  # 2
 
# Esborrar tots els elements
producte.clear()
print(producte)  # {}
