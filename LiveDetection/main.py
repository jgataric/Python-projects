import tensorflow as tf
import numpy as np
import cv2

image_path = 'roompeople.jpeg'
saved_model_dir = 'models'

coco_classes = {
    1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus', 7: 'train',
    8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant', 13: 'stop sign',
    14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat', 18: 'dog', 19: 'horse', 
    20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear', 24: 'zebra', 25: 'giraffe', 
    27: 'backpack', 28: 'umbrella', 31: 'handbag', 32: 'tie', 33: 'suitcase', 
    34: 'frisbee', 35: 'skis', 36: 'snowboard', 37: 'sports ball', 38: 'kite', 
    39: 'baseball bat', 40: 'baseball glove', 41: 'skateboard', 42: 'surfboard', 
    43: 'tennis racket', 44: 'bottle', 46: 'wine glass', 47: 'cup', 48: 'fork', 
    49: 'knife', 50: 'spoon', 51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 
    55: 'orange', 56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 
    60: 'donut', 61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 
    65: 'bed', 67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 
    74: 'mouse', 75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 
    79: 'oven', 80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 
    85: 'clock', 86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 
    90: 'toothbrush'
}

colors = {i: np.random.uniform(0, 255, size=(3,)).astype(int).tolist() for i in coco_classes.keys()}

print("Loading model...")
detect_fn = tf.saved_model.load(saved_model_dir)
print("Model loaded successfully.")

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Unable to load image at {image_path}")
    exit()

input_tensor = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_tensor = np.expand_dims(input_tensor, axis=0)

print("Performing inference...")
detections = detect_fn(input_tensor)

num_detections = int(detections.pop('num_detections'))
detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}

boxes = detections['detection_boxes']
scores = detections['detection_scores']
classes = detections['detection_classes'].astype(np.int64)

height, width, _ = image.shape
bboxes = []
for box in boxes:
    ymin, xmin, ymax, xmax = box
    x, y, w, h = int(xmin * width), int(ymin * height), int((xmax - xmin) * width), int((ymax - ymin) * height)
    bboxes.append([x, y, w, h])

min_confidence = 0.41
nms_threshold = 0.2

indices = cv2.dnn.NMSBoxes(
    bboxes=bboxes, 
    scores=scores.tolist(), 
    score_threshold=min_confidence, 
    nms_threshold=nms_threshold
)

for i in indices.flatten():
    confidence = scores[i]
    if confidence > min_confidence:
        box = bboxes[i]
        class_id = classes[i]
        class_name = coco_classes.get(class_id, 'Unknown')

        color = colors.get(class_id, [0, 255, 0])

        start_point = (box[0], box[1])
        end_point = (box[0] + box[2], box[1] + box[3])
        cv2.rectangle(image, start_point, end_point, color, 2)
        
        label_y = max(box[1] - 10, 20)
        label = f"{class_name}: {confidence:.2f}"
        
        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
        text_x = box[0]
        text_y = label_y
        
        cv2.rectangle(image, (text_x, text_y - text_size[1] - 5), 
                      (text_x + text_size[0], text_y + 5), color, -1)
        
        cv2.putText(image, label, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
