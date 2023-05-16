import turtle as t
import time
from snake_for_game import Snake
import food as f
import scoreboard as sc

# setup the screen
screen=t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# creating an objet from snake_for_game which is create the snake body
snake=Snake()
food=f.Food()
score=sc.Scoreboard()


screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    # moving the snake
    snake.move()

    # creating the score and refresh
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # if collision with wall the game is not over
    if snake.head.xcor() > 280:
        for i in range(300,-300,-1):
            if snake.head.ycor()==i:
                snake.start_from1(-280,i)
        # score.game_over()
        # game_is_on=False
    
    if snake.head.xcor() < -280:
        for i in range(300,-300,-1):
            if snake.head.ycor()==i:
                snake.start_from1(280,i)
    
    if snake.head.ycor() > 280:
        for i in range(300,-300,-1):
            if snake.head.xcor()==i:
                snake.start_from1(i,-280)

    if snake.head.ycor() < -280:
        for i in range(300,-300,-1):
            if snake.head.xcor()==i:
                snake.start_from1(i,280)


    # detec segment with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()
            game_is_on=False















screen.exitonclick()