import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os


recog1 = spr.Recognizer()


mc = spr.Microphone()


def recognize_speech(recog, source):
    try:
        recog.adjust_for_ambient_noise(source, duration=0.2)  
        audio = recog.listen(source)  
        recognized_text = recog.recognize_google(audio)  
        return recognized_text.lower()
    except spr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except spr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

while(1):
    with mc as source:
        from_lang = input("Enter Your language:-")
        to_lang = input("Enter Your translation language:-")
        print("Speak 'hello' to initiate the Translation!")
        print("Speak 'Z' to break the translator")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        MyText = recognize_speech(recog1, source)
    if MyText == 'z' or MyText == 'Z':
        break

    if MyText and 'hello' in MyText:
        
        translator = Translator()

        with mc as source:
            print("Speak a sentence to translate...")
            get_sentence = recognize_speech(recog1, source)

        
            if get_sentence:
                try:
                    
                    print(f"Phrase to be Translated: {get_sentence}")

                
                    text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
                    translated_text = text_to_translate.text

                
                    speak = gTTS(text=translated_text, lang=to_lang, slow=False)

                
                    speak.save("captured_voice.mp3")

                
                    os.system("start captured_voice.mp3")

                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Unable to capture the sentence for translation.")
print("Translator Broken")
