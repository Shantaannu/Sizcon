import sys
import datetime
import os
import wikipedia
from requests import get
import webbrowser
import psutil #Manages Processes
from ENGINE.TTS.Stream_element import speak  # Import the speak function from Stream_element.py
import tkinter as tk
from tkinter import messagebox
from groq import Groq  # Import the Groq client

# Convert text to voice using the Stream_element function
def TakeCommand():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=7)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
        except sr.WaitTimeoutError:
            speak("Can I help you with anything else?", voice="Linda", emotion="neutral")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Can you repeat?", voice="Linda", emotion="confused")
            return ""
        except sr.RequestError:
            speak("Sorry, I can't connect to the recognition service.", voice="Linda", emotion="neutral")
            return ""
        except Exception as e:
            speak("Can you repeat that again!", voice="Linda", emotion="frustrated")
            print(f"Error: {e}")
            return ""
        
        return query

# Wish command; it will greet the user 
def Wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning ", voice="Linda", emotion="happy")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ", voice="Linda", emotion="happy")
    else:
        speak("Good Evening ", voice="Linda", emotion="happy")
    
    speak("How can I help you today?", voice="Linda", emotion="happy")

# Function to close an application by name
def close_application(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in proc.info['name'].lower():
            proc.terminate()
            speak(f"Closing {app_name}.", voice="Linda", emotion="neutral")
            return True
    speak(f"Could not find {app_name}.", voice="Linda", emotion="neutral")
    return False

# AI-powered response using Groq API
def AIResponse(query):
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=1,
        max_tokens=100,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    response_text = ""
    for chunk in completion:
        chunk_content = chunk.choices[0].delta.content or ""
        response_text += chunk_content

    # Now that the entire response is generated, speak it out
    print(response_text)  # Print the response for debugging/visual purposes
    speak(response_text, voice="Linda", emotion="neutral")

# Main Function   
if __name__ == "__main__":

    Wish()  # Greet the user
    
    while True:  # Loop to keep the assistant listening
        # Storing user response in query
        query = TakeCommand().lower()
        
        # Open Notepad through voice
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe" 
            os.startfile(npath)
            speak("Opening Notepad.", voice="Linda", emotion="neutral")
        
        # Close Notepad through voice
        elif "close notepad" in query:
            close_application("notepad.exe")
        
        # Find IP address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}", voice="Linda", emotion="neutral")
        
        # Wikipedia search
        elif "wikipedia" in query:
            speak("Searching Wikipedia", voice="Linda", emotion="neutral")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia", voice="Linda", emotion="neutral")
            speak(result, voice="Linda", emotion="neutral")

        # Open YouTube
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.", voice="Linda", emotion="neutral")

        # Close YouTube through voice (though this is tricky, it usually involves closing the browser window/tab)
        elif "close youtube" in query:
            speak("Please close YouTube manually.", voice="Linda", emotion="neutral")
        
        # Search anything on Google
        elif "open google" in query:
            speak("Sir, what should I search on Google?", voice="Linda", emotion="neutral")
            cm = TakeCommand().lower()
            speak("Here are the results of your query", voice="Linda", emotion="neutral")
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        # Exit the program based on user query
        elif "shutdown" in query or "close" in query or "exit" in query:
            speak("Shutting down. Have a nice day, sir.", voice="Linda", emotion="neutral")
            sys.exit()
        
        elif "no thanks" in query or "exit" in query or "Bye" in query:
            speak("Have a nice day. Sizcon.", voice="Linda", emotion="neutral")
            sys.exit()

        # If the query doesn't match any command, use the AI to generate a response
        else:
            AIResponse(query)
