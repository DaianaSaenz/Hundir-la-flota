import numpy as np
import random 

class Tablero:
    dimensiones = []
    barcos = [4,3,3,2,2,2,1,1,1,1]
    orientacion=['N', 'S', 'E','O']

    def __init__(self, dimensiones):
        self.dimensiones= dimensiones

    # Metodo que muestre al rival los aciertos y disparos sobre agua
    # Metodo que dibuje disparos sobre tablero
    def recibir_disparo(self):
        disparo_sin_efectuar= True
        while disparo_sin_efectuar:
            coord_disparo_x=int(input(" Introduzca coordenada de disparo sobre el eje X de 0 a 9"))
            cood_disparo_y=int(input(" Introduzca coordenada de disparo sobre el eje Y de 0 a 9"))

            if self.dimensiones[coord_disparo_x,cood_disparo_y]=='O':
                self.dimensiones[coord_disparo_x,cood_disparo_y]='X'
            elif self.dimensiones[coord_disparo_x,cood_disparo_y]=='X':
                print('Disparo repetido. Pruebe de nuevo')
            else:
                self.dimensiones[coord_disparo_x,cood_disparo_y]='-'
                disparo_sin_efectuar= False


    # Muestra estado actual del tablero del jugador
    def mostrar_tablero(self):
        print( self.dimensiones)
    
    # muestra al jugador rival la tabla con los disparos efectuados
    def mostrar_tablero_disparos_recibidos(self):
        tablero_disparos = np.where(self.dimensiones=='O'," ", self.dimensiones)
        print(tablero_disparos) 

    #comprobar fin del juego
    def comprobar_todos_barcos_hundidos(self):
        numero_de_esloras_hundidas= np.count_nonzero(self.dimensiones=='X')
        if numero_de_esloras_hundidas==20:
            True
            print("fin del juego")
        else:
            False

    def recibir_disparo_aleatorio(self):
        disparo_no_correcto=True
        while disparo_no_correcto:      
            coordenadas_aleatorias_x = random.randint(0,9)
            coordenadas_aleatorias_y = random.randint(0,9)
            if self.dimensiones[coordenadas_aleatorias_x,coordenadas_aleatorias_y] == "O":
                self.dimensiones[coordenadas_aleatorias_x,coordenadas_aleatorias_y]="X"
            elif self.dimensiones[coordenadas_aleatorias_x,coordenadas_aleatorias_y] == "-":
                continue
            else:
                self.dimensiones[coordenadas_aleatorias_x,coordenadas_aleatorias_y] ="-"
                disparo_no_correcto=True
            
    
    # Posiciona aleatoriamente los barcos maquina
    def posicionar_barcos_aleatoriamente(self):
        # itero sobre la listas de barcos
        for num_esloras in self.barcos:
            puedo_colocar_barco=False
            barco_no_colocado=True

            # Mientras el barco no se haya colocado se intentará posicionar sobre coordenadas aleatorias
            while barco_no_colocado:
                coordenadas_aleatorias_x = random.randint(0,9)
                coordenadas_aleatorias_y = random.randint(0,9)
                codernadas_esloras =[(  coordenadas_aleatorias_x, coordenadas_aleatorias_y)] 
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
                            codernadas_esloras.append( (coordenadas_aleatorias_x - 1 , coordenadas_aleatorias_y) )
                            coordenadas_aleatorias_x = coordenadas_aleatorias_x - 1

                        elif direccion=='S' and  coordenadas_aleatorias_y-1 >= 0 and self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y - 1 ] == " ":
                            codernadas_esloras.append( (  coordenadas_aleatorias_x, coordenadas_aleatorias_y -1) )
                            coordenadas_aleatorias_y = coordenadas_aleatorias_y - 1
                            
                        elif  direccion=='N' and  coordenadas_aleatorias_y + 1 <=9 and self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y + 1 ] == " ":
                            codernadas_esloras.append(( coordenadas_aleatorias_x,  coordenadas_aleatorias_y +1 ) )
                            coordenadas_aleatorias_y = coordenadas_aleatorias_y + 1
                        
                        elif  direccion=='E' and  coordenadas_aleatorias_x+1 <=0 and self.dimensiones[ coordenadas_aleatorias_x+1, coordenadas_aleatorias_y] == " ":
                            codernadas_esloras.append((  coordenadas_aleatorias_x+1, coordenadas_aleatorias_y) )
                            coordenadas_aleatorias_x = coordenadas_aleatorias_x + 1

                        contador_esloras_restantes= contador_esloras_restantes -1

                    puedo_colocar_barco = len(codernadas_esloras)==num_esloras 

                if puedo_colocar_barco:
                    barco_no_colocado=False
                    for x,y in codernadas_esloras:
                        self.dimensiones[x,y]="O"
       
    

    def ubicar_barcos_jugador_manual(self):
        print(self.dimensiones)
        for esloras in self.barcos:
            barco_no_colocado= True
            colocar_barco_manual= False

            while barco_no_colocado:
                coordi_x= int(input("Ingrese un numero para elegir la fila del 0 al 9: "))
                coordi_y= int(input("Ingrese un numero para indicar el numero de columna del 0 al 9: "))
                if self.dimensiones[ coordi_x, coordi_y ] == "O":                    
                        print('La coordenada elegida ya contiene un barco, pruebe de nuevo')
                        continue

                lista_coordenadas_barco=[(coordi_x, coordi_y)]
                if esloras == 1:
                    colocar_barco_manual=True

                else:
                    orientacion_elegida= input("Elige con una sola letra una orientación: N, S, E, O : ")
                 
                    contador_esloras_restantes= esloras-1

                    while contador_esloras_restantes !=0:
                        if orientacion_elegida=='E' and  coordi_y+1 <=9 and self.dimensiones[ coordi_x, coordi_y+1 ] !='O':
                            lista_coordenadas_barco.append(( coordi_x, coordi_y+1))
                            coordi_y = coordi_y+1 
                            
                        
                        if orientacion_elegida=='O'and  coordi_y-1 >=0 and self.dimensiones[ coordi_x, coordi_y-1 ] !='O':
                            lista_coordenadas_barco.append(( coordi_x, coordi_y-1))
                            coordi_y = coordi_y-1 
                            
                        if orientacion_elegida=='S'and  coordi_x+1 <=9 and self.dimensiones[ coordi_x+1, coordi_y] !='O':
                            lista_coordenadas_barco.append(( coordi_x+1, coordi_y))
                            coordi_x = coordi_x+1
                            
                        if orientacion_elegida=='N'and  coordi_x-1 >=0 and self.dimensiones[ coordi_x-1, coordi_y ] !='O':
                            lista_coordenadas_barco.append((coordi_x-1, coordi_y))
                            coordi_x = coordi_x-1

                        contador_esloras_restantes = contador_esloras_restantes-1

                    colocar_barco_manual = len(lista_coordenadas_barco) == esloras

                if colocar_barco_manual:
                    barco_no_colocado=False
                    for x, y in lista_coordenadas_barco:
                        self.dimensiones[x,y] = 'O'
                    print(self.dimensiones)
                else:
                    print('La coordenada elegida ya contiene un barco, pruebe de nuevo')


                






