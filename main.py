# 15 march 2023
# Virtual Assistant: PROJECT JJ

# Aim : create a virtual assistant able to do simple tasks

# IMPORTS
from gtts import gTTS
from pygame import mixer

language = 'en'
mixer.init()

# CLASS
class VR:

    def __init__(self,name) -> None:
        self.name = name
        self.speak("My name is " + self.name)

    def listen(self) -> None:
        pass

    def speak(self,text) -> None:
        '''
        Help : Speaksout text argument provided
        '''
        
        cache = gTTS(text=text, lang=language, slow=False)
        cache.save("cache/text.mp3")

        mixer.music.load("cache/text.mp3")
        mixer.music.play()

        while mixer.music.get_busy():  # wait for music to finish playing
            pass

        mixer.music.unload()

# MAIN
if __name__ == "__main__":
    app = VR("JJ")
    app.speak("Hello friend.")