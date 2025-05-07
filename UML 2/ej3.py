class PlataformaEducativa:
    def __init__(self):
        self.usuarios = {"estudiante1": "contraseña123"}
        self.cursos = ["Matemáticas", "Programación", "Historia"]
        self.inscrito = False
        self.pago_confirmado = False

    def iniciar_sesion(self, usuario, contraseña):
        if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
            print("Sesión iniciada con éxito.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False

    def buscar_cursos(self):
        print("Cursos disponibles:", self.cursos)
        return self.cursos

    def seleccionar_curso(self, curso):
        if curso in self.cursos:
            print(f"Curso {curso} seleccionado.")
            return True
        else:
            print("Curso no disponible.")
            return False

    def completar_formulario(self, datos):
        if datos.get("nombre") and datos.get("email"):
            print("Formulario completado con éxito.")
            self.inscrito = True
            return True
        else:
            print("Formulario incompleto.")
            return False

    def realizar_pago(self, monto):
        if monto > 0:
            print("Pago realizado con éxito.")
            self.pago_confirmado = True
            return True
        else:
            print("Error en el pago.")
            return False

    def confirmar_inscripcion(self):
        if self.inscrito and self.pago_confirmado:
            print("Inscripción confirmada. ¡Bienvenido al curso!")
            return True
        else:
            print("Inscripción no confirmada. Verifica el formulario o el pago.")
            return False

def main():
    plataforma = PlataformaEducativa()
    
    if plataforma.iniciar_sesion("estudiante1", "contraseña123"):
        plataforma.buscar_cursos()

        if plataforma.seleccionar_curso("Programación"):
            datos = {"nombre": "Juan Pérez", "email": "juan@example.com"}

            if plataforma.completar_formulario(datos):

                if plataforma.realizar_pago(100):
                    plataforma.confirmar_inscripcion()

if __name__ == "__main__":
    main()