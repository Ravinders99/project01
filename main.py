# Import Mddule
import turtle
import time
import random
import pygame
# For  control
class Direct:
    def go_up(self):
        if head.direction != "down":
            head.direction = "up"
    def go_down(self):
        if head.direction != "up":
            head.direction = "down"
    def go_left(self):
        if head.direction != "right":
            head.direction = "left"
    def go_right(self):
        if head.direction != "left":
            head.direction = "right" 
dr=Direct()
# For move
class Move():
    def move(self):
        if head.direction == "up":
            y=head.ycor()
            head.sety(y + 20)
            head.setheading(90)
            
        if head.direction == "down":
            y=head.ycor()
            head.sety(y - 20)
            head.setheading(270)
            
        if head.direction == "left":
            x=head.xcor()
            head.setx(x -20)
            head.setheading(180)
            
        if head.direction == "right":
            x=head.xcor()
            head.setx(x + 20)
            head.setheading(360)
            
mv=Move()
delay =0.1
score=0
try:
    with open('highscore.txt', 'r') as f:
        high_score = int(f.readline())
        f.seek(0) 
        # print(high_score)d
except:
    high_score = 0
pygame.mixer.init()
pygame.mixer.music.load("./sound/gta_san_andreas.mp3")
pygame.mixer.music.play(1000)
# background image
# bg = pygame.image.load("snake2.jpg")
# Screen 
win = turtle.Screen()
win.setup(width=900,height=550)
win.title(" \t!!!SNAKE GAME!!!\t")
win.bgpic('./gif/snake.gif')

win.tracer(0)
# pen 
pen =turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(220,150)
pen.write("SCORE =0 \nHIGHSCORE =0\n", move=False, align="center",font=('Arial',8, 'bold'))
pen.hideturtle()
# Border
border=turtle.Turtle()
border.color("black")
border.penup()
border.setposition(-450,-275)
border.speed(0)
border.pendown()
for size in range(2):
    border.fd(650)
    border.lt(90)
    border.fd(550)
    border.lt(90)

border.hideturtle()


# Snake Head
head = turtle.Turtle()
head.shape("turtle")
head.shapesize(1.1,1.1)
head.fillcolor("red")
head.pencolor("#99004d")
head.speed(0.001)
head.penup()
head.goto(10,10)
head.direction="stop"
# food 
food = turtle.Turtle()
food.shape("square")
food.shapesize(0.8,0.8)
food.fillcolor("#0000ff")
food.pencolor("red")
food.speed(0)
food.penup()
food.goto(0,100)
segments =[]


win.listen()
win.onkeypress(dr.go_up,"w")        
win.onkeypress(dr.go_right,"d")        
win.onkeypress(dr.go_down,"s")        
win.onkeypress(dr.go_left,"a")
# Main game loop
while True:
    win.update()
    # score 
    # for chechking for barrier
    if head.xcor()> 190 or head.xcor()<-450 or head.ycor() > 260 or head.ycor() <-260:       
        pygame.mixer.music.load("./sound/game_over_sms.mp3")
        pygame.mixer.music.play()
        time.sleep(1.5)
        pygame.mixer.music.load("./sound/gta_san_andreas.mp3")
        pygame.mixer.music.play(1000)
        head.goto(0,0)
        head.direction ="stop"
        # hide the segment 
        for segment in segments :
            segment.goto(1000,1000)       
        segments.clear()     # clear the segment
        score=0    # Reset score
    pen.clear()
    pen.write(f"SCORE = {score}\nHIGHSCORE={high_score}".format(score,high_score),move=False, align="left",font=('Arial', 20, 'bold'))
    # Collide snake to his segment
    for segment in segments :
        if segment.distance(head) < 20:
            pygame.mixer.music.load("./sound/game_over_sms.mp3")
            pygame.mixer.music.play()
            time.sleep(1.5)
            pygame.mixer.music.load("./sound/gta_san_andreas.mp3")
            pygame.mixer.music.play(1000)            
            head.goto(0,0)
            head.direction="stop"
            # hide the segment 
            for segment in segments :
                segment.goto(1000,1000)      
            segments.clear() # clear the segment
            score=0 # Reset score
        pen.clear()
        pen.write(f"SCORE = {score}\nHIGHSCORE={high_score}".format(score,high_score),move=False, align="left",font=('Arial', 20, 'bold'))
    if head.distance(food) < 20:
        x= random.randint(-430, 170)
        y= random.randint(-250, 250)
        food.goto(x,y)
        # Add segments 
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("circle")
        new_segments.fillcolor("#ff8080")
        new_segments.pencolor("red")
        new_segments.penup()
        segments.append(new_segments)
        score+=10
        if score >high_score:
            high_score = score
        pen.clear()
        pen.write(f"SCORE = {score}\nHIGHSCORE={high_score}".format(score,high_score),move=False, align="left",font=('Arial', 20, 'bold'))
        with open("highscore.txt","w") as f:
            f.write(str(high_score))
    for index in range(len(segments)-1,0,-1):
        x= segments[(index)-1].xcor()
        y= segments[(index)-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0 :
        x= head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    mv.move()
    time.sleep(delay)
win.mainloop()
