#Primero importamos todas las bibliotecas necesarias
import random
class Juego:
    
    def __init__(self,nombre=None):
        self.nombre=input("Introduce tu nombre para empezar a jugar: ")
                   
        #Creamos la lista de colores que vamos a utilizar en el juego    
        self.colores=['Rojo', 'Azul', 'Amarillo', 'Marron', 'Verde', 'Celeste', 'Blanco', 'Negro']
        
        #Imprimimos una presentacion y la funcion de inicio del juego
        print (f"Bienvenido {self.nombre} a MASTERMIND, tendras que elegir cuatro colores y colocarlos en la posicion correcta, tienes 8 oportunidades. Crees que serás capaz? Buena suerte!")
        
        
    #menu basico de opciones    
    def opciones(self):
            print("Para empezar a jugar: Jugar\nSi tienes dudas sobre como se juega: Dudas\nSi quieres saber cuales son los colores: Colores\nSi quieres salir: Salir")
            siguiente=input("Que quieres hacer? ")
            while True:
                #Comprobamos que el comando introducido es correcto 
                if siguiente=="Salir":
                    
                    print("Hasta la proxima!")
                    break
                    
                elif siguiente=="Jugar":
                    self.jugador()
                elif siguiente=="Dudas":
                    print("Se trata de adivinar un codigo secreto oculto! Tienes que adivinar la combinacion de colores correcta. Los colores se pueden repetir, cuando aciertes uno de las posiciones la respuesta de la maquina sera una X, si aciertas un color pero no esta en posicion correcta sera un O, si el color no esta se imprime un /")
                    self.opciones()
                elif siguiente=="Colores":
                    self.ejemplo_colores()
                    self.opciones()
                else:
                    print("Comando introducido no es correcto, intentalo de nuevo")
                    self.opciones()
            
                
        
    #ejemplo de colores coloerados
    def ejemplo_colores(self):
        print(f"Los colores disponibles son: ")
        print("Azul")
        print( "Rojo" )
        print( "Amarillo")
        print( "Marron" )
        print("Verde" )
        print( "Celeste" )
        print("Blanco" )
        print("Negro")
          
    
        
    #Vamos con la seleccion aleatoria de las cuatro bolas entre los 8 colores diferentes
    def seleccion_bolas(self):
        #para la seleccion aleatoria de los colores y su posicion
        self.colores=['Rojo', 'Azul', 'Amarillo', 'Marron', 'Verde', 'Celeste', 'Blanco', 'Negro']
        self.seleccion=random.choices(self.colores,k=4)
        return self.seleccion

       
    #creamos la funcion de pedir los colores e identificar si estan en el sitio correcto
    def jugador(self):
        seleccion=self.seleccion_bolas()
        #codigo para comprobaciones, se imprimen los colores en orden, lo dejo desseleccionado para jugar
        'print(seleccion)'
        
        #Comprobar que las oportunidades sea un numero:
        try:
            self.oportunidades=int(input("Introduce el numero de partidas que quieres jugar: (Lo establecido son 15) "))
        except ValueError:
            print("No has introducido un numero!")
            self.oportunidades=int(input("Introduce UN NUMERO de partidas que quieres jugar:  "))
        
        #Comienza el juego con las oportunidades que has marcado
        while self.oportunidades>0:
            #ahora vamos a comprobar que coincida el color      
            primer_numero=input("Introduce el primer color: ")
            segundo_numero=input("Introduce el segundo color: ")
            tercer_numero=input("Introduce el tercer color: ")
            cuarto_numero=input("Introduce el cuarto color: ")
            
            #creo una lista para imprimir el resultado
            self.resultado=[]       
            
            #condiciones del primer numero            
            if primer_numero==seleccion[0]:
                a="X"                
            elif primer_numero in seleccion:
                    a="O"                    
            elif primer_numero not in seleccion:
                    a="/"
                    
            #condiciones del segundo numero            
            if segundo_numero==seleccion[1]:
                    b="X"
            elif segundo_numero in seleccion:
                    b="O"
            elif segundo_numero not in seleccion:
                    b="/"
            
            #condiciones del tercer numero            
            if tercer_numero==seleccion[2]:
                c="X"
            elif tercer_numero in seleccion:
                c=("O")
            elif tercer_numero not in seleccion:
                c=("/")
                
            #condicones del cuarto numero:
            if cuarto_numero==seleccion[3]:
                d=("X")
            elif cuarto_numero in seleccion:
                d=("O")
            elif cuarto_numero not in seleccion:
                d=("/")
                
            #variable que junta el resultado y cambia el orden de las respuestas
            self.resultado=a+b+c+d
            ''.join(random.sample(self.resultado,len(self.resultado)))
            
            self.oportunidades-=1
            print(f'Te quedan {self.oportunidades} oportunidades todavia, recuerda que los colores son {self.colores}')
            
            
            if self.resultado=="XXXX":
                print("HAS CONSEGUIDO GANAR!!")
                self.opciones()
                break
            elif self.oportunidades==0:
                print(f"{self.resultado}\nHas sido derrotado!La respuesta correcta es: {seleccion}")
            
            #Una vez piedes que te devuelva al menu
                self.opciones()
        #Ahora se muestra el resultado
            print("======")
            print(f'|{self.resultado}|')
            print("======")
def main():
    while True:
        partida = Juego()
        partida.opciones()
        break
            
if __name__ == '__main__':
    main()