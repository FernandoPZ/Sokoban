'''
Autor: Fernando Pérez Suárez
Fecha de inicio: 13/07/2019
Fecha de finalizacion: 
Nombre: proyect_sokoban
Versión: 7.0.0
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

    def __init__ (self):
        pass

    #Primer nivel
    def nivel1 (self):
        #Mapa
        mapa = [[2,2,2,2,2,2,2,2,2],
                [2,2,2,3,2,2,2,2,2],
                [2,2,2,4,2,2,2,2,2],
                [2,2,2,1,4,1,3,2,2],
                [2,3,4,1,0,2,2,2,2],
                [2,2,2,2,1,2,2,2,2],
                [2,2,2,2,3,2,2,2,2],
                [2,2,2,2,2,2,2,2,2],
                [2,2,2,2,2,2,2,2,2]]

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

        imprimir_mapa()

        #Buscador de personaje
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

        #Instrucciones
        def instrucciones ():
            print ("Movimientos:    [W]   ")
            print ("             [A][S][D]")
            print ("[W] = Arriba")
            print ("[S] = Abajo")
            print ("[A] = Izquierda")
            print ("[D] = Derecha")

        while True:
                os. system ("cls")
                print (" Nivel 1")
                print ("¡A jugar!")
                print ("---------")
                imprimir_mapa()
                print ("---------")
                instrucciones()
                move = input("")
                if move == "w":
                    if mapa[per_col-1][per_row]==2:
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
                        print (imprimir_mapa())   

                    elif mapa[per_col-1][per_row]==3:
                        mapa[per_col][per_row]=4
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==4:
                        mapa[per_col][per_row]=3
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==3:
                        mapa[per_col][per_row]=3
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "s":
                    if mapa[per_col+1][per_row]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==2:
                        print("Hay una pared, no puedes pasar")

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==1:
                        print("No puedes empujar 2 cajas")

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col+1][per_row]==4:
                        mapa[per_col][per_row]=4
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa()) 

                    elif mapa[per_col+1][per_row]==3:
                        mapa[per_col][per_row]=4
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==3:
                        mapa[per_col][per_row]=3
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==4:
                        mapa[per_col][per_row]=3
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())   

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "a":
                    if mapa[per_col][per_row-1]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==1:
                        print("No puedes mover 2 cajas")

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col][per_row-1]==4:
                        mapa[per_col][per_row]=4
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())   

                    elif mapa[per_col][per_row-1]==3:
                        mapa[per_col][per_row]=4
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==3:
                        mapa[per_col][per_row]=3
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==4:
                        mapa[per_col][per_row]=3
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())  

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())      

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                elif move == "d":
                    if mapa[per_col][per_row+1]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==2:
                        print("Hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==1:
                        print("No puedes empujar 2 cajas")

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col][per_row+1]==4:
                        mapa[per_col][per_row]=4
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())  

                    elif mapa[per_col][per_row+1]==3:
                        mapa[per_col][per_row]=4
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==4:
                        mapa[per_col][per_row]=3
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==3:
                        mapa[per_col][per_row]=3
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "r":
                    break

                else:
                    print ("Oprimiste la tecla equivocada")

                #Finalizador
                if mapa[0].count(1)==0 and mapa[1].count(1)==0 and mapa[2].count(1)==0 and mapa[3].count(1)==0 and mapa[4].count(1)==0:
                    print("¡¡¡Felicidades!!!")
                    print("¡¡¡Terminaste el nivel 1!!!")

    #Segundo nivel
    def nivel2 (self):
        #Mapa
        mapa = [[2,2,2,2,2,2,2,2,2],
                 [2,4,4,4,2,2,2,2,2],
                 [2,4,1,0,2,2,2,2,2],
                 [2,4,1,1,2,2,2,3,2],
                 [2,2,2,4,2,2,2,3,2],
                 [2,2,2,4,4,4,4,3,2],
                 [2,2,4,4,4,2,4,4,2],
                 [2,2,4,4,4,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

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

        imprimir_mapa()

        #Buscador de personaje
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

        #Instrucciones
        def instrucciones ():
            print ("Movimientos:    [W]   ")
            print ("             [A][S][D]")
            print ("[W] = Arriba")
            print ("[S] = Abajo")
            print ("[A] = Izquierda")
            print ("[D] = Derecha")

        while True:
                os. system ("cls")
                print (" Nivel 1")
                print ("¡A jugar!")
                print ("---------")
                imprimir_mapa()
                print ("---------")
                instrucciones()
                move = input("")
                if move == "w":
                    if mapa[per_col-1][per_row]==2:
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
                        print (imprimir_mapa())   

                    elif mapa[per_col-1][per_row]==3:
                        mapa[per_col][per_row]=4
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==4:
                        mapa[per_col][per_row]=3
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==3:
                        mapa[per_col][per_row]=3
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "s":
                    if mapa[per_col+1][per_row]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==2:
                        print("Hay una pared, no puedes pasar")

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==1:
                        print("No puedes empujar 2 cajas")

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col+1][per_row]==4:
                        mapa[per_col][per_row]=4
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa()) 

                    elif mapa[per_col+1][per_row]==3:
                        mapa[per_col][per_row]=4
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==3:
                        mapa[per_col][per_row]=3
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==4:
                        mapa[per_col][per_row]=3
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())   

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "a":
                    if mapa[per_col][per_row-1]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==1:
                        print("No puedes mover 2 cajas")

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col][per_row-1]==4:
                        mapa[per_col][per_row]=4
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())   

                    elif mapa[per_col][per_row-1]==3:
                        mapa[per_col][per_row]=4
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==3:
                        mapa[per_col][per_row]=3
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==4:
                        mapa[per_col][per_row]=3
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())  

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())      

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                elif move == "d":
                    if mapa[per_col][per_row+1]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==2:
                        print("Hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==1:
                        print("No puedes empujar 2 cajas")

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col][per_row+1]==4:
                        mapa[per_col][per_row]=4
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())  

                    elif mapa[per_col][per_row+1]==3:
                        mapa[per_col][per_row]=4
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==4:
                        mapa[per_col][per_row]=3
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==3:
                        mapa[per_col][per_row]=3
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "r":
                    break

                else:
                    print ("Oprimiste la tecla equivocada")

                #Finalizador
                if mapa[0].count(1)==0 and mapa[1].count(1)==0 and mapa[2].count(1)==0 and mapa[3].count(1)==0 and mapa[4].count(1)==0:
                    print("¡¡¡Felicidades!!!")
                    print("¡¡¡Terminaste el nivel 1!!!")

    #Tercer nivel
    def nivel3 (self):
        #Mapa
        mapa = [[2,2,2,2,2,2,2,2,2],
                 [2,2,4,4,2,2,2,2,2],
                 [2,4,0,1,2,2,2,2,2],
                 [2,2,1,4,2,2,2,2,2],
                 [2,2,4,1,4,2,2,2,2],
                 [2,3,1,4,4,2,2,2,2],
                 [2,3,3,5,3,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

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

        imprimir_mapa()

        #Buscador de personaje
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

        #Instrucciones
        def instrucciones ():
            print ("Movimientos:    [W]   ")
            print ("             [A][S][D]")
            print ("[W] = Arriba")
            print ("[S] = Abajo")
            print ("[A] = Izquierda")
            print ("[D] = Derecha")

        while True:
                os. system ("cls")
                print (" Nivel 1")
                print ("¡A jugar!")
                print ("---------")
                imprimir_mapa()
                print ("---------")
                instrucciones()
                move = input("")
                if move == "w":
                    if mapa[per_col-1][per_row]==2:
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
                        print (imprimir_mapa())   

                    elif mapa[per_col-1][per_row]==3:
                        mapa[per_col][per_row]=4
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==4:
                        mapa[per_col][per_row]=3
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==3:
                        mapa[per_col][per_row]=3
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=1
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==1 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col-1][per_row]==5 and mapa[per_col-2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col-2][per_row]=5
                        per_col=per_col-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "s":
                    if mapa[per_col+1][per_row]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==2:
                        print("Hay una pared, no puedes pasar")

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==1:
                        print("No puedes empujar 2 cajas")

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col+1][per_row]==4:
                        mapa[per_col][per_row]=4
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa()) 

                    elif mapa[per_col+1][per_row]==3:
                        mapa[per_col][per_row]=4
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==3:
                        mapa[per_col][per_row]=3
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==4:
                        mapa[per_col][per_row]=3
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=1
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())   

                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==1 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col+1][per_row]==5 and mapa[per_col+2][per_row]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col+2][per_row]=5
                        per_col=per_col+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "a":
                    if mapa[per_col][per_row-1]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==1:
                        print("No puedes mover 2 cajas")

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col][per_row-1]==4:
                        mapa[per_col][per_row]=4
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())   

                    elif mapa[per_col][per_row-1]==3:
                        mapa[per_col][per_row]=4
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==3:
                        mapa[per_col][per_row]=3
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==4:
                        mapa[per_col][per_row]=3
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==5 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())  

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=1
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())      

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row-1]==1 and mapa[per_col][per_row-2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row-2]=5
                        per_row=per_row-1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                elif move == "d":
                    if mapa[per_col][per_row+1]==2:
                        print("hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==2:
                        print("Hay una pared, no puedes pasar")

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==1:
                        print("No puedes empujar 2 cajas")

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==2:
                        print ("Obstaculo enfrente")

                    elif mapa[per_col][per_row+1]==4:
                        mapa[per_col][per_row]=4
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())  

                    elif mapa[per_col][per_row+1]==3:
                        mapa[per_col][per_row]=4
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==4:
                        mapa[per_col][per_row]=3
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())
                
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==3:
                        mapa[per_col][per_row]=3
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=4
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==4:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=1
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     

                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==1 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=0
                        print (imprimir_mapa())     
                    
                    elif mapa[per_col][per_row]==6 and mapa[per_col][per_row+1]==5 and mapa[per_col][per_row+2]==3:
                        mapa[per_col][per_row]=3
                        mapa[per_col][per_row+2]=5
                        per_row=per_row+1
                        mapa[per_col][per_row]=6
                        print (imprimir_mapa())

                elif move == "r":
                    break

                else:
                    print ("Oprimiste la tecla equivocada")

                #Finalizador
                if mapa[0].count(1)==0 and mapa[1].count(1)==0 and mapa[2].count(1)==0 and mapa[3].count(1)==0 and mapa[4].count(1)==0:
                    print("¡¡¡Felicidades!!!")
                    print("¡¡¡Terminaste el nivel 1!!!")

pop = Sokoban()
print("¡Bienvenido a mi juego de sokoban!")
print("--NIVELES--")
print("[1] Nivel 1")
print("[2] Nivel 2")
print("[3] Nivel 3")
eleccion = input ("Escoja un nivel: \n")

#Opcion1
if eleccion == "1":
    pop.nivel1()
#Opcion2
elif eleccion == "2":
    pop.nivel2()
#Opcion3
elif eleccion == "3":
    pop.nivel3()
