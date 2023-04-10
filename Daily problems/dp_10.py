"""
This program prints out a Latin square based on the user input.

Author: Nguyen Chinh Quan
Time spent: 30 minutes
"""
def print_latin_square():
    Latin_square_order=int(input("Enter the order of the Latin Square: "))
    for i in range(Latin_square_order):
        for j in range(Latin_square_order):
            if i<=j:
                print(j, end = " ")
        for k in range(Latin_square_order):
            if k<i:
                print(k, end = " ")
        print()
#print_latin_square()