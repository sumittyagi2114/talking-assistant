***************************************************************
*                                                             *
*                           Sumit Tyagi                       *
*                                                             *
*              Voice Assistant Using OpenAI and Pygame        *
*                                                             *
***************************************************************

This project implements a voice assistant named Sumit that can perform various tasks such as opening websites, playing music, and fetching news headlines. The assistant uses OpenAI's GPT-3.5 model for handling general queries and responses.

**Main Script: main.py**

1. **Imports and Initializations:**
   - Essential libraries are imported, including `speech_recognition`, `webbrowser`, `pyttsx3`, `requests`, `openai`, `gtts`, `pygame`, and `os`.
   - The `music_here` dictionary from `music.py` is imported.
   - Initializations for the speech recognizer (`voice_recognizer`) and text-to-speech engine (`speech_engine`) are done.
   - API keys for OpenAI and News API (commented out) are set.

2. **Text-to-Speech Functions:**
   - `speak_with_pyttsx3(text)`: Uses the `pyttsx3` library to convert text to speech.
   - `speak_with_gtts(text)`: Uses the `gTTS` library to convert text to speech and plays it using the `pygame` mixer.

3. **OpenAI Response Function:**
   - `get_openai_response(user_input)`: Sends the user's input to the OpenAI API and returns the response.

4. **Command Handling Function:**
   - `handle_command(command)`: Processes the user's command to perform actions like opening websites, playing music from the `music_here` dictionary, fetching news headlines, or getting a response from OpenAI.

5. **Main Loop:**
   - The assistant initializes with a welcome message.
   - The program continuously listens for the wake word "Sumit."
   - Upon detecting the wake word, it listens for a command and processes it using the `handle_command` function.
   - Errors are caught and printed to the console.

**Music Script: music.py**

1. **Music Dictionary:**
   - `music_here`: A dictionary containing song names as keys and their corresponding YouTube links as values.
   - Example:
     ```python
     music_here = {
         "boldonazara": "https://www.youtube.com/watch?v=EpEraRui1pc",
         "mockingbird": "https://www.youtube.com/watch?v=S9bCLPwzSC0",
         "enemy": "https://www.youtube.com/watch?v=D9G1VOjN_84"
     }
     ``'
     you add more songs if you want

**Usage:**

1. Ensure all necessary libraries are installed:
   ```bash
   pip install speechrecognition pyttsx3 requests openai gtts pygame
