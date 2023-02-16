import random
def inicio_juego():
    #dara acceso a que se imprima el print de bienvenida
    #Importar constantes
    print(mensaje_bienvenida)
    print(introduccion)

def jugador_ingresa_coordenada():
    #input de fila e imput de columnas 
    coordenadas_x= int(input("Introduce fila"))
    coordenadas_y= int(input("Introduce columna"))
    buscar_coordenadas(coordenadas_x, coordenadas_y, 'jugador')


def buscar_coordenadas(cordenadax, cordenaday, jugador):
    #IMPORTA CONSTANTES DE TABLERO
    #Si jugador es persona comprobar tablero posiciones maquina sino viceversa
    tablero[coordenada_disparo]
    #checkear en tabla de disparos si el tiro esta repetido si esta repetido llamar a la funcion jugador ingresa coordenada o maquina
    #si disparo es efectivo/agua pinto en tabla disparos de jugador/maquina el resultado

def fin_del_juego():
    #esto retornara un ganador
    if barcos_jugador == 0 or barcos_maquina ==0:
        return True

def maquina_selecciona_coordenada_aleatoria():
    coordenadas_x= random.randint(0,10)
    coordenadas_y= random.randint(0,10)
    buscar_coordenadas(coordenadas_x,coordenadas_y, 'maquina')
 
