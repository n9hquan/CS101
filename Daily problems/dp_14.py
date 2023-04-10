"""
This program contains two programming problems named Simon Says and Colorful Tiles.

Author: Nguyen Chinh Quan
Time spent: 35 minutes
"""
def simon_says():
    """
    This function prints out the instructions that were obeyed from a list of instructions by Simon.
    """
    list_action = []
    list_instructions = input("Enter list of instructions:")
    list_instructions = eval(list_instructions)
    for i in list_instructions:
        temp = i.split()
        if i == "":
            continue
        if temp[0] == "Simon" and temp[1] == "says":
            keywords_split = i.split("Simon says ")
            list_action += [keywords_split[1]]
    print("Instructions to obey:",list_action)
#simon_says()
def min_tiles_to_change():
    """
    This function prints the minimum number of tiles that Phyllida must change based on the input colors of the tiles.
    """
    tile_colors = input("Enter the tile colors:")
    tile_color_position = 0
    number_tiles_change = 0
    while tile_color_position<len(tile_colors)-1:
        if tile_colors[tile_color_position]!=tile_colors[tile_color_position+1]:
            tile_color_position +=1
        else:
            number_tiles_change +=1
            tile_color_position +=2
    print("Number of tiles to change:",number_tiles_change)
#min_tiles_to_change()