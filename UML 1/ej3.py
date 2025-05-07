class Desarrollador:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.videojuegos = []

    def agregar_videojuego(self, videojuego):
        self.videojuegos.append(videojuego)

    def __str__(self):
        return f"Desarrollador: {self.nombre}, País: {self.pais}"


class Videojuego:
    def __init__(self, titulo, desarrollador, precio):
        self.titulo = titulo
        self.desarrollador = desarrollador
        self.precio = precio
        self.en_stock = True
        desarrollador.agregar_videojuego(self)

    def vender(self):
        if self.en_stock:
            self.en_stock = False
            return True
        return False

    def reponer(self):
        self.en_stock = True

    def __str__(self):
        return f"Videojuego: {self.titulo}, Precio: ${self.precio}, En stock: {self.en_stock}"


class Cliente:
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.videojuegos_comprados = []

    def comprar(self, videojuego):
        if videojuego.vender():
            self.videojuegos_comprados.append(videojuego)
            return True
        return False

    def __str__(self):
        return f"Cliente: {self.nombre}, ID: {self.id_cliente}"


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.videojuegos = []
        self.clientes = []

    def agregar_videojuego(self, videojuego):
        self.videojuegos.append(videojuego)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def __str__(self):
        return f"Tienda: {self.nombre}, Videojuegos: {len(self.videojuegos)}, Clientes: {len(self.clientes)}"


# Ejemplo de uso
if __name__ == "__main__":
    desarrollador = Desarrollador("Nintendo", "Japón")
    videojuego = Videojuego("The Legend of Zelda", desarrollador, 59.99)
    cliente = Cliente("Ana Gómez", "C001")
    tienda = Tienda("GameStore")

    tienda.agregar_videojuego(videojuego)
    tienda.registrar_cliente(cliente)
    cliente.comprar(videojuego)

    print(tienda)
    print(desarrollador)
    print(videojuego)
    print(cliente)