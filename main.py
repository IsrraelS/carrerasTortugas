import turtle
import random

class Circuito():
    corredores = []
    __posStarY = (-30, -10, 10, 30 )
    __colorTurtle = ('red', 'orange', 'blue', 'purple')
    
    #se crea el circuito
    
    def __init__(self, width, height):

        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__starLine = -width/2 + 20
        self.__finishLine = width/2 -20
        
    # se invoca los objetos corredores
    
        self.__crearCorredores()
    
    # aqui se crean los corredores
    
    def __crearCorredores(self):
        for i in range(4):
                new_turtle = turtle.Turtle()
                new_turtle.color(self.__colorTurtle[i])
                new_turtle.shape('turtle')
                new_turtle.penup()
                new_turtle.setpos(self.__starLine, self.__posStarY[i])
                
                self.corredores.append(new_turtle)
                
    def competir(self):
        
        ganador = False
        
        while not ganador:
            for tortuga in self.corredores:
                avance = random.randint(1, 6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    ganador = True
                    print("la tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
        
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()