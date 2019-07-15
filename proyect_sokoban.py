# TODO Cambiar los iconos del juego
# TODO Realizar el juego con clases
'''
0.- Personaje
1.- Caja
2.- Paredes
3.- Metas
4.- Pasillo
5.- Caja/meta
6.- Personaje/meta
'''

class sokoban:
    #Variables generales
    def __init__ (self):
        pass
    #Mapas
    def mapa1 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,3,4,1,0,2,2,2,2],
                 [2,2,2,2,1,2,2,2,2],
                 [2,2,2,2,3,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]:

    def mapa2 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

    def mapa3 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

    def mapa4 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

    def mapa5 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]

    def mapa6 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]:

    def mapa7 = [[2,2,2,2,2,2,2,2,2],
                 [2,2,2,3,2,2,2,2,2],
                 [2,2,2,4,2,2,2,2,2],
                 [2,2,2,1,4,1,3,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2,2,2]]:

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
