"""
This program prints out the lyrics of the song Surfin' Bird, a multiplication table for 13
and draws a polygon based on the input number of sides and length of each side.

Author: Nguyen Chinh Quan
Time: 35 minutes
"""
def print_surfin_bird():
    print("A-well-a, everybody's heard about the bird")
    for i in range(8):
        print("A-well-a, bird, bird, bird, b-bird's the word")
    print("Surfin' bird")
    for j in range(6):
        print("Papa-ooma-mow-mow, papa-ooma-mow-mow")
        for h in range(1):
            print("Ooma-mow-mow, papa-ooma-mow-mow")

def print_multiplication_table():
    for i in range(20):
        print("13 times",i+1,"=",13*(i+1))

import turtle
def draw_polygon():
    sides = int(input("Enter number of sides:"))
    length = int(input("Enter number of each side:"))
    for i in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)
    turtle.done()
