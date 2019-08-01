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
        
mapa2 = [[chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)],
         [chr(35),chr(32),chr(32),chr(32),chr(35),chr(35),chr(35),chr(35),chr(35)],
         [chr(35),chr(32),chr(78),chr(79),chr(35),chr(35),chr(35),chr(35),chr(35)],
         [chr(35),chr(32),chr(78),chr(78),chr(35),chr(35),chr(35),chr(88),chr(35)],
         [chr(35),chr(35),chr(35),chr(32),chr(35),chr(35),chr(35),chr(88),chr(35)],
         [chr(35),chr(35),chr(35),chr(32),chr(32),chr(32),chr(32),chr(88),chr(35)],
         [chr(35),chr(35),chr(32),chr(32),chr(32),chr(35),chr(32),chr(32),chr(35)],
         [chr(35),chr(35),chr(32),chr(32),chr(32),chr(35),chr(35),chr(35),chr(35)],
         [chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35),chr(35)]]

