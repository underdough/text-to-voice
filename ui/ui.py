from tkinter import Tk, Text, Button, Label, END
from core.file_handler import save_text
from core.tts import text_to_speech

def create_ui():
    root = Tk()
    root.title("Texto a Voz")
    root.configure(bg='black')

    text_area = Text(root, height=20, width=50, font=("Arial", 12))
    text_area.pack()
    text_area.configure(bg='black', fg='white')

    status_label = Label(root, text="", fg='green', bg='black')
    status_label.pack()

    def save():
        text = text_area.get("1.0", END)
        message = save_text(text)
        status_label.config(text=message)

    def play():
        text = text_area.get("1.0", END)
        filename = text_to_speech(text)
        status_label.config(text="Audio generado con éxito")

    save_button = Button(root, text="Guardar Texto", command=save)
    save_button.pack(pady=10)

    play_button = Button(root, text="Reproducir Texto", command=play)
    play_button.pack()

    root.mainloop()
