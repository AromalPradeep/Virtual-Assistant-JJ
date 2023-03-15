# 15 march 2023
# Virtual Assistant: PROJECT JJ

# Aim : create a virtual assistant able to do simple tasks

# IMPORTS
from gtts import gTTS
from pygame import mixer
import speech_recognition as speech     

import os
from datetime import datetime

language = 'en'
mixer.init()
voice = speech.Recognizer()

# CLASS
class VR:

    def __init__(self,name) -> None:
        self.name = name
        self.speak("My name is " + self.name)
        self.listen()

    def listen(self) -> None:

        while True:
            try:
                with speech.Microphone() as source:
                    voice_command = voice.listen(source)

                 # check input
                try:
                            
                    text = voice.recognize_google(voice_command)
                            
                # handle the exceptions
                except speech.UnknownValueError:
                            
                    text = "System could not understand. Please try again."
            except:
                text = "Sorry, there was an error. Please try again later."

            if self.verify(text)==1:                
                break
            
            

    def verify(self,text) -> int:
        if text in ("exit","quit"):
            text = "Ok bie."
            self.speak(text)
            return 1
        else:
            self.speak(text)
            return 0
            

    def speak(self,text) -> None:
        '''
        Help : Speaksout text argument provided
        '''

        try:
            cache = gTTS(text=text, lang=language, slow=False)
            cache.save("cache/text.mp3")
            
        except FileNotFoundError:
            # create cache folder if it does not exist
            os.mkdir('cache')
            cache = gTTS(text=text, lang=language, slow=False)
            cache.save("cache/text.mp3")

        mixer.music.load("cache/text.mp3")
        mixer.music.play()

        while mixer.music.get_busy():  # wait for music to finish playing
            pass

        mixer.music.unload()

    def exit(self) -> None:
        '''
        Help : Clears cache and resets program
        '''
        try:
            # clear cache files
            for root, dirs, files in os.walk('cache'):
                for file in files:
                    os.remove(os.path.join(root, file))
        except FileNotFoundError:
            # create cache folder if it does not exist
            os.mkdir('cache')
            
        # record last run
        with open("cache/last_run.txt","w") as f:            
            f.write(str(datetime.now()))

# MAIN
if __name__ == "__main__":
    app = VR("JJ")
    #app.speak("Hello friend.")
    app.exit()