import app.speech_recognition_module as sr

def ajustar_ruido(reconhecedor, source):
    reconhecedor.adjust_for_ambient_noise(source, duration=1)

def reconhecer_fala(reconhecedor, source):
    ajustar_ruido(reconhecedor, source)
    audio = reconhecedor.listen(source)
    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        return texto
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        raise Exception(f"Erro de reconhecimento: {e}")