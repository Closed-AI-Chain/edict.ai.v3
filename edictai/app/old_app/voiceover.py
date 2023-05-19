import requests
import json
import time

# API website to get your (free) key: https://rapidapi.com/k_1/api/large-text-to-speech/



def voice_over(text):


    url = "https://large-text-to-speech.p.rapidapi.com/tts"
    payload = {"text": text}

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com",
        'x-rapidapi-key': "4746f8dfa7msh12d29ab1b0cd7d9p186eb2jsne58f90e4151e"
        }

    # POST request
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response.text)

    # get id and eta of the job from the response
    id = json.loads(response.text)['id']
    eta = json.loads(response.text)['eta']

    print(f'Waiting {eta} seconds for the job to finish...')
    time.sleep(eta)

    # GET the result from the API
    response = requests.request("GET", url, headers=headers, params={'id': id})
    # if url not returned yet, wait and try again
    while "url" not in json.loads(response.text):
        response = requests.get(url, headers=headers, params={'id': id})
        time.sleep(5)
    # if no error, get url and download the audio file
    if not "error" in json.loads(response.text):
        result_url = json.loads(response.text)['url']
        # download the waw file from results_url
        response = requests.get(result_url)
        # save the waw file to disk
        with open('output.wav', 'wb') as f:
            f.write(response.content)
        print("File output.wav saved!")
    else:
        print(json.loads(response.text)['error'])



# import pyttsx3
# import spacy
# from textblob import TextBlob

# # initialize the text-to-speech engine
# engine = pyttsx3.init()

# # set the properties of the voice
# engine.setProperty('volume', 1) # volume between 0 and 1
# voice = engine.getProperty('voices')
# # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enIN_RaviM"
# # engine.setProperty('voice', voice_id)
# engine.setProperty('voice', voice[1].id)
# # load the spaCy English model
# nlp = spacy.load('en_core_web_sm')

# # define a function to speak a given text with a given pitch and rate
# def speak_with_pitch_and_rate(text, pitch, rate):
#     # set the pitch and rate of the voice
#     engine.setProperty('pitch', pitch)
#     engine.setProperty('rate', rate)
    
#     # speak the text with the specified pitch and rate
#     engine.say(text)
#     engine.runAndWait()

# # define a sample paragraph to test the code
# paragraph = "Cricketer Kedar Jadhav's father Mahadev Sopan Jadhav has gone missing since Monday morning from Pune's Kothrud area. Cricketer Kedar Jadhav's father Mahadev Sopan Jadhav has gone missing since Monday morning from Pune's Kothrud area.I am very happy"

# # process each sentence in the paragraph and allocate pitch and rate based on sentiment
# for sentence in nlp(paragraph).sents:
#     # calculate the sentiment score for the sentence using TextBlob
#     sentiment_score = TextBlob(sentence.text).sentiment.polarity
    
#     # allocate pitch and rate based on the sentiment score
#     if sentiment_score > 0:
#         pitch = 150 # happy
#         rate = 170 # fast
#     elif sentiment_score < 0:
#         pitch = 100 # sad
#         rate = 140 # slow
#     else:
#         pitch = 125 # neutral
#         rate = 150 # normal
    
#     # speak the sentence with the allocated pitch and rate
#     speak_with_pitch_and_rate(sentence.text, pitch, rate)
