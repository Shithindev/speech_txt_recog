# speech_recog that uses the SpeechRecognition library to continuously listen to audio from a microphone and transcribe it into text using Google's speech recognition service, printing the recognized text or requesting a repeat if nothing is heard.

import speech_recognition as sr
def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()
    while True:
        with mic as source:
            print('speak...')
            audio=r.listen(source)

            try:
                text=r.recognize_google(audio)
                print('you said:----',text)
            except sr.UnknownValueError:
                print('didnt hear anything please repeat')
speech_recog()



