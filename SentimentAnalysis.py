from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise...')
    print('Start Recording!')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    recordedaudio = recognizer.listen(source)
    print('Done recording...')
try:
    print('Printing the message')
    text = recognizer.recognize_google(recordedaudio,language='en=US')
    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)

Sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyser.polarity_scores(i)
    print(v)



