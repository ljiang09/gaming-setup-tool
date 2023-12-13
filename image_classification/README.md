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
