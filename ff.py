from turtle import  *

class Face:
    def __init__(self,xpos,ypos):
        self.size = 90
        self.coord = (xpos,ypos)
        self.noseSize = 'Small'
    def setSize(self,radius):
        self.size = radius
    
    
    def draw(self):
        self.goHome()
        pensize(5)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawMouth()
        self.drawNose()
        pensize(5)
        
        
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)
        
        
    def drawOutline(self):
        penup()
        forward(self.size)
        self.goHome()
        
    def drawEye(self,turn):
        penup()
        forward(self.size/2)
        pendown()
        dot(self.size/10)
        self.goHome()
        
    def drawMouth(self):
        penup()
        forward(self.size/1.7)
        left(90) 
        pendown()
        circle(self.size/1.7,90)
        self.goHome()
        
    def drawNose(self):
        if self.noseSize =='large':
            dot(self.size/2, 'gray') 
        elif self.noseSize ==  'Small':
            dot(self.size/6, 'gray')
        else :
            dot(self.size/6, 'gray')
            self.goHome()
                
           
        
x =Face(0,0)
x.draw()       
showturtle()
done()
            
            
        

    