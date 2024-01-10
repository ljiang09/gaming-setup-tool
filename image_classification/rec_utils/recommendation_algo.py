# name, price, link, img url, colors
# eventually add tags and related items (like if there's a 75% of the same keyboard)

import pandas as pd
import cv2
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance
from PIL import Image
# eventually add tags


THRESHOLD = 50  # how close of a color is acceptable


def extract_colors(image_path, num_colors):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Get the dominant colors
    colors = kmeans.cluster_centers_.astype(int)

    return colors


# TODO: this function desperately needs to be refactored
def recommend_similar_images(target_colors, database, num_imgs=3):
    '''
    Recommends images from the database based on the target colors.
    Doesn't provide the actual image, but the index of the image

    Args:
    target_colors: array of arrays, with each subarray representing
        an rgb color that we want to recommend based on
    database: array of dominant colors for each image in the existing
        database
    num_imgs: int representing the number of images to be recommended

    Returns:
    An array of up to `num_imgs` ints representing the indices of the
    recommended images in the provided database
    '''
    distances = {}
    for i, arr in enumerate(database):
        for color in arr:
            for targ_col in target_colors:
                dist = distance.euclidean(targ_col, color)
                if distances.get(dist):
                    distances[dist].append(i)
                else:
                    distances[dist] = [i]
    
    distance_vals = list(distances.keys())
    distance_vals.sort()  # sort closest distance to furthest

    # TODO: refactor this to use numpy
    # Also this mayyyy be wrong but i cannot think rn
    x = [0] * len(database)
    for i in range(num_imgs):  # iterate through closest colors
        for index in distances[distance_vals[i]]:
            x[index] += 1

    return_vals = []
    for i in range(num_imgs):
        max_val_idx = x.index(max(x))
        if max(x) > 0:
            return_vals.append(max_val_idx)
            x[max_val_idx] = 0
        else:
            break

    return return_vals


def rec_by_colors(colors):
    '''
    Gets a list of 3 keyboard and 3 mice based purely on color.

    Args:
    colors: an array of integer tuples representing rgb values like so:
        (255, 255, 255)
    
    Returns:
    An array of data for 3 mice and 3 keyboards. This data is of the
    form of a subarray
    '''
    pass


# Example usage
image_paths = ["unknown1.jpeg", "unknown2.jpeg", "unknown3.jpeg"]
database = [extract_colors(path, 6) for path in image_paths]

# User selects a set of colors
target_colors = np.array([[255, 0, 0], [0, 255, 0]])

# Recommend similar images
similar_images = recommend_similar_images(target_colors, database)

print(similar_images)

# Print recommended image paths
for index in similar_images:
    print(image_paths[index])



# TODO: maybe the best move is to write a classification
# algorithm for colors, and when putting a new image through,
# grab the nearest neighbors. images will be named with their ID, which
# can be used to grab additional info from the csv

