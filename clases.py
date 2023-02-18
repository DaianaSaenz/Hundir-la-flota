import numpy as np
import random 
class Tablero:
    dimensiones = np.full((10,10), (" "))
    barcos = [2,2,2,3,3,4,1,1,1,1]

    def posicionar_barcos(self):
        # generar_coordenas_aleatorias


        for num_esloras in self.barcos:
            coordenadas_aleatorias_x = random.randint(0,9)
            coordenadas_aleatorias_y = random.randint(0,9)
            contador_esloras_restantes= num_esloras-1
            codernadas_esloras =[]
            puedo_colocar_barco=False
          
            while self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y ] != " ":
                coordenadas_aleatorias_x = random.randint(0,9)
                coordenadas_aleatorias_y = random.randint(0,9)
           
            #comprobar cordenadas aleatorias y que se pueda pintar numero de esloras
         
            ##comprobar que coordenadas no sean mayores que 10 y menores que 0
            #Pintar solo cuando comprobemos que todas las esloras puedan ser pintadas
            if num_esloras == 1:
                self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y ] = "O"
            else:
                codernadas_esloras.append((coordenadas_aleatorias_x, coordenadas_aleatorias_y))

                while contador_esloras_restantes !=0:


                    if coordenadas_aleatorias_x-1 >= 0 and self.dimensiones[ coordenadas_aleatorias_x-1, coordenadas_aleatorias_y ] == " " :
                        codernadas_esloras.append( (coordenadas_aleatorias_x - 1, coordenadas_aleatorias_y) )

                    elif  coordenadas_aleatorias_y-1 >= 0 and self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y - 1 ] == " ":
                        codernadas_esloras.append( (coordenadas_aleatorias_x, coordenadas_aleatorias_y -1 ) )
                        
                    elif  coordenadas_aleatorias_y + 1 <=9 and self.dimensiones[ coordenadas_aleatorias_x, coordenadas_aleatorias_y + 1 ] == " ":
                        codernadas_esloras.append(( coordenadas_aleatorias_x, coordenadas_aleatorias_y +1) )
                    
                    elif coordenadas_aleatorias_x+1 <=0 and self.dimensiones[ coordenadas_aleatorias_x+1, coordenadas_aleatorias_y] == " ":
                        codernadas_esloras.append((coordenadas_aleatorias_x+1, coordenadas_aleatorias_y) )

                    contador_esloras_restantes= contador_esloras_restantes -1
                puedo_colocar_barco = len(codernadas_esloras)==num_esloras

                print(num_esloras, codernadas_esloras)

            if puedo_colocar_barco:
                for x, y in codernadas_esloras:
                    self.dimensiones[x,y]="O"
        print(self.dimensiones)
