"""
This program contains 1 programming problem named Pig Latin.

Author: Nguyen Chinh Quan
Time spent: 15 minutes
"""
def to_pig_latin(word):
    """
    Description: Change a word to Pig Latin using the given rules.

    Parameter:
        word: A single string
    Return: The translated string
    """
    word = str(word)
    way = "way"
    ay = "ay"
    result = ""
    if word[0] in "ueoai":
        result = word + way
    else:
        for i in range(len(word)):
            if word[i] in "ueoai":
                consonant_clusters = word[(i-1)::-1][-1::-1]
                remove_consonant_clusters = word[i::1]
                result = remove_consonant_clusters + consonant_clusters + ay
                break
    return result
