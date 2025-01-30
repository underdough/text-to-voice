def save_text(text, filename="text/user_input.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return "Texto guardado con éxito"
