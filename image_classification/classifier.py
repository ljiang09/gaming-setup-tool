# https://www.youtube.com/watch?v=UuNGmhLpbCI

import os
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


# prepare data
input_dir = "/Users/lilyjiang/Documents/GitHub/gaming-setup-tool/image_classification/data"
categories = ["keyboard", "mouse"]

data = []
labels = []

for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        if file == ".DS_Store":
            continue
        # if (file[len(file) - 3:] == "jpg"):
        # if (file[len(file) - 4:] == "jpeg"):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (50, 50))
        data.append(img.flatten())  # flatten the image into vector
        labels.append(category_idx)

data = np.asarray(data, dtype=object)
labels = np.asarray(labels, dtype=object)

label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

# train/test split
x_train, x_test, y_train, y_test = train_test_split(data, labels_encoded, test_size=0.2, shuffle=True, stratify=labels)

# train classifier
classifier = SVC()  # change algo as desired
parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

# test performance
best_estimator = grid_search.best_estimator_
y_prediction = best_estimator.predict(x_test)

print("*****y_prediction", y_prediction)
print("*****y_test", y_test)

score = accuracy_score(y_prediction, y_test)

print("*****", score * 100, '% of samples were correctly classified')
