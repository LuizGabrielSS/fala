import pyttsx3
import speech_recognition as sr
from random import choice
from conversar import falas,perturbar,erros

reproducao = pyttsx3.init()
fala = choice(falas)
perturba = choice(perturbar)
erro = choice(erros)

def sai_som(resposta):
	reproducao.say(resposta)
	reproducao.runAndWait()

rec = sr.Recognizer()

with sr.Microphone() as s:
    rec.adjust_for_ambient_noise(s)
while True:
    audio = rec.listen(s)
    texto = rec.recognize_google(audio,language = "pt")

    resposta = input("Gostaria de perturbar alguem,imitar ou so falar?:")
    #resposta = 

    if resposta == 'imitar':
        sai_som(texto)
        print(texto)

    elif resposta == 'falar':
        sai_som(fala)
        print(fala)

    elif 'perturbar' in resposta:
        sai_som(perturba)
        print(perturba)
    
    else:
        sai_som(erro)
        print(erro)
