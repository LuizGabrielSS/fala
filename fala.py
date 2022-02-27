import pyttsx3
import speech_recognition as sr
from random import choice
from conversar import falas,perturbar,erros

reproducao = pyttsx3.init()
fala = choice(falas)
perturba = choice(perturbar)
erro = choice(erros)

resposta = input("Gostaria de perturbar alguem,imitar ou so falar?:")

def sai_som(resposta):
	reproducao.say(resposta)
	reproducao.runAndWait()
def brincar():
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        try:
            while True:

                audio = rec.listen(s)
                texto = rec.recognize_google(audio,language = "pt")

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

        except sr.UnknownValueError:
                    sai_som(erro)

if __name__ == '__main__':
    sai_som("iniciando")
    brincar()

