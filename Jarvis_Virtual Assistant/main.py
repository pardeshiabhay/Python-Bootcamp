import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    
    
    #Initialize Pygame mixer
    pygame.mixer.init()
    
    #Load the MP3file
    pygame.mixer.music.load('temp.mp3')
    
    #play the mp3 file
    pygame.mixer.music.play()
    
    #keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(api_key= "")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return print(completion.choices[0].message)
    
    
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ") [1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "read news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()
            
            #extract the articles
            articles = data.get("articles", [])
            
            #print the headlines
            for article in articles:
                speak(article["title"])
                
    else:
        #Let openAI handle the request
        output = aiProcess(c)
        speak(output)
    
    
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word Jarvis
        # Obtain audio from the microphone
        r = sr.Recognizer()
            
        print("Recognizing....")
            
        #Recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2, phrase_time_limit= 1 )
                
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
                      
        except Exception as e:
            print("Error; {0}".format(e))