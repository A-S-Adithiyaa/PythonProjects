import turtle as t
t.speed(1)


side = 200 #Set the desired outside square side length


def square(side):
    for i in range(4):
        t.forward(side)
        t.right(90)


def tiltsquare(tilted_side):
    t.forward(tilted_side / (2 ** 0.5))
    t.right(45)
    for i in range(4):
        t.forward(tilted_side)
        t.right(90)


def squareinsquare(side):
    square(side)
    tiltsquare(side / 2 ** 0.5)


squareinsquare(side)