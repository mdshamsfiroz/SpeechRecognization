import speech_recognition as sr
def recognize_speech():
    recognizer= sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...Say Something")
        audio = recognizer.listen(source)
        
    try:
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {recognized_text}")
        
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error occured;{e}")

if __name__=="__main__":
    recognize_speech()
