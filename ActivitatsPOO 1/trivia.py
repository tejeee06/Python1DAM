class Pregunta:
    def __init__(self, pregunta,  opcions, respostaCorrecta):
        self.pregunta = pregunta
        self.opcions = opcions
        self.respostaCorrecta = respostaCorrecta
    
    def is_correct(self, resposta):
        return resposta == self.respostaCorrecta

class JocTrivia:
    def __init__(self):
        self.preguntas = []
        self.puntuacio = 0
    
    def afegirPregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def jugar(self):
        print("Juego de Trivia ! ")

        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"Pregunta {i}: {pregunta.pregunta}")
            for idx, opcio in enumerate(pregunta.opcions, 1):
                print(f"{idx}. {opcio}")
            
            while True:
                try:
                    resposta = int(input("Selecciona la respuesta correcta : "))
                    if 1 <= resposta <= 4:
                        respostaIndex = resposta - 1
                        break
                    else:
                        print("Error , opcion fuera del rango.")
                except ValueError:
                    print("Error , tienes que introducir un numero.")
            
            if pregunta.is_correct(respostaIndex):
                print("")
                print("Respuesta correcta !!!")
                print("")
                self.puntuacio += 1
            else :
                print("")
                print(f"Respuesta incorrecta. La respuesta correcta es : {pregunta.opcions[pregunta.respostaCorrecta]}")
                print("")
        
        self.mostrarResultat()
    
    def mostrarResultat(self):
        totalPreguntes = len(self.preguntas)
        print(f"Resultado Final : {self.puntuacio}/{totalPreguntes}")

        if self.puntuacio == totalPreguntes:
            print("Felicidades has acertado todas  !!!!")
        elif self.puntuacio >= totalPreguntes * 0.9:
            print("Muy bien , casi perfecto")
        elif self.puntuacio >= totalPreguntes * 0.7:
            print("Buen conocimiento !!!!")
        elif self.puntuacio >= totalPreguntes * 0.5:
            print("Por los pelos , puedes mejorar.")
        elif self.puntuacio == 0:
            print("Estabas jugando a adivinar ? ")
        else :
            print("Puedes mejorar.")

if __name__ == "__main__":
    joc = JocTrivia()

    joc.afegirPregunta(Pregunta(
        "¿En que año se lanzo  el primer 'The legend of Zelda' ? ",
        ["1985", "1986", "1987", "1988"],
        1
    ))
    joc.afegirPregunta(Pregunta(
        "¿Quien es el protagonista original de 'Resident Evil' ? ",
        ["Chris Redfield", "Jill Valentine", "Leon S.Kennedy", "Paul Walker"],
        0
    ))
    joc.afegirPregunta(Pregunta(
        "¿Cual es el objetivo principal de Minecraft",
        ["Matar a aldeanos", "Encontrar diamantes", "Derrotar al Ender Dragon", "Sobrevivir"],
        2
    ))
    joc.afegirPregunta(Pregunta(
        "¿De que mitologia proviene Kratos ?",
        ["Griega", "Nordica", "China", "Egipcia"],
        0
    ))
    joc.afegirPregunta(Pregunta(
        "¿Que dos primeros Pokemon se lanzaron fuera de Japon ?",
        ["Pokemon Blanco y Negro", "Pokemon x y", "Pokemon Rojo y Azul", "Pokemon Oro y Plata"],
        2
    ))
    joc.afegirPregunta(Pregunta(
        "¿En que epoca esta ambientado 'Assassin's Creed Valhalla' ? ",
        ["Edad Media", "Antiguo Egipto", "Antigua Grecia", "Era Vikinga"],
        3
    ))
    joc.afegirPregunta(Pregunta(
        "¿Quien es el protagonista de 'Final Fantasy VII' ?",
        ["Cloud Strife", "Squall LeonHart", "Titus", "Zidane Tribal"],
        0
    ))
    joc.afegirPregunta(Pregunta(
        "¿Cual es la moneda de 'Animal Crossing' ?",
        ["Ballas", "Soles", "Estrellas", "Bayas"],
        3
    ))
    joc.afegirPregunta(Pregunta(
        "¿Que puede hacer el Impostor en Among US que los tripulantes no ?",
        ["Realizar Tareas", "Sabotear Sistemas", "Reportar Cuerpos", "Usar Camaras"],
        1
    ))
    joc.afegirPregunta(Pregunta(
        "¿Que restauras al sentarte en una hogera en Dark Souls ?",
        ["Vida", "Estus Flask", "Humanidad", "Todas las anteriores" ],
        3
    ))

    joc.jugar()
