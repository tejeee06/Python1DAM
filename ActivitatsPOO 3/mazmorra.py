import random

class Mazmorra:
    def __init__(self, columnes, files, densitatMurs):
        self.columnes = columnes
        self.files = files
        self.densitatMurs = densitatMurs
        self.grid = []
        self.posicioJugador = (0, 0)
        self.generarMazmorra()
    
    def generarMazmorra(self):
        print()
        self.grid = [
            ['#' if random.random() < self.densitatMurs else '.'
             for _ in range(self.columnes)]
            for _ in range(self.files)
        ]

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
        
        self.posicioJugador = random.choice(poscionsValides)
        i, j = self.posicioJugador
        self.grid[i][j] = 'P'
    
    def mostrarMazmorra(self):
        for fila in self.grid :
            print(''.join(fila))

m = Mazmorra(10, 10, 0.3)
m.generarMazmorra()
m.mostrarMazmorra()