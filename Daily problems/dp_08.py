"""
This program prints out a right triangle based on the input of height from the user.

Author: Nguyen Chinh Quan
Time spent: 10 minutes
"""
def draw_outlined_triangle():
    height = int(input("Enter height: "))
    for i in range(height):
        for j in range(height):
            if j==0 or i==j:
                print('%',end = " ")
            elif j>i:
                print('',end = " ")
            else:
                print('*',end = " ")
        print()
#draw_outlined_triangle()