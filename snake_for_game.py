from turtle import Turtle
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

STARTING_POSITION=[(-230,0),(-250,0),(-270,0)]
START1=[(280,0),(250,0),(270,0)]
START2=[(0,-280),(0,-250),(0,-270)]
START3=[(0,280),(0,250),(0,270)]

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        # turtle.speed("fast")
        for positions in STARTING_POSITION:
            self.add_segment(positions)

    # creating a new segment
    def add_segment(self, position):
        new_segments=Turtle()
        new_segments.shape("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # global segments
        for seg in range(len(self.segments)-1,0,-1):
            x_seg=self.segments[seg-1].xcor()
            y_seg=self.segments[seg-1].ycor()
            self.segments[seg].goto(x_seg, y_seg)
        self.head.forward(MOVE_DISTANCE)
                    

    def start_from1(self, pos1,pos2):
        self.head.goto(pos1,pos2)
    
    def start_from2(self,pos1,pos2):
        self.head.goto(pos1,pos2)
    
    def start_from3(self,pos1,pos2):
        self.head.goto(pos1,pos2)

    def start_from4(self,pos1,pos2):
        self.head.goto(pos1,pos2)
    

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



