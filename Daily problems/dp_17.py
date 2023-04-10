"""
This program contains two programming problems called Scrabble Scoring and DNA Sequence Alignment.

Author: Nguyen Chinh Quan
Time spent: 40 minutes
"""
def scrabble_score_file(filename):
    """
    Description: Retrieve words from the input text file and calculate the score.
    Parameter:
        filename: A single input text file
    Return: The average scrabble score of all the words in the specified file.
    """
    sum = 0
    TILE_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                   "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                   "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                   "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                   "y": 4, "z": 10}
    word_split = open(filename).read().split()
    for i in range(len(word_split)):
        for j in range(len(word_split[i])):
            if word_split[i][j] in TILE_SCORES:
                sum += TILE_SCORES.get(word_split[i][j])
    average = sum / len(word_split)
    return average

def compute_dna_distance(all_list_DNA):
    """
    Description: Determine the “distance” between each pair of DNA strands.
    Parameter:
        all_list_DNA: A list of strings (each of which contains two DNA strand descriptors)
    Return: A list of integers, indicating the distance between the respective pair of DNA strings.
    """
    list_of_integers = []
    for i in range(len(all_list_DNA)):
        distance = 0
        list_DNA = all_list_DNA[i].split()
        dna_strand_1 = list_DNA[0]
        dna_strand_2 = list_DNA[1]
        if len(dna_strand_1) < len(dna_strand_2):
            for i in range(len(dna_strand_1)):
                if dna_strand_1[i] != dna_strand_2[i] and dna_strand_1[i] != "-" and dna_strand_2[i] != "-":
                    distance += 1
            for i in range(len(dna_strand_1), len(dna_strand_2)):
                distance += 1
        else:
            for i in range(len(dna_strand_2)):
                if dna_strand_1[i] != dna_strand_2[i] and dna_strand_1[i] != "-" and dna_strand_2[i] != "-":
                    distance += 1
            for i in range(len(dna_strand_2), len(dna_strand_1)):
                distance += 1
        list_of_integers.append(distance)
    return list_of_integers



