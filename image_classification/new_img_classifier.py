# Run model on new images
# TODO: have user input to check if the model was right, and if so, add it to the current database

import joblib
from skimage.io import imread
from skimage.transform import resize


# load stored model and encoder
loaded_model = joblib.load('image_classification/svc_model.pkl')
label_encoder = joblib.load('image_classification/label_encoder.pkl')

categories = ["keyboard", "mouse"]

# Load a new image for classification
new_image_path = "image_classification/unknown4.jpeg"
new_img = imread(new_image_path)
new_img = resize(new_img, (50, 50))
new_data = new_img.flatten().reshape(1, -1)  # Reshape to match the format used during training

# Use the loaded model to predict the class of the new image
predicted_class = loaded_model.predict(new_data)[0]
predicted_category = categories[predicted_class]

print(f"The predicted category for the new image is: {predicted_category}")
