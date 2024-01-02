'''
Functions to identify the dominant color(s) of an image.
'''

from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import colorspacious as cs


# TODO: the goal is to be identify 1-5 main colors
# only return a color if 20% of the image has it?
# need to make sure the colors aren't super similar though.. a filtering mechanism perslaps


def get_dominant_color(pil_img):
    '''
    Get the singular most dominant color for an image. This is the
    legacy algorithm.

    Args:
    pil_img: a PIL Image object

    Returns:
    A tuple of 3 integers representing an RGB color
    '''
    img = pil_img.copy()
    img = img.convert("RGBA")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    return dominant_color




WIDTH = 100
HEIGHT = 100
THRESHOLD_DISTANCE = 150

# new algorithm that can identify multiple dominant colors
# only problem is that it likes to focus on the background colors
def identify_colors(image=None):
    '''
    Get the 6 most dominant colors for an image.

    Args:
    image: a PIL Image object

    Returns:
    An array of 6 colors, each represented by a tuple of 3 integers
    '''
    if image is None:
        filename = "./unknown1.jpeg"
        image = Image.open(filename)
    image = image.resize((WIDTH, HEIGHT), resample = 0)
    # Get colors from image object
    pixels = image.getcolors(WIDTH * HEIGHT)

    # Sort them by count number (first element of tuple)
    sorted_pixels = sorted(pixels, key=lambda t: t[0], reverse=True)
    colors = [sorted_pixels[0][1]]

    # Filter out colors that are too similar to the dominant color
    # iterate across all pixels, find the first one that isn't within the threshold distance
    for pixel in sorted_pixels:
        curr_color = pixel[1]
        meets_threshold = True
        for color in colors:
            sum = abs(curr_color[0] - color[0]) + abs(curr_color[1] - color[1]) + abs(curr_color[2] - color[2])
            if sum <= THRESHOLD_DISTANCE:
                meets_threshold = False
                break

        if meets_threshold:
            # pixel is appropriately far away from the original color
            colors.append(pixel[1])
            if len(colors) == 6: break
        else:
            continue

    return colors

