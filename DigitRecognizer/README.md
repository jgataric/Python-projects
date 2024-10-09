Digit Recognizer
This project is a digit recognizer application that uses a TensorFlow model to predict handwritten digits. The application loads images of digits, processes them, and makes predictions using a pre-trained neural network. If the prediction is incorrect, the user can provide the correct label, and the model can be retrained with new data.

Project Structure
main.py: The main script that runs the digit recognition GUI application using Tkinter.
digits/: A folder containing images of handwritten digits (1-9) in .png format. These images are used for testing and correcting the model.
handwritten_model.keras: The pre-trained TensorFlow model that predicts the digits.

Features
Displays an image of a handwritten digit and predicts the number.
Allows user feedback for incorrect predictions and updates the model with the corrected values.
Retrains the model if there are any corrections.

Install the required Python packages:
bash
pip install tensorflow opencv-python numpy pillow
Make sure the digits/ folder exists in the project root, containing digit images in .png format.

Place the pre-trained model (handwritten_model.keras) in the project root or train your own model if you have the data.

Run the application:
open terminal and run following:
python main.py
The application will display the images from the digits/ folder one by one, predicting the digit in the image. You can either accept or correct the prediction, and the model will be updated with your feedback if necessary.

How It Works
Image Processing: The program loads the images from the digits/ folder, converts them to grayscale, and resizes them to 28x28 pixels (the input size for the model).
Prediction: The loaded model makes a prediction for each digit, which is displayed on the GUI.
Correction: If the prediction is wrong, the user can input the correct label, which is used to retrain the model with new examples.
Model Retraining: When there are enough new samples, the model is retrained for a few epochs and saved again.
Retraining the Model
If any prediction is corrected, the program automatically adds the new data to the training set and retrains the model for 3 epochs. The updated model is saved as handwritten_model.keras.