import tkinter
import random
import time
tk = tkinter.Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",True)
canvas = tkinter.Canvas(tk,width=700,height=700,bd=0,highlightthickness = 0)
canvas.configure(background ='black')
canvas.pack()
tk.update()

class Score:
    def __init__(self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(600,70,text = self.score,fill =color,font = ("Purisa",50))
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id,text = self.score)

class Ball:
    def __init__(self,canvas,paddle,score,color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.color = color
        self.id = canvas.create_oval(50,50,75,75,fill= self.color)
        self.canvas.move(self.id,300,200)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_button = False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)

        if pos[1]<=0:
            self.y = 3
        if pos[3]>= self.canvas_height:
            self.hit_button = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0]<=0:
            self.x = 3
        if pos[2]>= self.canvas_width:
            self.x = -3

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <=paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += paddle.x
                self.score.hit()
                return True
        return False
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,200,20,fill=color)
        self.canvas.move(self.id,250,500)
        self.x = 0
        self.started = False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)
        
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2
    def start_game(self,evt):
        self.started = True

score = Score(canvas,'green')
paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle,score,"red")
game_over_text = canvas.create_text(350,300,text = 'Game~ Over~',state='hidden',fill = 'blueviolet',font = ("Purisa",50))

while True:
    if ball.hit_button == False and paddle.started == True:
        ball.draw()
        paddle.draw()
        if ball.hit_button == True:
            canvas.itemconfig(game_over_text,state = 'normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
