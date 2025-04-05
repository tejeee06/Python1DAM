import random

class Mapa:
    def __init__(self, files, columnes, densitatMurs, seed = None):
        self.files = files
        self.columnes = columnes
        self.densitatMurs = densitatMurs
        self.seed = seed
        self.grid = []
        self.posicioJugador =(0, 0)
        self.generarMapa()
    
    def generarMapa(self):
        if self.seed is not None:
            random.seed(self.seed)
        
        #Genera la base del mapa
        self.grid = [
            ['#' if random.random() < self.densitatMurs else '.'
             for _ in range(self.columnes)]
            for _ in range(self.files)
        ]

        #Posicio valida per al jugador
        poscionsValides = [
            (i, j)
            for i in range(self.files)
            for j in range(self.columnes)
            if self.grid[i][j] == '.'
        ]

        if not poscionsValides:
            i = random.randint(0, self.files -1)
            j = random.randint(0, self.columnes -1)
            self.grid[i][j] == '.'
            poscionsValides = [(i, j)]
        
        #Posar al jugador
        self.posicioJugador = random.choice(poscionsValides)
        i, j = self.posicioJugador
        self.grid[i][j] = 'P'
    
    def mostrarMapa(self):
        for fila in self.grid :
            print(''.join(fila))
    
    def obtenirCelda(self, x, y):
        if 0 <= x < self.files and 0 < y < self.columnes:
            return self.grid[x][y]
        return '#'
    
    def esTransitable(self, x, y):
        return self.obtenirCelda(x, y) in ['.', 'P']
    
    # Metode per moure el personatge
    def moureJugador(self, direccio):
        direccio = direccio.upper()
        x, y = self.posicioJugador
        new_X, new_Y = x, y

        if direccio == "W" : new_X -= 1
        elif direccio == "S": new_X += 1
        elif direccio == "A": new_Y -= 1
        elif direccio == "D": new_Y += 1
        else :
            return False
        
        # Actualitzem la posicio
        if self.esTransitable(new_X, new_Y):
            self.grid[x][y] = '.'  # Posició anterior buida
            self.grid[new_X][new_Y] = 'P'  # Nova posició jugador
            self.posicioJugador = (new_X, new_Y)
            return True
        return False

mapa = Mapa(files=8, columnes=12, densitatMurs=0.25, seed=42)
print("Generando el mapa...")

while True:
    print("\n" * 2)
    mapa.mostrarMapa()
    print()
    mov = input("Movimento (WASD) o Q para salir ")
    if mov == "Q":
        print("Saliendo del juego...")
        break
    elif mov in ["W", "A", "S", "D"] :
        if mapa.moureJugador(mov) :
            print("Movimento realizado") 
        else :
            print("Moviento boqueado")
    else :
        print("Error , entrada no valida")
