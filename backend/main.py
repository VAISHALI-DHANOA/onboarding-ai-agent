from typing import Union
from fastapi import FastAPI
# Importing required libraries
import speech_recognition as sr
from IPython.display import display, Markdown
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Custom-Header"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen for the wake word "Hey Dashboard"
def listen_for_command():
    try:
        # Use the microphone as source
        with sr.Microphone() as source:
            display(Markdown("### Listening for 'Hey Dashboard'..."))
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio)
            
            if "hey dashboard" in command.lower():
                display(Markdown("### Command recognized: Hey Dashboard"))
                handle_interaction()
                # Add further actions here
            else:
                display(Markdown(f"### Heard: {command}. Waiting for 'Hey Dashboard'."))

    except sr.UnknownValueError:
        display(Markdown("### Could not understand the audio. Please try again."))
    except sr.RequestError as e:
        display(Markdown(f"### Error with the speech recognition service: {e}"))

# # Continuously listen for the command while running the notebook
# while True:
#     listen_for_command()

@app.get("/handle_interaction/{prompt}")
def handle_interaction(prompt:str):
    
    #recognized_text
    # recognized_text = "Can you filter the graph?"
    recognized_text = prompt

    # Prompt for OpenAI API
    prompt = f"Classify the following text into one of these categories: 'explain visualization,' 'explain interaction,' 'explain insight,' or 'insight usage.'\n\nText: {recognized_text}\n\nCategory:"
    client = OpenAI(api_key="")
    # OpenAI API Call
    try:
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "developer", "content": "You are a helpful assistant that classifies text."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)
        category = response.choices[0].message.content.strip()
        print(f"Predicted category: {category}")
        return category


    except Exception as e:
        return f"Error: {str(e)}"
    

