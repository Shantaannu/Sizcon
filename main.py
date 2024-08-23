# import pyttsx3
# import speech_recognition as sr
# import sys
# import datetime
# import os
# import wikipedia
# from requests import get
# import webbrowser  # Importing webbrowser module

# # Voice of Sizcon
# def speak(audio):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 140)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()

# # Convert text to voice
# def TakeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 1
        
#         try:
#             audio = r.listen(source, timeout=3, phrase_time_limit=7)
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"User Said: {query}")
#         except sr.WaitTimeoutError:
#             speak("Can I help you with anything else?")
#             return ""
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't understand that. Can you repeat?")
#             return ""
#         except sr.RequestError:
#             speak("Sorry, I can't connect to the recognition service.")
#             return ""
#         except Exception as e:
#             speak("Can you repeat that again!")
#             print(f"Error: {e}")
#             return ""
        
#         return query

# # Wish command; it will greet the user 
# def Wish():
#     hour = int(datetime.datetime.now().hour)
    
#     if hour >= 0 and hour < 12:
#         speak("Good Morning Sir")
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon Sir")
#     else:
#         speak("Good Evening Sir")
    
#     speak("How can I help you today?")
#  # Main Function   
# if __name__ == "__main__":
#     Wish()
    
#     while True:  # Loop to keep the assistant listening
#         # Storing user response in query
#         query = TakeCommand().lower()
        
#         # Open Notepad through voice
#         if "open notepad" in query:
#             npath = "C:\\Windows\\System32\\notepad.exe" 
#             os.startfile(npath)
        
#         # Find IP address
#         elif "ip address" in query:
#             ip = get('https://api.ipify.org').text
#             speak(f"Your IP address is {ip}")
        
#         # Wikipedia search
#         elif "wikipedia" in query:
#             speak("Searching Wikipedia")
#             query = query.replace("wikipedia", "")
#             result = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             speak(result)

#         # Open YouTube
#         elif "open youtube" in query:
#             webbrowser.open("https://www.youtube.com")

#         # Search anything on Google
#         elif "open google" in query:
#             speak("Sir, what should I search on Google?")
#             cm = TakeCommand().lower()  # Correct usage of TakeCommand
#             speak("Here are results of your query")
#             webbrowser.open(f"https://www.google.com/search?q={cm}")  # Construct the search URL
            
#         # Exit the program
#         elif "no thanks" in query:
#             speak("Have a nice day, sir.")
#             sys.exit()  # Correct exit call
        

import sys
import datetime
import os
import wikipedia
from requests import get
import webbrowser
from ENGINE.TTS.Stream_element import speak  # Import the speak function from Stream_element.py

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
            speak("Can I help you with anything else?", voice="Linda")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Can you repeat?", voice="Linda")
            return ""
        except sr.RequestError:
            speak("Sorry, I can't connect to the recognition service.", voice="Linda")
            return ""
        except Exception as e:
            speak("Can you repeat that again!", voice="Linda")
            print(f"Error: {e}")
            return ""
        
        return query

# Wish command; it will greet the user 
def Wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir", voice="Linda")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir", voice="Linda")
    else:
        speak("Good Evening Sir", voice="Linda")
    
    speak("How can I help you today?", voice="Linda")

# Main Function   
if __name__ == "__main__":
    Wish()
    
    while True:  # Loop to keep the assistant listening
        # Storing user response in query
        query = TakeCommand().lower()
        
        # Open Notepad through voice
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe" 
            os.startfile(npath)
        
        # Find IP address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}", voice="Linda")
        
        # Wikipedia search
        elif "wikipedia" in query:
            speak("Searching Wikipedia", voice="Linda")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia", voice="Linda")
            speak(result, voice="Linda")

        # Open YouTube
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        # Search anything on Google
        elif "open google" in query:
            speak("Sir, what should I search on Google?", voice="Linda")
            cm = TakeCommand().lower()
            speak("Here are the results of your query", voice="Linda")
            webbrowser.open(f"https://www.google.com/search?q={cm}")
            
        # Exit the program
        elif "no thanks" in query:
            speak("Have a nice day, sir.", voice="Linda")
            sys.exit()
        
