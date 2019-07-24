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
        for position_col in self.mapa1:
            for position_row in position_col:
                smapa = smapa+" "+str(position_row)
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
        for position_col in self.mapa2:
            for position_row in position_col:
                smapa = smapa+" "+str(position_row)
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

    '''
    #Direcciones
    def direccion (self):
        contador_col=0
        contador_row=0
        per_col=0
        per_row=0
    '''

    #Personaje
    def personaje1 (self):
        contador_col=0
        contador_row=0
        per_col=0
        per_row=0
        for search_col in mapa:
            for search_row in search_col:
                if search_row != 0 and search_row != 6:
                    contador_row=contador_row+1
                else:
                    per_col=contador_col
                    per_row=contador_row
                    break
            contador_col=contador_col+1
            contador_row=0

    #Muestra los controles
    def instrucciones (self):
        print ("Movimientos:    [W]   ")
        print ("             [A][S][D]")
        print ("[W] = Arriba")
        print ("[S] = Abajo")
        print ("[A] = Izquierda")
        print ("[D] = Derecha")
    
    #Movimientos
    def movimiento_derecha (self):
        if self.mapa1[self.position_col - 1] == 4:
            tem_col = self.position_col
            self.position_col = self.position_col - 1
            self.mapa1[tem_col] = 4
            self.mapa1[self.position_col] = 0
        elif self.mapa1[self.position_col - 1] == 1:
            tem_col = self.position_col

    def movimiento_izquierda (self):
        if self.mapa1[self.position_col + 1] == 4:
            tem_col = self.position_col
            self.position_col = self.position_col + 1
            self.mapa1[tem_col] = 4
            self.mapa1[self.position_col] = 0

    def movimiento_arriba (self):
        if mapa[per_col-1][per_row]==2:
            print("hay una pared, no puedes pasar")

        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
            mapa[per_col][per_row]=3
            mapa[per_col-2][per_row]=1
            per_col=per_col-1
            mapa[per_col][per_row]=0
            imprimir_mapa1()

        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
            mapa[per_col][per_row]=3
            mapa[per_col-2][per_row]=5
            per_col=per_col-1
            mapa[per_col][per_row]=0
            imprimir_mapa1()
    
        elif mapa[per_col][monoY]==6 and mapa[per_col-1][monoY]==3:
            mapa[per_col][monoY]=3
            per_col=per_col-1
            mapa[per_col][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=3
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==4:
            mapa[monoX][monoY]=3
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()
       
        elif mapa[monoX-1][monoY]==4:
            mapa[monoX][monoY]=4
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()   

        elif mapa[monoX-1][monoY]==3:
            mapa[monoX][monoY]=4
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==4:
            mapa[monoX][monoY]=4
            mapa[monoX-2][monoY]=1
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()

        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==2:
            print ("No puedes atravesar el muro por ti mismo, ¿Qué te hace pensar que con una caja lo haras?")

        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=4
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()
        
        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==1:
            print("Con que trabajos mueves una jajaja")

        elif mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=4
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==4:
            mapa[monoX][monoY]=3
            mapa[monoX-2][monoY]=1
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==2:
            print("No puedes atravesar los muros... aún ;)")
        
#alto
    def movimiento_abajo (self):
        if self.mapa1[self.position_row + 1] == 4:
            tem_row = self.position_row
            self.position_row = self.position_row + 1
            self.mapa1[tem_row] = 4
            self.mapa1[self.position_row] = 0

    def nivel1(self):
        os. system ("cls")
        self.personaje1()
        self.crear_mapa1()
        while True:
            os. system ("cls")
            print (" Nivel 1 ")
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
    mapa = pop.crear_mapa1()
    pop.nivel1()

elif eleccion == "2":
    pop.nivel2()

elif eleccion == "3":
    pop.nivel3()
