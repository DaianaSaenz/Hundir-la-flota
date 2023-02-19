import random
import constants
import numpy as np


#Función que presenta el juego
def inicio_juego():
    print(constants.presentacion)
    print(constants.mensaje_bienvenida)
    print(constants.introduccion)


def jugador_ingresa_coordenada():
    #input de fila e imput de columnas 
    coordenadas_x= int(input("Introduce fila"))
    coordenadas_y= int(input("Introduce columna"))
    disparo_sobre_coordenadas(coordenadas_x, coordenadas_y, True)


def disparo_sobre_coordenadas(cordenadax, cordenaday, esJugador):

    if esJugador:
        print('Comprobar que no se ha efectuado disparo sobre misma posicion')
        print('Si es agua cambia turno, si no vuele el jugador a elegir cordenadas // TIENES QUE PINTAR X o -')
    else:
        print('Comprobar que no se ha efectuado disparo sobre misma posicion')
        print('Si es agua cambia turno, si no vuele la maquina a elegir cordenadas // TIENES QUE PINTAR X o -')

def fin_del_juego():
    #check numero x de tabla jugador a y b

    return False

    

def maquina_elige_coordenadas():
    coordenadas_x= random.randint(0,10)
    coordenadas_y= random.randint(0,10)
    disparo_sobre_coordenadas(coordenadas_x,coordenadas_y, False)
 



## PARTE CARLOS##
BARCOS = [2,2,2,3,3,4,1,1,1,1]
TABLERO1 = np.full((10,10), (" "))
TABLERO1_2 = np.full((10,10), (" "))
TABLERO2_1 = np.full((10,10), (" "))
TABLERO2_2 = np.full((10,10), (" "))
DICLETRASYNUMEROS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

def print_board(tabla):
    print("  A B C D E F G H I J")
    print("+-+-+-+-+-+-+-+-+-+")
    numero_de_filas = 1
    for fila in tabla:
        print("%d|%s|" % (numero_de_filas, "|".join(fila)))
        numero_de_filas += 1

def colocar_barcos(tabla):
    for tamaño in BARCOS:
        while True:
            if tabla is TABLERO2_1:
                orientacion, fila, columna = random.choice(["H", "V"]), random.randint(0, 9), random.randint(0, 9)
            else:
                print(" Coloca un barco de tamaño " + str(tamaño))
                fila, columna, orientacion = entrada_de_usuario(True)
                
            if check_ship_fit(tamaño, fila, columna, orientacion):
                if not ship_overlaps(tabla, fila, columna, orientacion, tamaño):
                    if orientacion == "H":
                        for i in range(columna, columna + tamaño):
                            tabla[fila][i] = "O"
                    else:
                        for i in range(fila, fila + tamaño):
                            tabla[i][columna] = "O"
                    print_board(TABLERO1)
                    break 

def check_ship_fit(SHIP_LENGTH, fila, columna, orientacion):
    if orientacion == "H":
        if columna + SHIP_LENGTH > 10:
            return False
        else:
            return True
    else:
        if fila + SHIP_LENGTH > 10:
            return False
        else:
            return True

def ship_overlaps(tabla, fila, columna, orientacion, tamaño):
    if orientacion == "H":
        for i in range(columna, columna + tamaño):
            if tabla[fila][i] == "O":
                return True
    else:
        for i in range(fila, fila + tamaño):
            if tabla[i][columna] == "O":
                return True
    return False


def entrada_de_usuario(colocar_barcos):
    if colocar_barcos:
        while True:
            try: 
                orientacion = input("Inserta coordenadas (H para horizontal, V para vertical): ").upper()
                if orientacion == "H" or orientacion == "V":
                    break
            except TypeError:
                print("Inserta una coordenada horizontal o vertical valida")
        while True:
            try: 
                fila = input("Inserta una coordenada en las filas (1-10):  ")
                if fila in '12345678910':
                    fila = int(fila) - 1
                    break
            except ValueError:
                print("Inserta una letra valida entre 1 y 10")
        while True:
            try: 
                columna = input("Inserta la colo¡umna del barco: ").upper()
                if columna in 'ABCDEFGHIJ':
                    columna = DICLETRASYNUMEROS[columna]
                    break
            except KeyError:
                print("Inserta una columna valida entre A y J")
        return fila, columna, orientacion
    else:
        while True:
            try: 
                fila = input("Inserta una fila entre la 1 y la 10: ")
                if fila in '12345678910':
                    fila = int(fila) - 1
                    break
            except ValueError:
                print("Inserta una letra valida entre la 1 y la 10")
        while True:
            try: 
                columna = input("Inserta una columna entre la A y la J: ").upper()
                if columna in 'ABCDEFGHij':
                    columna = DICLETRASYNUMEROS[columna]
                    break
            except KeyError:
                print("Inserta una columna valida entre la A y la J")
        return fila, columna     

def countadordedisparos(tabla):
    c = 0
    for fila in tabla:
        for columna in fila:
            if columna == "X":
                c += 1
    return c

def turn(tabla):
    if tabla == TABLERO1_2:
        fila, columna = entrada_de_usuario(TABLERO2_2)
        if tabla[fila][columna] == "-":
            turn(tabla)
        elif tabla[fila][columna] == "X":
            turn(tabla)
        elif TABLERO2_1[fila][columna] == "X":
            tabla[fila][columna] = "X"
        else:
            tabla[fila][columna] = "-"
    else:
        fila, columna = random.randint(0,7), random.randint(0,7)
        if tabla[fila][columna] == "-":
            turn(tabla)
        elif tabla[fila][columna] == "X":
            turn(tabla)
        elif TABLERO1[fila][columna] == "X":
            tabla[fila][columna] = "X"
        else:
            tabla[fila][columna] = "-"

""" colocar_barcos(TABLERO1)
print_board(TABLERO1)
print_board(TABLERO2_1)
colocar_barcos(TABLERO2_1) """
        
""" while True:
    while True:
        print("Adivina una posicion")
        print_board(TABLERO1_2)
        turn(TABLERO1_2)
        break
    if countadordedisparos(TABLERO2_2) == 17:
        print("Has ganado!")
        break   
    while True:
        turn(TABLERO2_2)
        break           
    print_board(TABLERO2_2)   
    if countadordedisparos(TABLERO2_2) == 17:
        print("La computadora ha ganado!")
        break """