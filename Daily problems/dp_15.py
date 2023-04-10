"""
This program contains one programming problem named Pikachu.

Author: Nguyen Chinh Quan
Time spent: 45 minutes
"""
def is_speakable(Pikachu_pronounce):
    """
    Description: This function tests the input string whether it can be pronounced by Pikachu or not.

    Parameter:
        Pikachu_pronounce: Pikachu pronounced word
    Return: Print the result True or False to the screen
    """
    position_of_word = 0
    boolean_value = 0
    while position_of_word<len(Pikachu_pronounce):
        if position_of_word+1<len(Pikachu_pronounce) and Pikachu_pronounce[position_of_word]=="p" and Pikachu_pronounce[position_of_word+1]=="i":
            position_of_word +=2
            continue
        elif position_of_word+1<len(Pikachu_pronounce) and Pikachu_pronounce[position_of_word]=="k" and Pikachu_pronounce[position_of_word+1]=="a":
            position_of_word +=2
            continue
        elif position_of_word+2<len(Pikachu_pronounce) and Pikachu_pronounce[position_of_word] == "c" and Pikachu_pronounce[position_of_word+1]=="h" and Pikachu_pronounce[position_of_word+2]=="u":
            position_of_word += 3
            continue
        else:
            boolean_value = 1
            break
    if boolean_value==0:
        print("True")
    else:
        print("False")
