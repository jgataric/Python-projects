# Object Detection
This project performs object detection on an image using the pre-trained MobileNet-SSD model. The code uses OpenCV's deep learning module (cv2.dnn) to load the model and detect objects in the input image.

## How It Works
#### Model 
The MobileNet-SSD model is used for object detection. This is a lightweight deep learning model optimized for mobile devices, and it is capable of detecting 20 different classes of objects.
#### Object Detection
The model processes the input image and draws bounding boxes around detected objects, along with confidence scores.
#### Classes Detected
The model can detect the following objects:
Aeroplane, Bicycle, Bird, Boat, Bottle, Bus, Car, Cat, Chair, Cow, Dining Table, Dog, Horse, Motorbike, Person, Potted Plant, Sheep, Sofa, Train, TV Monitor.
#### Files
roompeople.jpeg: The image file that will be used for object detection.
models/MobileNetSSD_deploy.prototxt: The prototxt file which defines the network architecture.
models/MobileNetSSD_deploy.caffemodel: The pre-trained model weights file.

## How to Run
#### Set Up the Environment:
Install the required libraries, mainly OpenCV, using the following command in terminal:
pip install opencv-python
#### Prepare the Model Files:
Download the MobileNetSSD_deploy.prototxt and MobileNetSSD_deploy.caffemodel files and place them in the models/ folder.
#### Run the Code:
Run the script in your terminal:
python main.py

The program will load the image and detect objects, drawing bounding boxes around the detected objects and displaying them on the screen.

## Key Parameters
min_confidence: This variable controls the confidence threshold for displaying detected objects. Objects with a confidence score below this threshold will not be shown.

Default value: 0.2 (20%).
Classes: The classes array defines the list of 20 objects that the model is trained to detect, such as "person", "car", "dog", etc.

## Output
The output is a window displaying the image with bounding boxes and labels for each detected object. Each box is color-coded based on the object class.