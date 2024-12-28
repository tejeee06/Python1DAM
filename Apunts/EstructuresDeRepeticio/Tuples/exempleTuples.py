# Tupla de dies de la setmana
dies = ("Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge")
print(dies)

# Accés a elements individuals
print(dies[0])  # Dilluns
print(dies[4])  # Divendres
 
# Accés invers (índex negatiu)
print(dies[-1])  # Diumenge
 
# Subtuples (slicing)
print(dies[1:4])  # ('Dimarts', 'Dimecres', 'Dijous')

# Iterar amb un bucle for
for dia in dies:
    print(f"Avui és {dia}.")

# Unir tuples
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_unida = tupla1 + tupla2
print(tupla_unida)  # (1, 2, 3, 4, 5, 6)

# Multiplicar tuples
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Determinal la longitud de la tupla
print(len(dies))  # 7

# Cercar un element
print("Dissabte" in dies)  # True
print(dies.index("Dimarts"))  # 1
