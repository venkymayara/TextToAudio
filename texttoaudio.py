# TextToAudio
#Text_To_Audio Using Python
#pip install gTTS
#pip install playsound



from gtts import gTTS
# #pip install gtts
from playsound import playsound
# #pip install playsound


audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = " enter the text you want to convert into speech",
             lang = language, slow = False)
sp.save(audio)
playsound(audio)
