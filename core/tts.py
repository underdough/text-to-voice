from gtts import gTTS

def text_to_speech(text, filename="voice/output.mp3"):
    speech = gTTS(text=text, lang='es', slow=False, tld='com.br')
    speech.save(filename)
    return filename