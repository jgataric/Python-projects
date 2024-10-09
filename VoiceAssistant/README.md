# Jarvis Voice Assistant
This project is a voice-controlled assistant built using tkinter, speech_recognition, and pyttsx3 for speech synthesis. The assistant can either be connected to OpenAI's GPT-4 for dynamic responses, or you can configure it to respond to custom-defined intents using the neuralintents library.

## How It Works
OpenAI GPT-4 Mode: By default, the assistant connects to OpenAI's GPT-4 model, allowing it to respond dynamically to voice queries.
Custom Intents Mode: Alternatively, you can use the pre-defined intents in intents.json for handling specific commands like greetings or creating files.
Wake Word Detection: The assistant listens for the wake word ("Hey Jarvis") before accepting any commands.

## Usage
### Option 1: OpenAI GPT-4 Mode
Set up your OpenAI API key:
In main.py, replace '*Your OpenAi API key*' with your actual OpenAI API key.
Run the Assistant:
Simply run the main.py file:
open terminal and type in following:
python main.py
The assistant will connect to GPT-4 via OpenAI's API and provide dynamic responses to any voice command after detecting the wake word "Hey Jarvis".

### Option 2: Custom Intents Mode
Edit the intents.json File:
If you'd prefer to use your own custom responses and commands, edit the intents.json file to match the intents you want the assistant to handle.
The assistant will respond based on the patterns and responses defined in intents.json file.

## Run the Assistant:
open terminal and type in following:
python withIntents.py
The assistant will listen for commands based on the defined intents in intents.json.

### Interacting with Jarvis
Once Jarvis detects the wake word "Hey Jarvis", it will listen for further commands.
In GPT-4 Mode, Jarvis will respond dynamically to any command.
In Custom Intents Mode, you can say:
"Hi" (for a greeting response).
"What is your name?" (to get the assistant's name).
"Create a file" (to trigger the file creation).
Stopping the Assistant
Say "stop" to terminate the assistant.

### Intents Configuration

Greeting:
Patterns: "Hi", "Hey", "What's up", "Hey how are you doing?"
Responses: "Hey Sir!", "What can I do for you?"

Name:
Patterns: "What is your name?", "What should I call you?"
Responses: "My name is Jarvis", "You can call me Jarvis."

File:
Patterns: "Create a file", "Create a new file."
Response: Creates a file named somefile.txt and writes "Hello, I did what you asked" into it.
