"""
This program contains one programming problem named Zookeeper

Author: Nguyen Chinh Quan
Time spent: 60 minutes
"""
def tabulate_animals(filename):
    """
    Description: Reads a list of animal names from a file, and returns a tally of each kind of animal in the zoo.
    Parameter:
        filename: The name of a file containing the complete names of the animals in the zoo
    Return: A list of strings in the format "species count" for each unique species in the zoo, sorted alphabetically.
    """
    try:
        with open(filename,'r') as input_file:
            text = input_file.read().splitlines()
            if text == []:
                return []
            else:
                list_animals = []
                for i in range(len(text)):
                    text[i] = text[i].lower()
                    lists_of_text = text[i].split()
                    list_animals.append(lists_of_text[len(lists_of_text)-1])
                list_animals.sort()
                i = 0
                list_tally_animal = []
                while i+1 < len(list_animals):
                    number_of_animal = 1
                    for j in range(i+1,len(list_animals)):
                        if list_animals[i] == list_animals[j]:
                            number_of_animal += 1
                    if number_of_animal > 1:
                        i += number_of_animal - 1
                        list_tally_animal.append(list_animals[i]+str(' ')+str(number_of_animal))
                    else:
                        i += 1
                list_tally_animal.sort()
                return list_tally_animal
    except FileNotFoundError:
        return []

