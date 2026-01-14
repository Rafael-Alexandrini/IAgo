import pyttsx3 # pyttsx3-2.91
import time

engine = pyttsx3.init()
engine.setProperty("rate", 250)
engine.setProperty("volume", 0.9)

voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

"""engine.say("Oi!")
engine.runAndWait()
engine.say("Olá!")
engine.runAndWait()

for i in range(8):
    if i % 2 == 0:
        engine.say("Puts")
        engine.runAndWait()
    else:
        engine.say("Cátis")
        engine.runAndWait()
    i = i + 1"""