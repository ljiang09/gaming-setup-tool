# Run model on new images
# TODO: have user input to check if the model was right, and if so, add it to the current database

import joblib
from skimage.io import imread
from skimage.transform import resize


# load stored model and encoder
loaded_model = joblib.load('svc_model.pkl')

categories = ["keyboard", "mouse"]

def classify_image(img_data = None):
    new_img = None
    if img_data is None:
        # Load a local image for classification
        new_image_path = "unknown4.jpeg"
        new_img = imread(new_image_path)
        new_img = resize(new_img, (50, 50))
    else:
        new_img = resize(img_data, (50, 50))

    new_data = new_img.flatten().reshape(1, -1)  # Reshape to match the format used during training

    # Use the loaded model to predict the class of the new image
    predicted_class = loaded_model.predict(new_data)[0]
    predicted_category = categories[predicted_class]

    print(f"The predicted category for the new image is: {predicted_category}")
    return predicted_category
