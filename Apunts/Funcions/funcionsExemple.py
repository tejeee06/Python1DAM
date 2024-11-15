class Cotxe:
    # Mètode inicialitzador (constructor)
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model

    # Un mètode per mostrar la informació del cotxe
    def mostra_info(self):
        print(f"Marca: {self.marca}, Model: {self.model}")


# Creem un objecte de la classe Cotxe
cotxe1 = Cotxe("Toyota", "Corolla")
# Cridem el mètode mostra_info
cotxe1.mostra_info()
