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
    def mapa1 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,2,2,3,2,2,2,2,2],
                [2,2,2,4,2,2,2,2,2],
                [2,2,2,1,4,1,3,2,2],
                [2,3,4,1,0,2,2,2,2],
                [2,2,2,2,1,2,2,2,2],
                [2,2,2,2,3,2,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

    def mapa2 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,4,4,4,2,2,2,2,2],
                [2,4,1,0,2,2,2,2,2],
                [2,4,1,1,2,2,2,3,2],
                [2,2,2,4,2,2,2,3,2],
                [2,2,2,4,4,4,4,3,2],
                [2,2,4,4,4,2,4,4,2],
                [2,2,4,4,4,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

    def mapa3 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,2,4,4,2,2,2,2,2],
                [2,4,0,1,2,2,2,2,2],
                [2,2,1,4,2,2,2,2,2],
                [2,2,4,1,4,2,2,2,2],
                [2,3,1,4,4,2,2,2,2],
                [2,3,3,5,3,2,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

    def mapa4 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,2,0,4,2,2,2,2,2],
                [2,2,4,1,4,4,2,2,2],
                [2,2,2,4,2,4,2,2,2],
                [2,3,2,4,2,4,4,2,2],
                [2,3,1,4,4,2,4,2,2],
                [2,3,4,4,4,1,4,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

    def mapa5 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,2,2,4,4,4,4,2,2],
                [2,2,2,1,1,1,4,2,2],
                [2,0,4,1,3,3,4,2,2],
                [2,4,1,3,3,3,2,2,2],
                [2,2,2,2,4,4,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

    def mapa6 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,2,2,4,4,0,2,2,2],
                [2,4,4,1,3,4,2,2,2],
                [2,4,4,3,1,3,4,2,2],
                [2,2,2,4,5,1,4,2,2],
                [2,2,2,4,4,4,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

    def mapa7 (self):
        return [[2,2,2,2,2,2,2,2,2],
                [2,2,2,3,3,2,2,2,2],
                [2,2,2,4,3,2,2,2,2],
                [2,2,4,4,1,3,2,2,2],
                [2,2,4,1,4,4,2,2,2],
                [2,4,4,2,1,1,4,2,2],
                [2,4,4,0,4,4,4,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]
    
    #Impresion de mapas
    def print_map (self):
        smapa = ""
        for position_row in range(9):
            for position_col in range(9):
                smapa += str(object.mapa1 ()[position_row][position_col])
            print (smapa)
            smapa = ""
        tem_row = position_row
        tem_col = position_col

    #Movimientos
    def movimiento_derecha (self):
        position_col = position_col+1
    
    def movimiento_izquierda (self):
        position_col = position_col-1

    def movimiento_arriba (self):
        position_row = position_row-1

    def movimiento_abajo (self):
        position_row = position_row+1


object = Sokoban()
print("¡Bienvenido a mi juego de sokoban!")
print("Escoja un nivel: ")
print("[1] Nivel 1")
print("[2] Nivel 2")
print("[3] Nivel 3")
print("[4] Nivel 4")
print("[5] Nivel 5")
print("[6] Nivel 6")
print("[7] Nivel 7")
eleccion=int(input("Escoja un nivel: \n"))

#Opcion1
if eleccion == 1:
    os.system('cls')
    print ("Nivel 1")
    print ("¡A jugar!")
    print ("---------")
    print (object.print_map())
    object.mapa1()[4][4]=0
    position_row = 4
    position_col = 4
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
            object.movimiento_arriba()
            object.mapa1()[tem_col][tem_row]=4
            object.mapa1()[position_col][position_row]=0
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
        

smapa = ""
for position_row in range(9):
    for position_col in range(9):
        smapa += str(mapa[position_row][position_col])
    print (smapa)
    smapa = ""
print ('-----')
mapa[1][3]=0
position_row = 1
position_col = 3
while True:
    smapa = ""
    for position_row in range(5):
        for position_col in range(5):
            smapa += str(mapa[position_row][position_col])
        print (smapa)
        smapa = ""
    print ('-----')
    tem_col = position_col
    tem_row = position_row
    move = input('a-left, d-rigth, w-up, s-down \n')
    if move == 'd' and mapa[position_col+1]!=2:
        position_col = position_col+1
    elif move == 'a' and mapa[position_col-1]!=2:
        position_col = position_col-1
    elif move == 's' and mapa[position_row+1]!=2:
        position_row = position_row+1
    elif move == 'w' and mapa[position_row-1]!=2:
        position_row = position_row-1
    mapa[tem_col][tem_row]=4
    mapa[position_row][position_col]=0
#a-left position_col = position_col-1
#d-rigth position_col = position_col+1
#w-up position_row = position_row-1
#s-down position_row = position_row+1
