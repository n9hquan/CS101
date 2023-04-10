"""
This program uses the Leibniz formula to print out the approximation to π obtained using the specified number of terms.

Author: Nguyen Chinh Quan
Time spent: 20 minutes
"""
def approximate_pi():
    Number_of_terms = input("How many terms would you like to use? ")
    Minus_half = int(0)
    Plus_half = int(0)
    for i in range(int(Number_of_terms)):
        if i%2==0:
            Plus_half = Plus_half + (1/(2*i+1))
        else:
            Minus_half = Minus_half - (1 / (2 * i + 1))
    Pi = 4*(Plus_half + Minus_half)
    print(Pi)
#approximate_pi()