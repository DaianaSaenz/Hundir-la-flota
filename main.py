import funciones as funciones_juego
import random
 

def juego():
    # 1. Mostrar reglas Juego
    turno_jugador=True
    funciones_juego.inicio_juego()
    # 2. Pintar tablero / Colocar barcos
    # FUNCION WHILE QUE EJECUTE ACCION DE DISPARO HASTA QUE UNO DE LOS OCNTADORES LLEGUE A LOS 20 PUNTOS
    
    #while not funciones_juego.fin_del_juego() :
    funciones_juego.maquina_elige_coordenadas()

    print() 


    # 3. Turnos disparar, ALTERNAN TURNOS si disparo erroneo y comprobar si todos los barcos esyan hundidos
    # 5. Si hay ganador condicion while false entonces fin juego



juego()


""" if __name__ == "__main__": """
