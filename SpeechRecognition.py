import speech_recognition as sr
import webbrowser as wb
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
print('speak now!')
googleurl='https://www.google.com/search?q='
yturl='https://www.youtube.com/results?search_query='
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source, duration=5)
    print('search your query')
    audio=r2.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        sent=r2.recognize_google(audio)
        print("Google Speech Recognition thinks you said " +sent )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    wb.get().open_new(yturl+sent)
