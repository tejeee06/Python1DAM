class Cliente:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.carrito = []

    def iniciar_sesion(self, email, contraseña):
        return self.email == email and self.contraseña == contraseña

    def añadir_al_carrito(self, producto, cantidad=1):
        self.carrito.append({"producto": producto, "cantidad": cantidad})
        print(f"{cantidad} x {producto.nombre} añadido al carrito.")

    def ver_carrito(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            print("Contenido del carrito:")
            for item in self.carrito:
                print(f"{item['cantidad']} x {item['producto'].nombre} - ${item['producto'].precio * item['cantidad']}")


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_producto(self) :
        return f"Producto : {self.nombre} {self.precio}$"


class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos 
        self.estado = "creado"

    def actualizar_estado(self, nuevo_estado):
        estados_validos = ["creado", "pagado", "enviado", "entregado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            print(f"Estado del pedido actualizado a: {self.estado}")
        else:
            print("Estado no válido.")

    def mostrar_pedido(self):
        print(f"Pedido de {self.cliente.nombre} - Estado: {self.estado}")
        for item in self.productos:
            print(f"{item['cantidad']} x {item['producto'].nombre} - ${item['producto'].precio * item['cantidad']}")


class TiendaOnline:
    def __init__(self):
        self.clientes = []
        self.productos = []

    def registrar_cliente(self, nombre, email, contraseña):
        cliente = Cliente(nombre, email, contraseña)
        self.clientes.append(cliente)
        print(f"Cliente {nombre} registrado con éxito.")
        return cliente

    def añadir_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.productos.append(producto)
        print(f"Producto {nombre} añadido a la tienda.")
        return producto

    def realizar_pedido(self, cliente):
        if not cliente.carrito:
            print("No se puede realizar el pedido: el carrito está vacío.")
            return None
        pedido = Pedido(cliente, cliente.carrito.copy())
        cliente.carrito = [] 
        print("Pedido realizado con éxito.")
        return pedido

if __name__ == "__main__":
    tienda = TiendaOnline()

    cliente = tienda.registrar_cliente("Ana", "ana@email.com", "1234")

    prod1 = tienda.añadir_producto("Libro", 20)
    prod2 = tienda.añadir_producto("Lápiz", 2)

    if cliente.iniciar_sesion("ana@email.com", "1234"):
        print("Inicio de sesión exitoso.")

    cliente.añadir_al_carrito(prod1, 2)
    cliente.añadir_al_carrito(prod2, 5)
    cliente.ver_carrito()

    pedido = tienda.realizar_pedido(cliente)
    if pedido:
        pedido.mostrar_pedido()
        pedido.actualizar_estado("pagado")
        pedido.actualizar_estado("enviado")
        pedido.actualizar_estado("entregado")