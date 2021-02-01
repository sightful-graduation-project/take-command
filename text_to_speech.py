from gtts import gTTS
from playsound import playsound
import os

def play_text(text_to_play):
    language = 'en'
    output = gTTS(text=text_to_play,lang=language,slow=False)
    output.save('output.mp3')
    playsound('output.mp3')
    os.remove("output.mp3")


