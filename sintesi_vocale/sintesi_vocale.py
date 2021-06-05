from gtts import gTTS
from playsound import playsound 


def sintesi_vocale():
    testo = input("inserisci il testo da sintetizzare ")
    tts = gTTS(text=testo, lang='it')
    tts.save("sintesi_vocale\sintesi.mp3")
    print("il file è stato salvato ")
    scelta=input("vuoi riprodurre l'audio? digita si o no ")
    if scelta == "si":
        playsound("sintesi_vocale\sintesi.mp3")
sintesi_vocale()
