"""
This program prints out a flag and a staircase pattern based on the user inputs.

Author: Nguyen Chinh Quan
Time spent: 25 minutes
"""
def draw_flag():
    """
    This function prints out a flag pattern based on the input of height.
    """
    Flag_height = int(input("Enter the height of the flag: "))
    for i in range(Flag_height):
        for j in range(Flag_height-1,-1,-1):
            if i==j:
                print('*', end = " ")
            elif i<j:
                print('* *', end = " ")
            else:
                print('. .',end = " ")
        print()
#draw_flag()
def draw_staircase():
    """
    This function prints out a staircase pattern based on the input of the height of the flight of stairs.
    and the width of each stair.
    """
    Staircase_height = int(input("Enter the height of the staircase: "))
    Staircase_width = int(input("Enter the width of the staircase: "))
    for i in range(Staircase_height):
        for j in range(Staircase_height):
            if j==i:
                print('* '*Staircase_width, end=" ")
            elif j>i:
                print('', end=" ")
            else:
                print('.', end=" ")
        print()
#draw_staircase()