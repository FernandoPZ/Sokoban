'''
Autor: Fernando Pérez Suárez
Fecha de inicio: 13/07/2019
Fecha de finalizacion: 
Nombre: proyect_sokoban
'''

'''
0.- Personaje
1.- Caja
2.- Paredes
3.- Metas
4.- Pasillo
5.- Caja/meta
6.- Personaje/meta
'''

class Sokoban:

    #Variables generales
    def __init__ (self):
        pass
    
    #Mapas
    def crear_mapa1 (self):
        self.mapa1 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,3,2,2,2,2,2],
                      [2,2,2,4,2,2,2,2,2],
                      [2,2,2,1,4,1,3,2,2],
                      [2,3,4,1,0,2,2,2,2],
                      [2,2,2,2,1,2,2,2,2],
                      [2,2,2,2,3,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa1 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa1[position_row][position_col])
            print (smapa)
            smapa = ""

    def crear_mapa2 (self):
        self.mapa2 = [[2,2,2,2,2,2,2,2,2],
                      [2,4,4,4,2,2,2,2,2],
                      [2,4,1,0,2,2,2,2,2],
                      [2,4,1,1,2,2,2,3,2],
                      [2,2,2,4,2,2,2,3,2],
                      [2,2,2,4,4,4,4,3,2],
                      [2,2,4,4,4,2,4,4,2],
                      [2,2,4,4,4,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa2 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa2[position_row][position_col])
            print (smapa)
            smapa = ""

    def crear_mapa3 (self):
        self.mapa3 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,4,4,2,2,2,2,2],
                      [2,4,0,1,2,2,2,2,2],
                      [2,2,1,4,2,2,2,2,2],
                      [2,2,4,1,4,2,2,2,2],
                      [2,3,1,4,4,2,2,2,2],
                      [2,3,3,5,3,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa3 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa3[position_row][position_col])
            print (smapa)
            smapa = ""

    def crear_mapa4 (self):
        self.mapa4 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,0,4,2,2,2,2,2],
                      [2,2,4,1,4,4,2,2,2],
                      [2,2,2,4,2,4,2,2,2],
                      [2,3,2,4,2,4,4,2,2],
                      [2,3,1,4,4,2,4,2,2],
                      [2,3,4,4,4,1,4,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa4 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa4[position_row][position_col])
            print (smapa)
            smapa = ""

    def crear_mapa5 (self):
        self.mapa5 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,4,4,4,4,2,2],
                      [2,2,2,1,1,1,4,2,2],
                      [2,0,4,1,3,3,4,2,2],
                      [2,4,1,3,3,3,2,2,2],
                      [2,2,2,2,4,4,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa5 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa5[position_row][position_col])
            print (smapa)
            smapa = ""

    def crear_mapa6 (self):
        self.mapa6 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,4,4,0,2,2,2],
                      [2,4,4,1,3,4,2,2,2],
                      [2,4,4,3,1,3,4,2,2],
                      [2,2,2,4,5,1,4,2,2],
                      [2,2,2,4,4,4,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa6 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa6[position_row][position_col])
            print (smapa)
            smapa = ""

    def crear_mapa7 (self):
        self.mapa7 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,3,3,2,2,2,2],
                      [2,2,2,4,3,2,2,2,2],
                      [2,2,4,4,1,3,2,2,2],
                      [2,2,4,1,4,4,2,2,2],
                      [2,4,4,2,1,1,4,2,2],
                      [2,4,4,0,4,4,4,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    def imprimir_mapa7 (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa7[position_row][position_col])
            print (smapa)
            smapa = ""

    #Personaje
    def personaje (self):
        for p in range(len(self.mapa1)):
            if self.mapa1[p] == 0:
                self.position_col = p
    
    #Movimientos
    def movimiento_derecha (self):
        if self.mapa1[self.position_col + 1] == 4:
            tem_col = self.position_col
            self.position_col = self.position_col - 1
            self.mapa1[tem_col] = 4
            self.mapa1[self.position_col] = 0
    
    def instrucciones (self):
        print ("Movimientos:    [W]   ")
        print ("             [A][S][D]")
        print ("[W] = Arriba")
        print ("[S] = Abajo")
        print ("[A] = Izquierda")
        print ("[D] = Derecha")

    def movimiento_izquierda (self):
        position_col = position_col-1

    def movimiento_arriba (self):
        position_row = position_row-1

    def movimiento_abajo (self):
        position_row = position_row+1

    def nivel1(self):
        self.crear_mapa1()
        self.personaje()
        while True:
            print ("Nivel 1")
            print ("¡A jugar!")
            print ("---------")
            self.imprimir_mapa1()
            print ("---------")
            self.instrucciones()
            move = input("")
            if move == "w":
                self.movimiento_arriba()
            elif move == "s":
                self.movimiento_abajo()
            elif move == "a":
                self.movimiento_izquierda()
            elif move == "d":
                self.movimiento_derecha()
            elif move == "r":
                break

pop = Sokoban()
print("¡Bienvenido a mi juego de sokoban!")
print("--NIVELES--")
print("[1] Nivel 1")
print("[2] Nivel 2")
print("[3] Nivel 3")
print("[4] Nivel 4")
print("[5] Nivel 5")
print("[6] Nivel 6")
print("[7] Nivel 7")
eleccion = input ("Escoja un nivel: \n")

#Opcion1
if eleccion == "1":
    pop.nivel1()

elif eleccion == "2":
    pop.nivel2()
