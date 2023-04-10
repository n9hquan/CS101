"""
This program contains one programming problem named Magic Square.

Author: Nguyen Chinh Quan
Time spent: 20 minutes
"""
def is_magic_square(nested_list):
    """
    Description: Check the input list if it is a magic square or not. 
    Parameters:
        nested_list: a nested list of integers
    Return: True or False
    """
    #check sum of rows
    sum_of_first_row = sum(nested_list[0])
    for i in range(1,len(nested_list)):
        if sum(nested_list[i]) != sum_of_first_row:
            return False
    # check sum of columns
    sum_of_first_column = 0
    sum_of_column = 0
    for i in range(len(nested_list)):
        sum_of_first_column += nested_list[i][0]
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            sum_of_column += nested_list[j][i] 
        if sum_of_column != sum_of_first_column:
            return False
        else:
            sum_of_column = 0
    # check sum of two diagonals
    sum_of_left_to_right_diagonal = 0
    sum_of_right_to_left_diagonal = 0
    for i in range(len(nested_list)):
        sum_of_left_to_right_diagonal += nested_list[i][i]
    for i in range(len(nested_list)):
        sum_of_right_to_left_diagonal += nested_list[i][-i-1] 
    if sum_of_left_to_right_diagonal != sum_of_right_to_left_diagonal:
        return False
    return True      
# print(is_magic_square([[2,7,6],[9,5,1],[4,3,8]]))