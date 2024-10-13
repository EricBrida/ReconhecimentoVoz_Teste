import tkinter as tk
from tkinter import font as tkFont
import winsound
import webbrowser
import speech_recognition as sr
from app.speech_recognition_module import reconhecer_fala

class VoiceRecognitionApp:
    def __init__(self, root, reconhecedor):
        self.reconhecedor = reconhecedor
        self.root = root
        self.root.title("Reconhecimento de Voz")
        self.font = tkFont.Font(family="Helvetica", size=12)

        # Criação de frames
        self.main_frame = tk.Frame(root, bg="lightgray", padx=50, pady=40)
        self.main_frame.pack(padx=100, pady=100)

        # Criação dos elementos da interface
        self.status_label = tk.Label(self.main_frame, text="Clique no botão para falar", font=self.font, bg="lightgray")
        self.status_label.pack(pady=10)

        self.lang_options = ["pt-BR", "eng", "de", "es", "fr"]
        
        # Inicializa a variável StringVar para seleção de linguagem
        self.lang_selected = tk.StringVar(value=self.lang_options[0])  # Define a opção padrão

        # Criação do menu suspenso para seleção de linguagem
        self.lang_menu = tk.OptionMenu(self.main_frame, self.lang_selected, *self.lang_options)
        self.lang_menu.pack(pady=10)

        # Botão para reconhecer fala
        self.reconhecer_button = tk.Button(self.main_frame, text="Reconhecer Fala", command=self.reconhecer_fala, font=self.font, bg="skyblue", padx=10, pady=5)
        self.reconhecer_button.pack(pady=10)

        self.resultado_label = tk.Label(self.main_frame, text="", font=self.font, fg="green", bg="lightgray")
        self.resultado_label.pack(pady=10)

    def reconhecer_fala(self):
        with sr.Microphone() as source:
            lang = self.lang_selected.get()
            self.status_label.config(text="Pronto para ouvir...", bg="lightblue")
            winsound.Beep(1000, 500)  # Emitir um beep
            texto = reconhecer_fala(self.reconhecedor, source, lang)

            if texto:
                self.resultado_label.config(text=f"Você disse: {texto}", fg="black")
                # Abertura do navegador com a busca
                url = f"https://www.google.com/search?q={texto}"
                webbrowser.open(url)
            else:
                self.resultado_label.config(text="Desculpe, não consegui entender.", fg="red")