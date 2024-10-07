import os
import cv2
import numpy as np
import tensorflow as tf
from tkinter import Tk, Button, Label, Entry, StringVar, Frame
from PIL import Image, ImageTk

os.chdir(r"C:\Users\jakov\Desktop\AI\DigitRecognizer")
model = tf.keras.models.load_model('handwritten_model.keras')

current_img = None
current_label = None
new_x_train = []
new_y_train = []
image_number = 1

def process_image():
    global current_img, current_label, img_label, image_number
    img_path = f"digits/digit{image_number}.png"
    
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    display_img = cv2.resize(img, (140, 140))
    img_for_prediction = cv2.resize(img, (28, 28))
    img_for_prediction = np.invert(np.array([img_for_prediction]))
    current_img = img_for_prediction
    
    prediction = model.predict(img_for_prediction.reshape(1, 28, 28))
    current_label = np.argmax(prediction)
    
    img_display = ImageTk.PhotoImage(image=Image.fromarray(display_img))
    img_label.config(image=img_display)
    img_label.image = img_display

    prediction_label.config(text=f"The number is probably a {current_label}")
    entry_var.set("")

def correct_prediction():
    new_x_train.append(current_img[0])
    new_y_train.append(current_label)
    next_image()

def incorrect_prediction():
    input_frame.pack()
    submit_button.pack()

def submit_correct_number():
    correct_number = int(entry_var.get())
    new_x_train.append(current_img[0])
    new_y_train.append(correct_number)
    input_frame.pack_forget()
    submit_button.pack_forget()
    next_image()

def next_image():
    global image_number
    image_number += 1
    if os.path.isfile(f"digits/digit{image_number}.png"):
        process_image()
    else:
        if len(new_x_train) > 0:
            retrain_model()
        root.quit()

def retrain_model():
    x_train_additional = np.array(new_x_train)
    y_train_additional = np.array(new_y_train)
    x_train_additional = x_train_additional.reshape(x_train_additional.shape[0], 28, 28)
    x_train_additional = tf.keras.utils.normalize(x_train_additional, axis=1)
    model.fit(x_train_additional, y_train_additional, epochs=3)
    model.save('handwritten_model.keras')


root = Tk()
root.title("Digit Recognition")

root.geometry("300x350")


img_label = Label(root)
img_label.pack()


prediction_label = Label(root, text="")
prediction_label.pack()


correct_button = Button(root, text="Correct", command=correct_prediction)
correct_button.pack(side="left")

incorrect_button = Button(root, text="Incorrect", command=incorrect_prediction)
incorrect_button.pack(side="right")

input_frame = Frame(root)
entry_var = StringVar()
entry_label = Label(input_frame, text="Enter the correct number:")
entry_label.pack(side="left")
entry_field = Entry(input_frame, textvariable=entry_var)
entry_field.pack(side="left")

submit_button = Button(root, text="Submit", command=submit_correct_number)

process_image()

root.mainloop()
