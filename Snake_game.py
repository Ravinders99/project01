# Import MOdule

import turtle
import time
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("game_sound.mp3")
pygame.mixer.music.play(1000)


delay =0.1


win = turtle.Screen()
win.setup(width=900,height=550)
win.title(" \t!!!SNAKE GAME!!!\t")
win.bgcolor("#1affa3")
win.tracer(0)





# Snake Head
head = turtle.Turtle()
head.shape("circle")
head.fillcolor("red")
head.pencolor("#99004d")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction="stop"


# food 

food = turtle.Turtle()
food.shape("turtle")
food.fillcolor("#0000ff")
food.pencolor("red")

food.speed(0)
food.penup()
food.goto(0,0)


segments =[]


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
    

# For move
class Move():
    def move(self):
        if head.direction == "up":
            y=head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y=head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x=head.xcor()
            head.setx(x -20)
        if head.direction == "right":
            x=head.xcor()
            head.setx(x + 20)

mv=Move()
dr=Direct()
win.listen()
win.onkeypress(dr.go_up,"w")        
win.onkeypress(dr.go_right,"d")        
win.onkeypress(dr.go_down,"s")        
win.onkeypress(dr.go_left,"a")               

# Main game loop

while True:
    win.update()
    # for chechking for barrier
    if head.xcor()> 450 or head.xcor()<-450 or head.ycor() > 260 or head.ycor() <-260:
        # pygame.mixer_music('D:\\game_over.mp3')
        pygame.mixer.music.load("game_over.mp3")
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.load("game_sound.mp3")
        pygame.mixer.music.play(1000)
        head.goto(0,0)
        head.direction ="stop"
    # hide the segment 
        for segment in segments :
            segment.goto(1000,1000)

        
    # clear the segment
        segments.clear()
    # Collide snake to his segment
    for segment in segments :
        if segment.distance(head) < 20:
            
            # playsound('D:\\game_over.mp3')
            head.goto(0,0)
            head.direction="stop"
     # hide the segment 
            for segment in segments :
                segment.goto(1000,1000)

        
    # clear the segment
            segments.clear()

    if head.distance(food) < 20:
        x= random.randint(-430, 430)
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