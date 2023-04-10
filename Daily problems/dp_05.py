"""
This program uses a turtle to draw a picture in Task 1: Following Directions and
performs a shuffle in Task 2: The Perfect Shuffle

Author: Nguyen Chinh Quan
Time spent: 35 minutes
"""
import turtle
def steer_turtle():
    """
    Task 1: Following Directions
    This function uses turtle graphics to draw a picture based on the input of two lists of numbers: step and angles.
    """
    list_step_sizes = input("Enter the step sizes to take (as a list): ")
    list_angles = input("Enter the angles to turn by (as a list): ")
    list_step_sizes = eval(list_step_sizes)
    list_angles = eval(list_angles)
    for i in range(len(list_step_sizes)):
        turtle.forward(list_step_sizes[i])
        turtle.right(list_angles[i])
    turtle.done()
#steer_turtle()
def shuffle():
    """
    Task 2: The Perfect Shuffle
    This function prints out the result of performing a perfect shuffle on the input list.
    """
    list_to_shuffle = input("Enter list: ")
    list_to_shuffle = eval(list_to_shuffle)
    first_half_of_list = []
    second_half_of_list = []
    list_shuffled = []
    first_half_of_list = list_to_shuffle[0:int(len(list_to_shuffle)/2)]
    second_half_of_list = list_to_shuffle[int(len(list_to_shuffle)/2):]
    for i in range(len(first_half_of_list)):
            list_shuffled = list_shuffled + [first_half_of_list[i]] + [second_half_of_list[i]]
    print(list_shuffled)
#shuffle()