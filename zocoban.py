'''
Autor: Fernando Pérez Suárez
Fecha de inicio: 13/07/2019
Fecha de finalizacion:
Nombre: proyect_sokoban
Versión: 10.0.0
'''

'''
0> chr(79): 79 = O .- Personaje
1> chr(78): 78 = N .- Caja
2> chr(35): 35 = # .- Paredes
3> chr(88): 88 = X .- Metas
4> chr(32): 32 = [] .- Pasillo
5> chr(77): 77 = M .- Caja/meta
6> chr(48): 48 = 0 .- Personaje/meta
7> chr()
'''

import os
import msvcrt
import time

os. system ("cls")
print("               Bienvenido a mi juego               ")
print("               -------SOKOBAN-------               ")
time.sleep(1)
print("          Hay que comenzar por algo facil          ")
time.sleep(1)
print("En total son 7 niveles, uno mas dificil que el otro")
time.sleep(1)
print("                   ¿Estas listo?                   ")
time.sleep(1)
print("")
print("")
eleccion = input("Pulsa la tecla [Enter] paa continuar")

#MAPAS
#primer mapa
mapa1 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(88),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(78),chr(32),chr(78),chr(88),chr(35),chr(35)],
        [chr(35),chr(88),chr(32),chr(78),chr(79),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(78),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(88),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]
#Segundo mapa      
mapa2 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(32),chr(32),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(78),chr(79),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(78),chr(78),chr(35),chr(35),chr(35),chr(88),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(35),chr(35),chr(35),chr(88),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(32),chr(32),chr(32),chr(88),chr(35)],
        [chr(35),chr(35),chr(32),chr(32),chr(32),chr(35),chr(32),chr(32),chr(35)],
        [chr(35),chr(35),chr(32),chr(32),chr(32),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]
#Tercer mapa
mapa3 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(32),chr(32),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(79),chr(78),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(78),chr(32),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(32),chr(78),chr(32),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(88),chr(78),chr(32),chr(32),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(88),chr(88),chr(77),chr(88),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]
#Cuarto mapa
mapa4 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(79),chr(32),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(32),chr(78),chr(32),chr(32),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(35),chr(32),chr(35),chr(35),chr(35)],
        [chr(35),chr(88),chr(35),chr(32),chr(35),chr(32),chr(32),chr(35),chr(35)],
        [chr(35),chr(88),chr(78),chr(32),chr(32),chr(35),chr(32),chr(35),chr(35)],
        [chr(35),chr(88),chr(32),chr(32),chr(32),chr(78),chr(32),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]
#Quinto mapa
mapa5 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(32),chr(32),chr(32),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(78),chr(78),chr(78),chr(32),chr(35),chr(35)],
        [chr(35),chr(79),chr(32),chr(78),chr(88),chr(88),chr(32),chr(35),chr(35)],
        [chr(35),chr(32),chr(78),chr(88),chr(88),chr(88),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(32),chr(32),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]
#Sexto mapa
mapa6 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(32),chr(79),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(32),chr(78),chr(88),chr(32),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(32),chr(88),chr(78),chr(88),chr(32),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(77),chr(78),chr(32),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(32),chr(32),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]
#Septimo mapa
mapa7 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(88),chr(88),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(32),chr(88),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(32),chr(32),chr(78),chr(88),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(32),chr(78),chr(32),chr(32),chr(35),chr(35),chr(35)],
        [chr(35),chr(32),chr(32),chr(32),chr(78),chr(78),chr(32),chr(35),chr(35)],
        [chr(35),chr(32),chr(32),chr(79),chr(32),chr(32),chr(32),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
        [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]

mapa = mapa1
eleccion = 0
while eleccion < 7:
    eleccion = eleccion + 1
    os.system("cls")
    #Buscador de personaje
    contador_col=0
    contador_row=0
    per_col=0
    per_row=0
    for search_col in mapa:
        for search_row in search_col:
            if search_row != chr(79) and search_row != chr(48):
                contador_row=contador_row+1
            else:
                per_col=contador_col
                per_row=contador_row
                break
        contador_col=contador_col+1
        contador_row=0
    #Jugada
    while True:
        os. system ("cls")
        print ("     Nivel",eleccion)
        print ("    ¡A jugar!     ")
        print ("-------------------")
        #Impresor de mapa
        position_col=0
        position_row=0
        smapa = ""
        for position_col in mapa:
            for position_row in position_col:
                smapa = smapa+" "+str(position_row)
            print (smapa)
            smapa = ""
        #Impresor de mapa
        print ("-------------------")
        print ("Movimientos:    [W]   ")
        print ("             [A][S][D]")
        print ("[W] = Arriba")
        print ("[S] = Abajo")
        print ("[A] = Izquierda")
        print ("[D] = Derecha")
        print ("[C] = Agarrar caja")
        print ("Lanzar Caja:    [8]   ")
        print ("             [4][2][6]")
        print ("[8] = Arriba")
        print ("[2] = Abajo")
        print ("[4] = Izquierda")
        print ("[6] = Derecha")
        move = msvcrt.getch()
        move1 = ord(move)
        move = chr(move1)
        #Movimientos basicos
        if move == "w":
            if mapa[per_col-1][per_row]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(78):
                print("No puedes empujar 2 cajas")
                time.sleep(1)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(78)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)      
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79) 
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col-2][per_row]=chr(78)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(78)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col-1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col-1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
        elif move == "s":
            if mapa[per_col+1][per_row]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(35):
                print("Hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(78):
                print("No puedes empujar chr(35) cajas")
                time.sleep(1)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(78)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col+2][per_row]=chr(78)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(78)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col+1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
        elif move == "a":
            if mapa[per_col][per_row-1]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(78):
                print("No puedes mover chr(35) cajas")
                time.sleep(1)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(78)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row-2]=chr(78)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(78)
                per_row=per_row-chr(78)
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row-1]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
        elif move == "d":
            if mapa[per_col][per_row+1]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(78):
                print("No puedes mover chr(35) cajas")
                time.sleep(1)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(78)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row+2]=chr(78)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(78)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row+1]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
        elif move == "r":
            print("Ooooh, conoces el truco, eh?")
            time.sleep(2.5)
            print("")
            time.sleep(0.5)
            print("Tramposo...")
            time.sleep(0.5)
            break
        else:
            print ("Oprimiste la tecla equivocada")
            time.sleep(1)
        #Lanzamiento
        if move == "8":
            if mapa[per_col-1][per_row]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(78):
                print("No puedes empujar 2 cajas")
                time.sleep(1)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(78)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)      
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79) 
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col-1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col-2][per_row]=chr(78)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col-1][per_row]==chr(78) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col-2][per_row]=chr(77)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col-1][per_row]==chr(77) and mapa[per_col-2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col-2][per_row]=chr(78)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col-1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col-1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col-1
                mapa[per_col][per_row]=chr(48)
        elif move == "s":
            if mapa[per_col+1][per_row]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(35):
                print("Hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(78):
                print("No puedes empujar chr(35) cajas")
                time.sleep(1)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(78)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col+1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col+2][per_row]=chr(78)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(78) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col+2][per_row]=chr(77)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col+1][per_row]==chr(77) and mapa[per_col+2][per_row]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col+2][per_row]=chr(78)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col+1][per_row]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col+1][per_row]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_col=per_col+1
                mapa[per_col][per_row]=chr(48)
        elif move == "a":
            if mapa[per_col][per_row-1]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(78):
                print("No puedes mover chr(35) cajas")
                time.sleep(1)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(78)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row-1]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row-2]=chr(78)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(78) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row-2]=chr(77)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row-1]==chr(77) and mapa[per_col][per_row-2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row-2]=chr(78)
                per_row=per_row-chr(78)
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row-1]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row-1]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row-1
                mapa[per_col][per_row]=chr(48)
        elif move == "d":
            if mapa[per_col][per_row+1]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(35):
                print("hay una pared, no puedes pasar")
                time.sleep(1)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(78):
                print("No puedes mover chr(35) cajas")
                time.sleep(1)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(35):
                print ("Obstaculo enfrente")
                time.sleep(1)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(78)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(88):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row]==chr(48) and mapa[per_col][per_row+1]==chr(32):
                mapa[per_col][per_row]=chr(88)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(32):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row+2]=chr(78)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(78) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(88):
                mapa[per_col][per_row]=chr(32)
                mapa[per_col][per_row+2]=chr(77)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row+1]==chr(77) and mapa[per_col][per_row+2]==chr(32):
                mapa[per_col][per_row]=chr(88)
                mapa[per_col][per_row+2]=chr(78)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
            elif mapa[per_col][per_row+1]==chr(32):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(79)
            elif mapa[per_col][per_row+1]==chr(88):
                mapa[per_col][per_row]=chr(32)
                per_row=per_row+1
                mapa[per_col][per_row]=chr(48)
        elif move == "r":
            print("Ooooh, conoces el truco, eh?")
            time.sleep(2.5)
            print("")
            time.sleep(0.5)
            print("Tramposo...")
            time.sleep(0.5)
            break
        else:
            print ("Oprimiste la tecla equivocada")
            time.sleep(1)
        if mapa[0].count(chr(78))==0 and mapa[1].count(chr(78))==0 and mapa[2].count(chr(78))==0 and mapa[3].count(chr(78))==0 and mapa[4].count(chr(78))==0 and mapa[0].count(chr(78))==0 and mapa[5].count(chr(78))==0 and mapa[6].count(chr(78))==0 and mapa[7].count(chr(78))==0 and mapa[8].count(chr(78))==0:
            os. system ("cls")
            print ("     Nivel",eleccion)
            print ("    ¡A jugar!     ")
            print ("-------------------")
            position_col=0
            position_row=0
            smapa = ""
            for position_col in mapa:
                for position_row in position_col:
                    smapa = smapa+" "+str(position_row)
                print (smapa)
                smapa = ""
            print ("-------------------")
            print (" ¡¡¡FELICIDADES!!! ")
            print ("     Nivel",eleccion)
            print ("   Completado    ")
            time.sleep(2)
            break

    os. system ("cls")
    if eleccion == 1:
        mapa = mapa2
    elif eleccion == 2:
        mapa = mapa3
    elif eleccion == 3:
        mapa = mapa4
    elif eleccion == 4:
        mapa = mapa5
    elif eleccion == 5:
        mapa = mapa6
    elif eleccion == 6:
        mapa = mapa7
    elif eleccion == 7:
        print ("Niveles completados")
        print ("-------------------")
        print ("     GAME OVER     ")
        print ("-------------------")
        time .sleep(2)
        print ("Gracias por jugar")
        time.sleep(1)
        break
