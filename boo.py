from tkinter import *
 
class Ball:
    def __init__(self, xpos, ypos, v):
        self.x = xpos
        self.y = ypos
        self.v_x = v
        self.v_y = v
        self.image = canvas.create_rectangle(self.x,self.y,self.x+10,self.y+10, fill='black')
     
    def bounce_x(self):
        self.v_x = self.v_x*-1
         
    def bounce_y(self):
        self.v_y = self.v_y*-1
 
    def move(self):
        #increments ball location
        self.x = self.x+self.v_x
        self.y = self.y+self.v_y
        #draws ball to canvas
        canvas.move(self.image, self.v_x,self.v_y)
        canvas.update()
     
h = 400
w = 500
Window = Tk()
 
canvas = Canvas(height=h, width=w, bg='white')
canvas.pack()
 
balls = [Ball(h/2,w/2,2)]
 
while True:
    for ball in balls:
        if ball.x >w:
            ball.bounce_x()
        elif ball.x <0:
            ball.bounce_x()
        if ball.y >h:
            ball.bounce_y()
        elif ball.y <0:
            ball.bounce_y()
        ball1.move()
    canvas.update()
    canvas.after(10)
 
Window.mainloop()
