import turtle

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
    
        self._crearCorredores()
    
    # aqui se crean los corredores
    
    def __crearCorredores(self):
        for i in range(4):
                new_turtle = turtle.Turtle()
                new_turtle.color(self.__colorTurtle[i])
                new_turtle.shape('turtle')
                new_turtle.penup()
                new_turtle.setpos(self.__starLine, self.__posStarY[i])
                
                
                self.corredores.append(new_turtle)
                
    
        
if __name__ == '__main__':
    circuito = Circuito(640, 480)