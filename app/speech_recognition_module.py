import speech_recognition as sr

def ajustar_ruido(reconhecedor, source):
    reconhecedor.adjust_for_ambient_noise(source, duration=1)

def reconhecer_fala(reconhecedor, source, lang):
    ajustar_ruido(reconhecedor, source)
    audio = reconhecedor.listen(source)
    try:
        texto = reconhecedor.recognize_google(audio, language=lang)
        return texto
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        raise Exception(f"Erro de reconhecimento: {e}")