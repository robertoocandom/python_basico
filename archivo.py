# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    roberto = turtle.Turtle()

    make_square(roberto)
    turtle.mainloop()

def make_square(roberto):
    length = int(raw_input('Tamano de cuadrado: '))
    for i in range(8):
        make_line_and_turn(roberto, length)    


def make_line_and_turn(roberto, length):
    roberto.forward(length)
    roberto.left(45)

if __name__ == '__main__':
      main()