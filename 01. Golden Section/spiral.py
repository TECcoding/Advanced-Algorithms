import turtle

def square(size: int) -> None:
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def golden_spiral(size: int) -> None:
    for i in range(1, 100):
        square(i * 10)
        turtle.right(10)



if __name__ == '__main__':
    golden_spiral(200)
    turtle.done()