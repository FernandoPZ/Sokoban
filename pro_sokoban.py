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
        position_col=0
        position_row=0
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

    '''
    #Direcciones
    def direccion (self):
        contador_col=0
        contador_row=0
        per_col=0
        per_row=0
    '''

    #Personaje
    def personaje (self):
        contador_col=0
        contador_row=0
        per_col=0
        per_row=0
        for search_col in self.mapa1:
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
    def movimiento_arriba (self):

        if self.mapa1[per_col-1][per_row]==2:
            print("hay una pared, no puedes pasar")

        elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==2:
            print("hay una pared, no puedes pasar")

        elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==1:
            print("No puedes empujar 2 cajas")

        elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==2:
            print ("Obstaculo enfrente")

        elif mapa[per_col-1][per_row]==4:
            mapa[per_col][per_row]=4
            per_col=per_col-1
            mapa[per_col][per_row]=0
            print (self.imprimir_mapa())   

        elif mapa[per_col-1][per_row]==3:
            mapa[per_col][per_row]=4
            per_col=per_col-1
            mapa[per_col][per_row]=6
            print (self.imprimir_mapa())
        
        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==4:
            mapa[per_col][per_row]=3
            per_col=per_col-1
            mapa[per_col][per_row]=0
            print (self.imprimir_mapa())
       
        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==3:
            mapa[per_col][per_row]=3
            per_col=per_col-1
            mapa[per_col][per_row]=6
            print (self.imprimir_mapa())

        elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
            mapa[per_col][per_row]=4
            mapa[per_col-2][per_row]=1
            per_col=per_col-1
            mapa[per_col][per_row]=0
            print (self.imprimir_mapa())

        elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
            mapa[per_col][per_row]=4
            mapa[per_col-2][per_row]=5
            per_col=per_col-1
            mapa[per_col][per_row]=0
            print (self.imprimir_mapa())

        elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
            mapa[per_col][per_row]=4
            mapa[per_col-2][per_row]=5
            per_col=per_col-1
            mapa[per_col][per_row]=6
            print (self.imprimir_mapa())

        elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==4:
            mapa[per_col][per_row]=3
            mapa[per_col-2][per_row]=1
            per_col=per_col-1
            mapa[per_col][per_row]=6
            print (self.imprimir_mapa())

        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
            mapa[per_col][per_row]=3
            mapa[per_col-2][per_row]=1
            per_col=per_col-1
            mapa[per_col][per_row]=0
            print (self.imprimir_mapa())

        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
            mapa[per_col][per_row]=3
            mapa[per_col-2][per_row]=5
            per_col=per_col-1
            mapa[per_col][per_row]=0
            print (self.imprimir_mapa())
        
        elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
            mapa[per_col][per_row]=3
            mapa[per_col-2][per_row]=5
            per_col=per_col-1
            mapa[per_col][per_row]=6
            print (self.imprimir_mapa())
        
    def movimiento_abajo (self):
        if mapa[per_col+1][per_row]==2:
            print("hay una pared, no puedes pasar")

    def movimiento_derecha (self):
        if mapa[per_col][per_row+1]==2:
            print("hay una pared, no puedes pasar")

    def movimiento_izquierda (self):
        if mapa[per_col][per_row-1]==2:
            print("hay una pared, no puedes pasar")

    def jugar (self):
        os. system ("cls")
        self.personaje()
        mapa
        while True:
            os. system ("cls")
            print (" Nivel ",eleccion)
            print ("¡A jugar!")
            print ("---------")
            self.imprimir_mapa()
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
    pop.imprimir_mapa()
    pop.jugar()

elif eleccion == "2":
    mapa = pop.crear_mapa2()
    pop.imprimir_mapa()
    pop.jugar()

elif eleccion == "3":
    mapa = pop.crear_mapa3()
    pop.imprimir_mapa()
    pop.jugar()

 