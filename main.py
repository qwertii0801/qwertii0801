import turtle

def draw_tree(branch_len, t, angle=20):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(angle)
        draw_tree(branch_len - 15, t, angle)
        t.left(angle * 2)
        draw_tree(branch_len - 15, t, angle)
        t.right(angle)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_tree(75, t)
    screen.exitonclick()


if __name__ == "_main_":
    main()