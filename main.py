
import turtle

from ball import Ball

WIDTH = 800
HEIGHT = 400


window = turtle.Screen()
turtle.setup(WIDTH + 20, HEIGHT + 20)
window.screensize(int(WIDTH/2), int(HEIGHT/2))
# window.setworldcoordinates(0, 0, WIDTH, HEIGHT)

# turtle._CFG.update({"canvWIDTH": WIDTH-20, "canvHEIGHT": HEIGHT-20})
window.bgcolor('black')
window.title('Bouncing ball')
window.tracer(False)


def start() -> None:
    """lance la creation des balles et l'algo
    """
    balls = []

    # Instantiation des balles
    # for _ in range(10):
    #     balls.append(Ball())

    # Methode avec liste de comprehension
    balls = [Ball() for _ in range(10)]

    # On boucle infiniment jusqu'au freeze
    while True:
        window.update()
        for ball in balls:
            ball.move()
            ball.bounce_floor(-HEIGHT / 2)
            ball.bounce_walls(WIDTH / 2)

            if ball.turtlesize() < (0.2, 0.2, 1):
                turtle.done()
        for i in range(len(balls)):
            for j in range(i+1, len(balls)):
                if balls[i].distance(balls[j]) < 15:
                    # A changer avec le bon calcul
                    temp_dx = balls[i].dx
                    temp_dy = balls[i].dy

                    balls[i].dx = balls[j].dx
                    balls[i].dy = balls[j].dy

                    balls[j].dx = temp_dx
                    balls[j].dy = temp_dy
                    balls[i].decrease_size()
                    balls[j].decrease_size()


start()
