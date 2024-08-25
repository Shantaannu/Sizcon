from typing import Union
import requests
import playsound
import os

def generate_audio(message: str, voice: str = "Brian", emotion: str = "neutral", pitch: int = 0, speed: int = 1, volume: int = 1):
    """
    Text to speech using StreamElements API

    Parameters:
        message (str): The text to convert to speech
        voice (str): The voice to use for speech synthesis. Default is "Brian".
        emotion (str): The emotion to apply to the voice. Default is "neutral".
        pitch (int): The pitch adjustment for the voice.
        speed (int): The speed of the voice.
        volume (int): The volume level of the voice.

    Returns:
        result (Union[bytes, None]): Audio content or None in failure
    """
    # Base URL for provider API
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}&emotion={emotion}&pitch={pitch}&speed={speed}&volume={volume}"
    
    # Request headers
    headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    # Try to send request or return None on failure
    try:
        result = requests.get(url=url, headers=headers)
        if result.status_code == 200:
            return result.content
        else:
            print(f"Failed to generate audio: {result.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = ".mp3", emotion: str = "neutral", pitch: int = 0, speed: int = 1, volume: int = 1) -> Union[None, str]:
    """
    Save the result content to a file and play it using the playsound module.

    Args:
        message (str): The text to convert to speech.
        voice (str): The voice to use.
        folder (str): The folder to save the file in.
        extension (str): The file extension.
        emotion (str): The emotion to apply.
        pitch (int): The pitch adjustment.
        speed (int): The speed of the voice.
        volume (int): The volume level.

    Returns:
        None, String
    """
    try:
        result_content = generate_audio(message, voice, emotion, pitch, speed, volume)
        if result_content:
            file_path = os.path.join(folder, f"{voice}{extension}")
            with open(file_path, "wb") as file:
                file.write(result_content)
            playsound.playsound(file_path)
            os.remove(file_path)
        else:
            return "Error generating TTS audio."
    except Exception as e:
        return "Error playing TTS: " + str(e)

if __name__ == "__main__": 
    message = "Hello, this is Linda. How can I assist you today?"
    error = speak(message, voice="Linda", emotion="happy", pitch=1, speed=1, volume=1)

    if error:
        print(error)
