"""
This function prints out the total number of trophies that are visible to the viewer based on the input of trophy heights

Author: Nguyen Chinh Quan
Time spent: 15 minutes
"""
def count_visible():
    list_trophies_heights = input("Enter trophy heights:")
    list_trophies_heights = eval(list_trophies_heights)
    numbers_of_visible_trophies = 1
    mark_trophy = list_trophies_heights[0]
    for i in range(1,len(list_trophies_heights)):
        if list_trophies_heights[i] > mark_trophy:
            numbers_of_visible_trophies += 1
            mark_trophy = list_trophies_heights[i]
    print("Number of visible trophies:",numbers_of_visible_trophies)
#count_visible()