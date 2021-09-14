"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

Integrantes:
Karen Lizette Rodríguez Hernández - A01197734
Jorge Eduardo Arias Arias - A01570549
Hernán Salinas Ibarra - A01570409

13/09/2021

Ejercicios denotados por ***ejercicio realizado***

"""
# Importamos librerias necesarias
from turtle import *
from freegames import vector

# Función para dibujar una linea desde un punto hasta otro
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    # Colorea la figura
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función para dibujar un circulo
def circle(start, end):                 # ***Función de circulo completada***
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    dot(end.x - start.x)

# Función para dibujar un rectangulo
def rectangle(start, end):                 # ***Función de rectangulo completada***
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    # Colorea la figura
    begin_fill()
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.x/2 - start.x/2)
        left(90)
    end_fill()

# Función para dibujar triangulo
def triangle(start, end):                 # ***Función de triangulo completada***
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    # Colorea la figura
    begin_fill()
    for i in range(3):
        forward(end.x - start.x)
        width(3-i)
        left(120)
        
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: pensize(pensize()+1), '+')   # ***Ancho de linea editable***
onkey(lambda: pensize(pensize()-1), '-')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')         # ***Color morado agregado***
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()