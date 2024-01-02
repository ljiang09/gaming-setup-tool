Goal: given 50 (labeled) images of keyboards and 50 images of computer mice,
classify new images with 70% accuracy

Stretch: be able to pinpoint a keyboard and a mouse in an image that has both
objects.

Model: https://www.youtube.com/watch?v=UuNGmhLpbCI

## How to run:

1. Store training image data in `image_classification/data`. Keyboard images
   should be in `image_classification/data/keyboards`, and mouse images should
   be in `image_classification/data/mouse`. Make sure they are in .jpg or .jpeg
   format
2. Run `image_classification/classifier_model.py` to save the model locally
3. Test a new image on the model using
   `image_classification/new_img_classifier.py`. Save the new image locally (jpg
   or jpeg) and change `new_image_path` to be the path of your new image

## Next steps:

- Make color classifying algorithm - extract main colors from the uploaded image
- Make recommendation algorithm
- Make algo to identify specific keyboards or mice in the photo, and recommend
  those in the algorithm

With all of these, we can try to provide the user with a list that includes the
exact keyboard/mouse shown in the photo (if it exists), and then some actual
recommendations
