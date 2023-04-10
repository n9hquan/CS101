"""
This function prints out the longest and lowest index DNA string in a list of input DNA strings.

Author: Nguyen Chinh Quan
Time spent: 15 minutes
"""
def find_longest_strand():
    temp = ""
    List_of_DNA_strands = input("Enter list of DNA strands: ")
    List_of_DNA_strands = eval(List_of_DNA_strands)
    for i in range(len(List_of_DNA_strands)):
        if len(temp) < len(List_of_DNA_strands[i]):
            temp = List_of_DNA_strands[i]
    print("Longest strand:",temp)
find_longest_strand()
