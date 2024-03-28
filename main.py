import pyttsx3

print("Willkommen zu Robosprecher 1.1 Erstellt von Barun")

engine = pyttsx3.init()

while True:
    x = input("Bitte geben Sie ein, was ich sagen soll: ")
    if x == "q":
        break
    
    engine.say(x)
    engine.runAndWait()