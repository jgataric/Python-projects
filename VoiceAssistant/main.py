import sys
import threading
import tkinter as tk
import speech_recognition
import pyttsx3 as tts
import openai
import json

openai.api_key = '***Your OpenAi API key***'

class Assistant:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        self.messages = []

        self.root = tk.Tk()
        self.root.title("GPT-4 Voice Assistant")
        self.label = tk.Label(text="Jarvis", font=("Arial", 120, "bold"))
        self.label.pack()

        assistant_thread = threading.Thread(target=self.run_assistant)
        assistant_thread.daemon = True
        assistant_thread.start()

        self.root.mainloop()

    def ask_gpt(self, prompt):
        self.messages.append({'role': 'user', 'content': prompt})
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=self.messages,
            )

            response_message = response.choices[0].message.content.strip()

            self.speaker.say(response_message)
            self.speaker.runAndWait()

            self.messages.append({
                'role': 'assistant',
                'content': response_message
            })

        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            self.speaker.say("Sorry, I couldn't get a response from GPT-4.")
            self.speaker.runAndWait()

    def listen_for_wake_word(self, mic):
        while True:
            try:
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio).lower()
                if "hey jarvis" in text:
                    return True
            except speech_recognition.UnknownValueError:
                continue

    def run_assistant(self):
        with speech_recognition.Microphone() as mic:
            while True:
                if self.listen_for_wake_word(mic):
                    self.label.config(fg="red")

                    try:
                        audio = self.recognizer.listen(mic)
                        question = self.recognizer.recognize_google(audio).lower()

                        if question == "stop":
                            self.speaker.say("Goodbye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.quit()
                            sys.exit()

                        else:
                            self.ask_gpt(question)

                        self.label.config(fg="black")

                    except speech_recognition.UnknownValueError:
                        self.label.config(fg="black")
                        continue

Assistant()
