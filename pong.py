# Pong game inspored from Tokyoedtech

import turtle
import random
import math

# Initialisation des score
score_a = 0
score_b = 0

# Main frame
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Jeu de Pong inspired by Tokyoedtech")
wn.setup(height=600, width=800)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.setx(350)
paddle_a.sety(0)
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(3, 1)
paddle_a.color("white")
paddle_a.penup()

# paddle B
paddle_b = turtle.Turtle()
paddle_b.setx(-350)
paddle_b.sety(0)
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(3, 1)
paddle_b.color("white")
paddle_b.penup()

# ball
ball = turtle.Turtle()
ball.sety(0)
ball.setx(0)
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()

# Ecriture des scores
score = turtle.Turtle()


def print_score(score_a:int, score_b:int) -> None:
    """

    :type score_b: None
    """
    score.clear()
    score.sety(270)
    score.setx(0)
    score.color("white")
    score.write("Player A : {} - Player B : {}".format(score_a, score_b), align="center",font=("Arial", 15, "normal"))
    score.hideturtle()

print_score(score_a,score_b)

# deplacements paddle_a
def paddle_a_up():
    paddle_a.sety(paddle_a.pos()[1] + 15)


def paddle_a_down():
    paddle_a.sety(paddle_a.pos()[1] - 15)


## deplacements paddle_b
def paddle_b_up():
    paddle_b.sety(paddle_b.pos()[1] + 15)


def paddle_b_down():
    paddle_b.sety(paddle_b.pos()[1] - 15)

# Détermine la rapidité de la balle

def ball_reinit():
    """Fonction de reinitialisation des deplacements de la ball"""
    while 1:
        deltax = random.randint(-45,45)/100.0
        deltay = random.randint(-45,45)/100.0
        if math.fabs(deltay)>.20 and math.fabs(deltax)>.20:
            break
    return deltax, deltay

deltax,deltay = ball_reinit()

# Main game loop
while True:

    wn.update()

    # touches pour lancer les déplacements des paddles
    wn.onkey(paddle_a_up, "Up")
    wn.onkey(paddle_a_down, "Down")
    wn.onkey(paddle_b_up, "q")
    wn.onkey(paddle_b_down, "w")

    # deplacement de la boule
    ball.sety(ball.pos()[1] + deltay)
    ball.setx(ball.pos()[0] + deltax)

    # collision de la ball avec les bords inferieurs et superieurs de l'écran
    if ball.pos()[1] > 290.0:
        deltay = -deltay
    if ball.pos()[1] < -290.0:
        deltay = -deltay

    # paddle_a renvoit la balle
    if (ball.pos()[0] > 350.0 and (ball.pos()[1] > paddle_a.pos()[1] - 30.0 and ball.pos()[1] < paddle_a.pos()[1] + 30.0)):
        deltax = -deltax

    if (ball.pos()[0] < -350.0 and (ball.pos()[1] > paddle_b.pos()[1] - 30.0 and ball.pos()[1] < paddle_b.pos()[1] + 30.0)):
        deltax = -deltax


    # Balle sort du jeu et repart de manière aléatoireprint
    if (ball.pos()[0] < -400.0 or ball.pos()[0] > 400.0 ):
        if ball.pos()[0] < 0:
            score_b += 1
        else:
            score_a += 1
        print_score(score_a,score_b)
        ball.sety(0)
        ball.setx(0)
        deltax,deltay=ball_reinit()

    wn.listen()
