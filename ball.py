
import random
from turtle import Turtle


class Ball(Turtle):
    """Créé une balle qui hérite de Turtle

    Args:
        Turtle (class): retourne une fonction turtle Screen
    """

    colors = ['red', 'yellow', 'green', 'white',
              'blue', 'pink', 'orange', 'brown', 'purple']

    def __init__(self) -> None:
        """Recuperation des attributs de la classe parent puis
        initialisation des attributs de la balle
        """
        super().__init__()
        # self.penup()
        self.color(random.choice(self.colors))
        self.shape('circle')
        self.speed(6)
        x = random.randint(-200, 200)
        y = random.randint(-400, 400)
        self.goto(x, y)

        # Vitesse sur chaque axes
        self.dy = random.randint(-3, 3)
        self.dx = random.randint(-3, 3)
        # self.turtlesize(3.0, 3.0, 1)

    def move(self) -> None:
        """Set les nouvelles coordonnées x & y
        """
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)

    def bounce_floor(self, y: int) -> None:
        """Change la direction de la balle si elle touche le plafond
        ou le sol

        Args:
            y (int): axe y
        """
        if self.ycor() < y:
            self.dy *= -1
            self.sety(y)

        if self.ycor() > -y:
            self.dy *= -1
            self.sety(-y)

    def bounce_walls(self, x: int) -> None:
        """Change la direction de la balle si elle touche un mur

        Args:
            x (int): axe x
        """
        if self.xcor() > x:
            self.dx *= -1

        if self.xcor() < -x:
            self.dx *= - 1

    # def collision(self, other_ball):
    #     temp_dx = self.dx
    #     temp_dy = self.dy

    #     self.dx = other_ball.dx
    #     self.dy = other_ball.dy

    #     other_ball.dx = temp_dx
    #     other_ball.dy = temp_dy
    #     return other_ball

    def decrease_size(self) -> None:
        """Divise la taille de la balle par 2
        """
        size = self.turtlesize()
        decrease = (num / 2 for num in size)
        # decrease[0] -= 0.1
        # decrease[1] -= 0.1
        self.turtlesize(*decrease)
