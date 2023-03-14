from gtts import gTTS
from pygame import mixer

mytext = 'Hello'

language = 'en'

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("cache/welcome.mp3")

mixer.init()
mixer.music.load("D:/Programming2/2023 March/Virtual Assistant JJ/cache/welcome.mp3")
mixer.music.play()

while mixer.music.get_busy():  # wait for music to finish playing
    pass

