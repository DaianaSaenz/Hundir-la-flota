import funciones as funciones_juego
import numpy as np
import clases as clases

def juego():
    turno_jugador=True
    quedan_barcos_sin_hundir_del_jugador= True
    quedan_barcos_sin_hundir_maquina= True
    tablero_jugador= clases.Tablero(np.full((10,10), (" ")))
    tablero_maquina= clases.Tablero(np.full((10,10), (" ")))
  
    # 1. Mostrar reglas Juego
    funciones_juego.inicio_juego()
 
    # 2. Colocar barcos
    tablero_maquina.posicionar_barcos_aleatoriamente()
    tablero_jugador.ubicar_barcos_jugador_manual()

    while quedan_barcos_sin_hundir_del_jugador and quedan_barcos_sin_hundir_maquina :
        disparo_sin_efectuar=True
        while disparo_sin_efectuar:
            eleccion_jugador=int(input(" Introduzca 1 si quieres consultar pantalla de disparo, pulse 2 para dispara cordenadas y 3 para consultar el tablero propio: "))
            if eleccion_jugador== 1:
                tablero_maquina.mostrar_tablero_disparos_recibidos()
            if eleccion_jugador== 3:
                tablero_jugador.mostrar_tablero()
            else:
                disparo_sin_efectuar = tablero_maquina.recibir_disparo()
                disparo_sin_efectuar= False

        tablero_jugador.recibir_disparo_aleatorio()
        quedan_barcos_sin_hundir_maquina = not tablero_maquina.comprobar_todos_barcos_hundidos()
        quedan_barcos_sin_hundir_del_jugador= not tablero_jugador.comprobar_todos_barcos_hundidos()

juego()


