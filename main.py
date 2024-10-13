import speech_recognition as sr
from app.gui_module import VoiceRecognitionApp
import tkinter as tk

def main():
    reconhecedor = sr.Recognizer()

    root = tk.Tk()
    app = VoiceRecognitionApp(root, reconhecedor)

    root.mainloop()

if __name__ == "__main__":
    main()