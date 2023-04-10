"""
This program prints out a multiplication square using the input height and width from the user.

Author: Nguyen Chinh Quan
Time spent: 30 minutes
"""
def print_multiplication_square():
    Height = int(input("Enter height:"))
    Width = int(input("Enter width:"))
    for i in range(Height):
        for j in range(Width):
            print((j+1)*(i+1),end=" ")
        print()
print_multiplication_square()
