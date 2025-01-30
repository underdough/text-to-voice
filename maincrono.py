import os 
from gtts import gTTS
from tkinter import Tk, Text, Button, END, Label


#funciones

#funcion para guardar el texto 
def save_text():
    # pass # usar pass para que no pase nada
    text = text_area.get("1.0", END)
    with open('user_input.txt', 'w', encoding='utf-8') as file:
        file.write(text)
        status_label.config(text="Texto guardado con éxito") # la w es de escritura

# función para pasar el texto a voz
def text_to_speech():
    text = text_area.get("1.0", END)
    speech = gTTS(text=text, lang='es', slow=False, tld='com.br')
    speech.save("output_3.mp3")
    status_label.config(text="Reproduciendo audio con éxito")
    
# Crear la ventana principal
root = Tk()
root.title("Texto a Voz")
root.configure(bg='black')

text_area = Text(root, height=20, width=50)
text_area.pack()
text_area.configure(bg='black')
Text.configure(text_area, fg='white')

save_button = Button(root, text= "Guardar Texto", command=save_text)
save_button.pack()

play_button = Button(root, text= "Reproducir Texto", command=text_to_speech)
play_button.pack()

status_label = Label(root, text="", fg='green', bg='black')
status_label.pack()

root.mainloop()
