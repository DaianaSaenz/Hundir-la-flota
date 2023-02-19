import funciones as funciones_juego
import random
import numpy as np
import clases

def juego():
    turno_jugador=True
    tablero_jugador= clases.Tablero()
    tablero_maquina=clases.Tablero()
  
    # 1. Mostrar reglas Juego
     # funciones_juego.inicio_juego()
 
    # 2. Colocar barcos
    tablero_jugador.posicionar_barcos()
    tablero_maquina.posicionar_barcos()
    # FUNCION WHILE QUE EJECUTE ACCION DE DISPARO HASTA QUE UNO DE LOS OCNTADORES LLEGUE A LOS 20 PUNTOS
    
    #while not funciones_juego.fin_del_juego() :
   # funciones_juego.maquina_elige_coordenadas()

    tablero_jugador= clases.Tablero()
    tablero_jugador.posicionar_barcos()
    print(tablero_jugador.mostrar_tablero())

    # 3. Turnos disparar, ALTERNAN TURNOS si disparo erroneo y comprobar si todos los barcos esyan hundidos
    # 5. Si hay ganador condicion while false entonces fin juego



juego()

""" if __name__ == "__main__":  """


