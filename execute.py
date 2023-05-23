import tensorflow as tf
import numpy as np
import os

# Load model from file "model_nsfw_sfw.h5"
model = tf.keras.models.load_model('model_nsfw_sfw.h5')

for file in os.listdir('execute'):

    # Path of the image to classify
    image_path = f"execute/{file}"

    # Load image and convert it to array
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(64, 64))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    # Predict
    prediction = model.predict(image)[0][0]

    # Print result
    if prediction > 0.5:
        print(f"The image {file} is classified as SFW (safe for work). Prediction : {prediction}")
    else:
        print(f"The image {file} is classified as NSFW (not safe for work). Prediction : {prediction}")
