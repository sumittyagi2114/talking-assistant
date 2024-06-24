import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import openai
from gtts import gTTS
import pygame
import os
from music import music_here  # Import the music dictionary

# Initialize recognizer and text-to-speech engine
voice_recognizer = sr.Recognizer()
speech_engine = pyttsx3.init()
# Replace with your API keys
news_api_key = "NEWSAPI_KEY"
openai.api_key = "API_KEY"

def speak_with_pyttsx3(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

def speak_with_gtts(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load and play the MP3 file
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def get_openai_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named sumit skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

def handle_command(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = music_here.get(song, f"https://www.youtube.com/results?search_query={song}")
        webbrowser.open(link)
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak_with_gtts(article['title'])
    else:
        response = get_openai_response(command)
        speak_with_gtts(response)

if __name__ == "__main__":
    speak_with_gtts("Initializing Sumit...")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = voice_recognizer.listen(source, timeout=2, phrase_time_limit=1)
            wake_word = voice_recognizer.recognize_google(audio)
            if wake_word.lower() == "sumit":
                speak_with_gtts("Yes")
                with sr.Microphone() as source:
                    print("sumit active. Listening for command...")
                    audio = voice_recognizer.listen(source)
                    user_command = voice_recognizer.recognize_google(audio)
                    handle_command(user_command)
        except Exception as e:
            print(f"Error: {e}")
