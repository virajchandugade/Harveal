from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Replace 'hmodel.h5' with the actual path to your saved model file
mod='mymod.h5'
loaded_model = load_model(mod)

image_path = 'dataset\mosaicimg.jpeg'  # Replace with the actual path

# Load and preprocess the new image
new_image = image.load_img(image_path, target_size=(64, 64))
new_image_array = image.img_to_array(new_image)
new_image_array = np.expand_dims(new_image_array, axis=0)
new_image_array /= 255.0  # Rescale to match the training data normalization

# Make a prediction
prediction = loaded_model.predict(new_image_array)

# Convert the prediction to a human-readable label
class_labels = ['healthy_leaf', 'target_spot', 'mosaic_virus']
predicted_class_index = np.argmax(prediction)
predicted_class = class_labels[predicted_class_index]

# Display the results
print(f"The predicted class is: {predicted_class}")
print(f"Confidence scores: {prediction.squeeze()}")
