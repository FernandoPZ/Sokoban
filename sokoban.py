'''
0.- Personaje
1.- Caja
2.- Paredes
3.- Metas
4.- Pasillo
5.- Caja/meta
'''
mapa = [2,4,4,4,0,4,4,1,3,2]
print (mapa)
position_x=4
while True:
    print (mapa)
    tem_x = position_x
    move = input('a-left, d-rigth \n')
    if move == 'd' and mapa[position_x+1]!=2:
        position_x = position_x+1
    elif move == 'a' and mapa[position_x-1]!=2:
        position_x = position_x-1
    mapa[tem_x]=4
    mapa[position_x]=0
