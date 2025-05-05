from datetime import datetime

# Classe Libro
class Libro:
    # Metodo Constructor
    def __init__(self, idLibro, tituloLibro, autorLibro, copias):
        self.idLibro = idLibro
        self.tituloLibro = tituloLibro
        self.autorLibro = autorLibro
        self.copias = copias
    
    # Metodos de la classe
    def mostrarInfoLibro(self):
        return f"Id del libro: {self.idLibro}, Título del Libro: {self.tituloLibro}, Autor del Libro: {self.autorLibro}, Copias existentes: {self.copias}"

# Classe Usuario
class Usuario:
    # Metodo Constructor
    def __init__(self, idUsuario, nombreUsuario, apellidosUsuario, DNIusuario, emailUsuario):
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.apellidosUsuario = apellidosUsuario
        self.DNIusuario = DNIusuario
        self.emailUsuario = emailUsuario
        self.librosPrestados = []
    
    # Metodos de la classe
    def mostrarInfoUsuario(self):
        return f"Id del Usuario: {self.idUsuario}, Nombre del Usuario: {self.nombreUsuario}, Apellidos: {self.apellidosUsuario}, E-Mail: {self.emailUsuario}"

# Classe Prestamo
class Prestamo:
    # Metodo Constructor
    def __init__(self, idPrestamo, libro, usuario, fechaPrestamo, fechaDevolucion=None):
        self.idPrestamo = idPrestamo
        self.libro = libro
        self.usuario = usuario
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucion = fechaDevolucion

    # Metodos de la classe
    def mostrarInfoPrestamo(self):
        if self.fechaDevolucion:
            devolucion = self.fechaDevolucion
        else:
            devolucion = "No devuelto"
        return f"Id Préstamo: {self.idPrestamo}, Libro: {self.libro.tituloLibro}, Usuario: {self.usuario.nombreUsuario}, Fecha Préstamo: {self.fechaPrestamo}, Fecha Devolución: {devolucion}"

# Classe Bibliotecario
class Bibliotecario:
    # Metodo Constructor
    def __init__(self, idBibliotecario, nombreBibliotecario):
        self.idBibliotecario = idBibliotecario
        self.nombreBibliotecario = nombreBibliotecario
        self.libros = []  
        self.usuarios = []  
        self.prestamos = []  
        self.contadorPrestamos = 0  # Genera ids unicos para los prestamos

    # Metodos de la classe
    def registrarLibro(self, idLibro, tituloLibro, autorLibro, copias):
        nuevoLibro = Libro(idLibro, tituloLibro, autorLibro, copias)
        self.libros.append(nuevoLibro)
        return f"Libro '{tituloLibro}' registrado con éxito."

    def registrarUsuario(self, idUsuario, nombreUsuario, apellidosUsuario, DNIusuario, emailUsuario):
        nuevoUsuario = Usuario(idUsuario, nombreUsuario, apellidosUsuario, DNIusuario, emailUsuario)
        self.usuarios.append(nuevoUsuario)
        return f"Usuario '{nombreUsuario} {apellidosUsuario}' registrado con éxito."

    def realizarPrestamo(self, idLibro, idUsuario):
        # Busca el libro y el usuario que realiza el prestamo
        libro = None
        for l in self.libros:
            if l.idLibro == idLibro:
                libro = l
                break
        if not libro:
            return "Error: Libro no encontrado."
        
        if libro.copias <= 0:
            return "Error: No hay copias disponibles del libro."

        usuario = None
        for u in self.usuarios:
            if u.idUsuario == idUsuario:
                usuario = u
                break
        if not usuario:
            return "Error: Usuario no encontrado."

        # Crea el Prestamo
        self.contadorPrestamos += 1
        fechaPrestamo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nuevoPrestamo = Prestamo(self.contadorPrestamos, libro, usuario, fechaPrestamo)
        self.prestamos.append(nuevoPrestamo)

        libro.copias -= 1
        usuario.librosPrestados.append(libro)

        return f"Préstamo registrado con éxito: {nuevoPrestamo.mostrarInfoPrestamo()}"

    def realizarDevolucion(self, idPrestamo):
        prestamo = None
        for p in self.prestamos:
            if p.idPrestamo == idPrestamo:
                prestamo = p
                break
        if not prestamo:
            return "Error: Préstamo no encontrado."
        
        if prestamo.fechaDevolucion:
            return "Error: El préstamo ya fue devuelto."

        prestamo.fechaDevolucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prestamo.libro.copias += 1
        prestamo.usuario.librosPrestados.remove(prestamo.libro)

        return f"Devolución registrada con éxito: {prestamo.mostrarInfoPrestamo()}"

    def mostrarLibros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join(libro.mostrarInfoLibro() for libro in self.libros)

    def mostrarUsuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        return "\n".join(usuario.mostrarInfoUsuario() for usuario in self.usuarios)

    def mostrarPrestamos(self):
        if not self.prestamos:
            return "No hay préstamos registrados."
        return "\n".join(prestamo.mostrarInfoPrestamo() for prestamo in self.prestamos)

# Ejemplo de uso del programa
bibliotecario = Bibliotecario(1, "Juan Pérez")
print(bibliotecario.registrarLibro(1, "Cien años de soledad", "Gabriel García Márquez", 3))
print(bibliotecario.registrarLibro(2, "1984", "George Orwell", 2))
print(bibliotecario.registrarUsuario(1, "Ana", "Gómez", "12345678A", "ana@gmail.com"))
print(bibliotecario.realizarPrestamo(1, 1))
print(bibliotecario.realizarDevolucion(1))