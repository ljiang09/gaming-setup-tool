from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster


# TODO: the goal is to be identify 1-5 main colors
# only return a color if 20% of the image has it?
# need to make sure the colors aren't super similar though.. a filtering mechanism perslaps

# Currently, we allow image = None for easy testing of the function
from PIL import Image
import colorspacious as cs

# pil_img should be a PIL Image object
def get_dominant_color(pil_img):
    img = pil_img.copy()
    img = img.convert("RGBA")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    return dominant_color
