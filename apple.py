from turtle import Screen ,Turtle
from time import sleep 
s=Screen()
s.setup(600,600);s.bgcolor("black")
height,width= s.window_height() ,s.window_width()
turtles= []
positions=[]

lenPos=0
for newPos in range(3):#set positions
    lenPos+= 20
    pos=(-width/2+lenPos,0)
    positions.append(pos)
s.tracer(0)
for i in range(len(positions)):#creating t with set his positions
    t= Turtle("square")
    t.color("white")
    t.up()
    t.goto(positions[i])
    t.degrees(360)
    turtles.append(t)
s.update()
while True :
    for t in turtles:
        t.forward(2)
        cardinats=t.pos()#x,y
        
        if cardinats[0] >= width/2+20  :
               t.goto(-width/2-20,cardinats[1])
        elif cardinats[0]  <= -width/2-20:
               t.goto(width/2+20,cardinats[1])
        elif cardinats[1]  >= height/2+20:
                t.goto(cardinats[0],-height/2)
        elif cardinats[1] <= -height/2-20:
                t.goto(cardinats[0],height/2)
        sleep(0.000001)
         
        s.update()
            
