"""
This program calculates the value of Lorentz Factor using the Lorentz Factor Formula
and the value of a polynomial using the given polynomial formula.

Author: Nguyen Chinh Quan
Time spent: 45 minutes
"""
def compute_lorentz_factor():
    fltVelocity = v = float(input("Enter object velocity (as a fraction of c): "))
    fltLorentzfactor = 1/((1-v**2))**0.5
    formatted_string = "{:.11f}".format(fltLorentzfactor)
    float_value = float(formatted_string)
    print("Lorentz factor: ", float_value)
""" x^12-2x^6+x^4 we put t=x^2
    => t^6-2t^3+t^2 
    = (t^3)^2- 2t^3x1+1+t^2-1 
    = (t^3-1)^2+(t^2-1) (1)
We have: a^3 - b^3 = (a-b)^3-3ab(a-b)
    => t^3 - 1 = (t-1)^3-3t(t-1)=(t-1)[(t-1)^2-3t]=(t-1)(t^2-5t+1)
 (1)=> (t-1)(t^2-5t+1)+(t+1)(t-1)
    = (t-1)(t^2-4t+2)
    = (t-1)*(t*t-4*t+2)"""
def evaluate_polynomial():
    fltValueofx = x = float(input("Enter the value of x: "))
    fltValueofp = x**12-2*x**6+x**4
    formatted_string1 = "{:.12f}".format(fltValueofp)
    float_value1 = float(formatted_string1)
    print("The value of p is: ", float_value1)

