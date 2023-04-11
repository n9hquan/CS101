"""
This program

Author:
Time spent:
"""
from csc121.image import get_channel, write_jpg
from PIL import Image
def gradient_blend():
    redRick = get_channel('rick.jpg','red')
    blueRick = get_channel('rick.jpg','blue')
    greenRick = get_channel('rick.jpg','green')
    redIlsa = get_channel('ilsa.jpg','red')
    blueIlsa = get_channel('ilsa.jpg','blue')
    greenIlsa = get_channel('ilsa.jpg','green')
    heightIlsa = len(redIlsa)
    widthIlsa = len(redIlsa[0])
    for r in range(heightIlsa):
        for c in range(widthIlsa):
            Br = r/heightIlsa
            Bc = c/widthIlsa
            B = max(Br, Bc)
            Rb = int(B * redRick[r][c] + (1 - B) * redIlsa[r][c])
            Gb = int(B * greenRick[r][c] + (1 - B) * greenIlsa[r][c])
            Bb = int(B * blueRick[r][c] + (1 - B) * blueIlsa[r][c])
            redRick[r][c] = Rb
            greenRick[r][c] = Gb
            blueRick[r][c] = Bb
    write_jpg(redRick, greenRick, blueRick, 'blended.jpg')
#gradient_blend()
def mirror():
    image = input("Enter your image: ")
    red = get_channel(image, 'red')
    blue = get_channel(image, 'blue')
    green = get_channel(image, 'green')
    height = len(red)
    width = len(red[0])
    t = 0
    for row in range(height):
        for col in range(width - 1, -1, -1):
            red[row][col] = red[row][t]
            blue[row][col] = blue[row][t]
            green[row][col] = green[row][t]
            if col == width // 2:
                t = 0
                break
            t = t + 1
    write_jpg(red, green, blue, 'mirrored.jpg')
#mirror()


def pencil_sketch():
    image = input("Enter the name of your picture: ")
    red = get_channel(image, 'red')
    blue = get_channel(image, 'blue')
    green = get_channel(image, 'green')
    height = len(red)
    width = len(red[0])
    for row in range(height-1):
        for col in range(width-1):
                grayscale_1 = (red[row][col] + blue[row][col] + green[row][col])//3
                grayscale_2 = (red[row][col+1] + blue[row][col+1] + green[row][col+1])//3
                grayscale_3 = (red[row+1][col] + blue[row+1][col] + green[row+1][col])//3
                if abs(grayscale_1 - grayscale_2) > 8 and abs(grayscale_1 - grayscale_3) > 8:
                    red[row][col] = 0
                    blue[row][col] = 0
                    green[row][col] = 0
                else:
                    red[row][col] = 255
                    blue[row][col] = 255
                    green[row][col] = 255
    write_jpg(red, green, blue, 'sketched.jpg')
#pencil_sketch()

def tile_image():
    image = input("Enter the name of your picture: ")
    image1 = int(image)
    red = get_channel(image, 'red')
    blue = get_channel(image, 'blue')
    green = get_channel(image, 'green')
    height = len(red)
    width = len(red[0])
    t=0
    for row in range(height):
        for col in range(width - 1, -1, -1):
            image1[row][col] = image1[row][t]
        if col == width // 2:
            t = 0
            break
        t = t + 1
        write_jpg(red, green, blue, 'sliding_tile.jpg')
tile_image()