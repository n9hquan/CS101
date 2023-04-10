"""
This program contains one programming problem named Minimum Cost Palindrome.

Author: Nguyen Chinh Quan
Time spent: 60 minutes
"""
def min_cost_palindrome(string_to_change,o_cost,x_cost):
    """
    Description: Check the input string whether it is a palindrome string or not and calculate the cost to change
    the string into a palindrome string if it is not.
    Parameter:
        string_to_change: A string of even length
        o_cost: the cost to replace "?" with "o"
        x_cost: the cost to replace "?" with "x"
    Return: The minimum cost of replacing "?"s with "x"s and "o"s that turns string_to_change into a palindrome.
    """
    if string_to_change == "":
        return 0
    sum_letters_used = 0
    for i in range(len(string_to_change)//2):
        if string_to_change[i] == "?" and string_to_change[-i-1] == "o":
            sum_letters_used += o_cost
        elif string_to_change[i] == "?" and string_to_change[-i-1] == "x":
            sum_letters_used += x_cost
        elif string_to_change[i-1] == "?" and string_to_change[i] == "o":
            sum_letters_used += o_cost
        elif string_to_change[i-1] == "?" and string_to_change[i] == "x":
            sum_letters_used += x_cost
        elif string_to_change[i] == "?" and string_to_change[-i-1] == "?":
            sum_letters_used += min(o_cost, x_cost) * 2
        elif string_to_change[i] == string_to_change[-i-1]:
            continue
        else:
            return -1
    if sum_letters_used == 0:
        return sum_letters_used
    else:
        return sum_letters_used

