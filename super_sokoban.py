'''
Autor: Fernando Pérez Suárez
Fecha de inicio: 13/07/2019
Fecha de finalizacion: 
Nombre: proyect_sokoban
Versión: 8.0.0
'''

'''
0> chr(79): 79 = O .- Personaje
1> chr(78): 78 = N .- Caja
2> chr(35): 35 = # .- Paredes
3> chr(88): 88 = X .- Metas
4> chr(32): 32 = [] .- Pasillo
5> chr(77): 77 = M .- Caja/meta
6> chr(48): 48 = 0 .- Personaje/meta
'''

import os
import msvcrt
import time

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

#Menu del juego
os.system("cls")
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
    mapa = mapa1
#Opcion2
elif eleccion == "2":
    mapa = mapa2
#Opcion3
elif eleccion == "3":
    mapa = mapa3
#Opcion4
elif eleccion == "4":
    mapa = mapa4
#Opcion5
elif eleccion == "5":
    mapa = mapa5
#Opcion6
elif eleccion == "6":
    mapa = mapa6
#opcion7
elif eleccion == "7":
    mapa = mapa7
#error
else:
    print ("ERROR!!!")
    print ("Seleccione una opcion valida")
    time.sleep(1)

#Impresor de mapa
def imprimir_mapa ():
    position_col=0
    position_row=0
    smapa = ""
    for position_col in mapa:
        for position_row in position_col:
            smapa = smapa+" "+str(position_row)
        print (smapa)
        smapa = ""

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

while True:
    os. system ("cls")
    print (" Nivel ",eleccion)
    print ("¡A jugar!")
    print ("---------")
    imprimir_mapa()
    print ("---------")
    print ("Movimientos:    [W]   ")
    print ("             [A][S][D]")
    print ("[W] = Arriba")
    print ("[S] = Abajo")
    print ("[A] = Izquierda")
    print ("[D] = Derecha")
    move = msvcrt.getch()
    move1 = ord(move)
    move = chr(move1)
                
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
            per_row=per_row-1
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
        break

    else:
        print ("Oprimiste la tecla equivocada")
        time.sleep(1)
                            
    if mapa[0].count(chr(78))==0 and mapa[1].count(chr(78))==0 and mapa[2].count(chr(78))==0 and mapa[3].count(chr(78))==0 and mapa[4].count(chr(78))==0 and mapa[0].count(chr(78))==0 and mapa[5].count(chr(78))==0 and mapa[6].count(chr(78))==0 and mapa[7].count(chr(78))==0 and mapa[8].count(chr(78))==0:
        os. system ("cls")
        print (" Nivel ",eleccion)
        print ("¡A jugar!")
        print ("---------")
        imprimir_mapa()
        print ("---------")
        print ("Movimientos:    [W]   ")
        print ("             [A][S][D]")
        print ("[W] = Arriba")
        print ("[S] = Abajo")
        print ("[A] = Izquierda")
        print ("[D] = Derecha")
        print ("¡¡¡FELICIDADES!!!")
        print ("Nivel",eleccion)
        print ("Completado")
        time.sleep(2)

        os. system ("cls")
        if eleccion == "1":
            mapa = mapa2
            jugar()
        if eleccion == "2":
            mapa == mapa3
            jugar()
        elif eleccion == "3":
            mapa = mapa4
            jugar()
        elif eleccion == "4":
            mapa = mapa5
            jugar()
        elif eleccion == "5":
            mapa = mapa6
            jugar()
        elif eleccion == "6":
            mapa = mapa7
            jugar()
        elif eleccion == "7":
            print ("Niveles completados")
            print ("-------------------")
            print ("     GAME OVER     ")
            time .sleep(0.5)
            print(". . .")
            time .sleep(0.5)
            print(". . .")
            time .sleep(0.5)
            print(". . .")
            time .sleep(0.5)
            print ("Gracias por jugar")
            time.sleep(1)
            break
