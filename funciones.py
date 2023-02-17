import random
import constants

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
 
