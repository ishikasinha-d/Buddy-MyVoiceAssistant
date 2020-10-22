import speech_recognition as sr
import pyttsx3 as ptx
import random
import os

r = sr.Recognizer()

def say():
    ptx.speak(random.choice(["Okay; launching", "As you say", "As you command", "Just a second", "Yeah sure"]))

ptx.speak("What application do you want to launch?")
with sr.Microphone() as source:
    print("say")
    audio = r.listen(source)
    print("okay")
            

x = r.recognize_google(audio)
x=x.lower()
print(x)
if ("chrome" in x or "google chrome" in x):
    say()
    os.system("chrome")

elif ("text editor" in x or "editor" in x or "notepad" in x):
    say()
    os.system("notepad")
elif ("exit" in x or "nothing" in x):
    ptx.speak("Okay we'll exit...wait")
else:
    ptx.speak("Path of this application has not been added yet")