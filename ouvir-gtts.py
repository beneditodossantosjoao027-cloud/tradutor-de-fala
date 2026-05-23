import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect
from playsound import playsound
import os

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    print("Fale algo...")
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio)
    print("Você disse:", texto)

    traducao = GoogleTranslator(source='auto', target='pt').translate(texto)
    print("Texto traduzido para pt-BR:", traducao)

    idioma = detect(texto)
    print("Idioma detectado:", idioma)

    # Fala o texto original
    tts_original = gTTS(text=texto, lang=idioma)
    tts_original.save("original.mp3")
    playsound("original.mp3")   # toca e só continua depois que terminar

    # Fala a tradução em português
    tts_traducao = gTTS(text=traducao, lang='pt')
    tts_traducao.save("traducao.mp3")
    playsound("traducao.mp3")   # toca depois que o anterior acabar

    # Limpa arquivos temporários
    os.remove("original.mp3")
    os.remove("traducao.mp3")

except sr.UnknownValueError:
    print("Não entendi o áudio")
except sr.RequestError:
    print("Erro ao acessar serviço de reconhecimento")
