import sys
import threading
import tkinter as tk
import speech_recognition
import pyttsx3 as tts
from neuralintents import BasicAssistant

class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        self.assistant = BasicAssistant("intents.json", method_mappings={"file": self.create_file})
        self.assistant.fit_model()

        self.root = tk.Tk()
        self.root.title("Jarvis Voice Assistant")
        self.label = tk.Label(text="Jarvis", font=("Arial", 120, "bold"))
        self.label.pack()

        assistant_thread = threading.Thread(target=self.run_assistant)
        assistant_thread.daemon = True
        assistant_thread.start()

        self.root.mainloop()

    def create_file(self):
        with open("somefile.txt", "w") as f:
            f.write("Hello, I did what you asked")

    def listen_for_wake_word(self, mic):
        print("Listening for wake word...")
        while True:
            try:
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio).lower()
                if "hey jarvis" in text:
                    print("Wake word detected!")
                    return True
            except speech_recognition.UnknownValueError:
                continue

    def run_assistant(self):
        with speech_recognition.Microphone() as mic:
            while True:
                if self.listen_for_wake_word(mic):
                    self.label.config(fg="red")
                    print("Awaiting further commands...")

                    try:
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio).lower()
                        print(f"Command: {text}")

                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.quit()
                            sys.exit()

                        else:
                            if text is not None:
                                response = self.assistant.process_input(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()

                        self.label.config(fg="black")

                    except speech_recognition.UnknownValueError:
                        print("Sorry, I did not understand.")
                        self.label.config(fg="black")
                        continue

Assistant()
