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

import os
class Sokoban:

    #Variables generales
    def __init__ (self):
        self.mapa = []
        self.position_col = 0
        self.position_row = 0
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

        self.mapa3 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,4,4,2,2,2,2,2],
                      [2,4,0,1,2,2,2,2,2],
                      [2,2,1,4,2,2,2,2,2],
                      [2,2,4,1,4,2,2,2,2],
                      [2,3,1,4,4,2,2,2,2],
                      [2,3,3,5,3,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]

        self.mapa4 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,0,4,2,2,2,2,2],
                      [2,2,4,1,4,4,2,2,2],
                      [2,2,2,4,2,4,2,2,2],
                      [2,3,2,4,2,4,4,2,2],
                      [2,3,1,4,4,2,4,2,2],
                      [2,3,4,4,4,1,4,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]

        self.mapa5 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,4,4,4,4,2,2],
                      [2,2,2,1,1,1,4,2,2],
                      [2,0,4,1,3,3,4,2,2],
                      [2,4,1,3,3,3,2,2,2],
                      [2,2,2,2,4,4,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]

        self.mapa6 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,4,4,0,2,2,2],
                      [2,4,4,1,3,4,2,2,2],
                      [2,4,4,3,1,3,4,2,2],
                      [2,2,2,4,5,1,4,2,2],
                      [2,2,2,4,4,4,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]

        self.mapa7 = [[2,2,2,2,2,2,2,2,2],
                      [2,2,2,3,3,2,2,2,2],
                      [2,2,2,4,3,2,2,2,2],
                      [2,2,4,4,1,3,2,2,2],
                      [2,2,4,1,4,4,2,2,2],
                      [2,4,4,2,1,1,4,2,2],
                      [2,4,4,0,4,4,4,2,2],
                      [2,2,2,2,2,2,2,2,2],
                      [2,2,2,2,2,2,2,2,2]]
    
    #Personaje
    def personaje (self):
        for p in range(len(self.mapa)):
            if self.mapa[p] == 0:
                self.position_col = p

    #Impresion de mapas
    def mostrar_mapa (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(self.mapa1()[position_row][position_col])
            print (smapa)
            smapa = ""
        tem_row = position_row
        tem_col = position_col
    
    #Movimientos
    def movimiento_derecha (self):
        if mapa[self.position_col + 1] == 4:
            tem_col = self.position_col
            self.position_col = self.position_col - 1
            mapa[tem_col] = 4
            mapa[self.position_col] = 0
    
    
    def movimiento_izquierda (self):
        position_col = position_col-1

    def movimiento_arriba (self):
        position_row = position_row-1

    def movimiento_abajo (self):
        position_row = position_row+1


object = Sokoban()
print("¡Bienvenido a mi juego de sokoban!")
print("---NIVELES---")
print("[1] Nivel 1")
print("[2] Nivel 2")
print("[3] Nivel 3")
print("[4] Nivel 4")
print("[5] Nivel 5")
print("[6] Nivel 6")
print("[7] Nivel 7")
eleccion = input ("Escoja un nivel: \n")

#Opcion1
if eleccion == 1:
    os.system('cls')
    mapa = object.crear_mapa1()
    print ("Nivel 1")
    print ("¡A jugar!")
    print ("---------")
    print (object.mostrar_mapa())
    print (object.personaje())
    print ("---------")
    print ("Movimientos:    [W]   ")
    print ("             [A][S][D]")
    print ("[W] = Arriba")
    print ("[S] = Abajo")
    print ("[A] = Izquierda")
    print ("[D] = Derecha")
    move = input ("")
    while True:
        if move == 'w' and object.mapa1()[position_col+1]!=2:
            print(object.movimiento_arriba())
            print(object.mapa1())[tem_col][tem_row]=4
            print(object.mapa1())[position_col][position_row]=0
        elif move == 's' and object.mapa1()[position_col-1]!=2:
            object.movimiento_abajo()
            object.mapa1()[tem_col][tem_row]=4
            object.mapa1()[position_col][position_row]=0
        elif move == 'a' and object.mapa1()[position_row-1]!=2:
            object.movimiento_izquierda()
            object.mapa1()[tem_col][tem_row]=4
            object.mapa1()[position_col][position_row]=0
        elif move == 'd' and object.mapa1()[position_row+1]!=2:
            object.movimiento_derecha()
            object.mapa1()[tem_col][tem_row]=4
            object.mapa1()[position_col][position_row]=0
