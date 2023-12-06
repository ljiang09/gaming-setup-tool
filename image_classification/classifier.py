import os
from skimage.io import imread
from skimage.transform import resize
import numpy as np


# prepare data
input_dir = "/Users/lilyjiang/Documents/GitHub/gaming-setup-tool/image_classification/data"
categories = ["keyboard", "mouse"]

data = []
labels = []

for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        if file == ".DS_Store":
            continue
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (50, 50))
        data.append(img.flatten())  # flatten the image into vector
        labels.append(category_idx)

data = np.asarray(data, dtype=object)
labels = np.asarray(labels, dtype=object)

# train/test split

# train classifier

# test performance
