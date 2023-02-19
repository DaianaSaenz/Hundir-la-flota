import numpy as np
import random 
from functools import reduce

class Tablero:
    dimensiones = np.full((10,10), (" "))
    barcos = [2,2,2,3,3,4,1,1,1,1]
    #calculo de esloras restantes
    total_esloras= reduce(lambda x,y: x+y, barcos)
    orientacion=['N', 'S', 'E','O']

    # Metodo que muestre al rival los aciertos y disparos sobre agua
    # Metodo que dibuje disparos sobre tablero
    def recibir_disparo(self,coordX, coordY):
        if self.dimensiones[coordX,coordY]=='O':
            self.dimensiones[coordX,coordY]='X'
        elif self.dimensiones[coordX,coordY]=='X':
            print('Disparo repetido. Pruebe de nuevo')
        else:
            self.dimensiones[coordX,coordY]='-'

    # Muestra estado actual del tablero del jugador
    def mostrar_tablero(self):
        return self.dimensiones
    
    # muestra al jugador rival la tabla con los disparos efectuados
    def mostrar_tablero_disparos_recibidos(self):
        tablero_disparos = np.where(self.dimensiones=='O'," ", self.dimensiones)
        return tablero_disparos
        
    def comprobar_todos_barcos_hundidos(self):
        numero_de_esloras_hundidas= np.count_nonzero(self.dimensiones=='X')
        if numero_de_esloras_hundidas==20:
            True
        else:
            False


    
    # Posiciona aleatoriamente los barcos
    def posicionar_barcos(self):
        # itero sobre la listas de barcos
        for num_esloras in self.barcos:
            puedo_colocar_barco=False
            barco_no_colocado=True

            # Mientras el barco no se haya colocado se intentará posicionar sobre coordenadas aleatorias
            while barco_no_colocado:
                coordenadas_aleatorias_x = random.randint(0,9)
                coordenadas_aleatorias_y = random.randint(0,9)
                codernadas_esloras =[(coordenadas_aleatorias_x, coordenadas_aleatorias_y)] 
                contador_esloras_restantes= num_esloras-1
                # si la primera coordinada esta ocupada busco de nuevo otras coordenadas
                if self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y ] == "O":
                    continue
                # si el barco tiene una sola eslora puedo colocar el barco
                if num_esloras == 1:
                    puedo_colocar_barco=True
                else:
                    #Coloco el barco hacia una direccion aleatoria
                    direccion= self.orientacion[random.randint(0,3)]
                    #Trata de colocar resto de esloras hacia una direccion
                    while contador_esloras_restantes !=0:
                        if direccion=='O' and coordenadas_aleatorias_x-1 >= 0 and self.dimensiones[ coordenadas_aleatorias_x-1, coordenadas_aleatorias_y ] == " " :
                            codernadas_esloras.append( (coordenadas_aleatorias_x - 1, coordenadas_aleatorias_y) )
                            coordenadas_aleatorias_x = coordenadas_aleatorias_x - 1

                        elif direccion=='S' and  coordenadas_aleatorias_y-1 >= 0 and self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y - 1 ] == " ":
                            codernadas_esloras.append( (coordenadas_aleatorias_x, coordenadas_aleatorias_y -1 ) )
                            coordenadas_aleatorias_y = coordenadas_aleatorias_y - 1
                            
                        elif  direccion=='N' and  coordenadas_aleatorias_y + 1 <=9 and self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y + 1 ] == " ":
                            codernadas_esloras.append(( coordenadas_aleatorias_x, coordenadas_aleatorias_y +1) )
                            coordenadas_aleatorias_y = coordenadas_aleatorias_y + 1
                        
                        elif  direccion=='E' and  coordenadas_aleatorias_x+1 <=0 and self.dimensiones[ coordenadas_aleatorias_x+1, coordenadas_aleatorias_y] == " ":
                            codernadas_esloras.append((coordenadas_aleatorias_x+1, coordenadas_aleatorias_y) )
                            coordenadas_aleatorias_x = coordenadas_aleatorias_x + 1

                        contador_esloras_restantes= contador_esloras_restantes -1

                    puedo_colocar_barco = len(codernadas_esloras)==num_esloras 

                if puedo_colocar_barco:
                    barco_no_colocado=False
                    for x, y in codernadas_esloras:
                        self.dimensiones[x,y]="O"
        #print(self.dimensiones)
    