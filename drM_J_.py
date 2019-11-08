import turtle
window=turtle.Screen()

# TODO (Marie)

def rectangle(w,h,clr):
    turtle.color(clr)
    for i in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)
    turtle.right(90)
def triangle(a,b,angle,clr):
    turtle.color(clr)
    turtle.forward(b)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.back(b)
    turtle.left(angle)
    turtle.forward(a)
    turtle.goto(x, y)
    turtle.right(angle)
    turtle.back(b)

# домик
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

turtle.begin_fill()
turtle.width(10)
triangle(100, 100, 60, "dark blue")
turtle.end_fill()

turtle.begin_fill()
rectangle(100, 90, "dark red")
turtle.end_fill()

# машинка
# переход на новое место
turtle.penup()
turtle.goto(50, 100)
turtle.pendown()

# рисуем корпус машинки
turtle.begin_fill()
turtle.color("black")
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(60)
turtle.left(60)
turtle.forward(40)
turtle.right(60)
turtle.forward(60)
turtle.right(60)
turtle.forward(40)
turtle.left(60)
turtle.forward(60)
turtle.right(60)
turtle.forward(45)
turtle.right(120)
turtle.forward(210)
turtle.right(180)
turtle.forward(130)
turtle.end_fill()


# рисуем колеса
# перемещаемся к центру первого колеса
turtle.penup()
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.pendown()
# Рисуем первое колесо
turtle.color("grey")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
# Перемещаемся к центру второго колеса
turtle.penup()
turtle.left(180)
turtle.forward(80)
turtle.right(90)
turtle.forward(20)
turtle.pendown()
# рисуем второе колесо
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

#шарик
# перемещаемся на новое место
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

turtle.width(5)
turtle.right(90)
turtle.begin_fill()
turtle.color("red")
turtle.circle(40)
turtle.end_fill()
# рисуем ниточку и треугольничек
turtle.right(90)
turtle.color("black")
turtle.forward(100)
turtle.color("red")
turtle.right(180)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.left(150)
turtle.forward(10)
turtle.left(120)
turtle.forward(10)
turtle.left(120)
turtle.forward(10)

# TODO (Julia)

def rectangle(w,h,clr):
    turtle.color(clr)
    for i in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)
    turtle.right(90)
def triangle(a,b,angle,clr):
    turtle.color(clr)
    turtle.forward(b)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.back(b)
    turtle.left(angle)
    turtle.forward(a)
    turtle.goto(x, y)
    turtle.right(angle)
    turtle.back(b)

# смайлик
# перемещаемся на новое место
turtle.penup()
turtle.goto(150, -100)
turtle.pendown()

# рисуем круг
turtle.width(20)
turtle.right(190)
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(60)
turtle.end_fill()

# рисуем глаза и рот
turtle.penup()
turtle.goto(160, -63)
turtle.pendown()
turtle.width(6)
turtle.right(290)
turtle.color("black")
turtle.forward(26)
turtle.penup()
turtle.goto(240, -74)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
turtle.goto(173, -104)
turtle.pendown()
turtle.right(57)
turtle.begin_fill()
turtle.circle(40, 117)

# забор
# перемещаемся на новое место
turtle.penup()
turtle.goto(-300, -50)
turtle.pendown()

# рисуем первую доску
turtle.right(180)
turtle.begin_fill()
turtle.width(5)
triangle(50, 50, 60, "brown")
turtle.end_fill()
turtle.forward(50)
turtle.left(30)
turtle.begin_fill()
rectangle(100, -50, "brown")
turtle.end_fill()

# рисуем ещё две дощечки
turtle.left(180)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(180)
turtle.begin_fill()
turtle.width(5)
triangle(50, 50, 60, "brown")
turtle.end_fill()
turtle.forward(50)
turtle.left(30)
turtle.begin_fill()
rectangle(100, -50, "brown")
turtle.end_fill()
turtle.left(180)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(180)
turtle.begin_fill()
turtle.width(5)
triangle(50, 50, 60, "brown")
turtle.end_fill()
turtle.forward(50)
turtle.left(30)
turtle.begin_fill()
rectangle(100, -50, "brown")
turtle.end_fill()

# рисуем машинку
# перемещаемся на новое место
turtle.penup()
turtle.goto(-420, 100)
turtle.pendown()

# рисуем корпус машинки и всё остальное
turtle.right(180)
turtle.color(1,0,0)
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.end_fill()

turtle.color(0,0,0)
turtle.up()
turtle.forward(10)
turtle.down()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.setheading(0)
turtle.up()
turtle.forward(90)
turtle.right(90)
turtle.forward(10)
turtle.setheading(0)
turtle.begin_fill()
turtle.down()
turtle.circle(10)
turtle.end_fill()



window.exitonclick()

