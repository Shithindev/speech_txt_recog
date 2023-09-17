import pyttsx3
text_speech=pyttsx3.init()
text=input('enter the text...\n')
text_speech.say(text)
text_speech.runAndWait()


