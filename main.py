import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move,"w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.is_at_finish() == True:
        player.go_to_start()
        cars.level_up()
        score.increase_level()
        score.update_scoreboard()



screen.exitonclick()