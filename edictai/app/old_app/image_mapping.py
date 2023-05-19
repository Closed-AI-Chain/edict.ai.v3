import re
import spacy
# from rake_nltk import Rake
import nltk
from keybert import KeyBERT
nltk.download('stopwords')
import nltk
nltk.download('punkt')

# from summ import summariser

# from .summarise import summariser
# from scraper import scraped_content
# from voiceover import voice_over
# from sklearn.metrics.pairwise import cosine_similarity
from moviepy.editor import VideoFileClip, concatenate_videoclips

import requests
import json
import time

import requests
import os

os.environ['PILLOW_VERSION'] = '7.0.0'
from PIL import Image, ImageDraw, ImageFont

from moviepy.editor import *

# example_text = scraped_content
paragraph = '''As part of the Mumbai-Ahmedabad bullet train project, the construction of a 21 km undersea tunnel between Shilphata and Vikhroli is ready to begin. This development comes after when an underground Mumbai bullet train station came to its final stage.'''
# paragraph = summariser(example_text)

chunks = []

# def chunking(paragraph):
#   # Define regular expression pattern to split on all types of punctuation marks
#   pattern = r'\.'
  
#   # Split paragraph into chunks
#   chunks = re.split(pattern, paragraph)

#   # Remove empty chunks and strip whitespace from each chunk
#   chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

#   for chunk in chunks: 
#   # calculate the sentiment score for the sentence using TextBlob
#     r = Rake()
#     # kw_model = KeyBERT()
#   # Extract keywords from the text
#     r.extract_keywords_from_text(chunk)
#     # top_keywords = kw_model.extract_keywords(chunk, top_n=3,keyphrase_ngram_range=(3, 3),use_mmr=True, diversity=0.3)

    

#   # Get the top 5 ranked keywords with their corresponding scores
#     top_keywords = r.get_ranked_phrases()[:3]
#     search_queries.extend(top_keywords)
#     print(top_keywords)

# # Call funtion
# chunking(paragraph)

kw_model = KeyBERT()
words = paragraph.split()
chunk_size = 20

chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]

meraNum = 0
clips  = []

for chunk in chunks:
    meraNum += 1
    apnaChunk = ' '.join(chunk)
    print(apnaChunk)
    keywords = kw_model.extract_keywords(apnaChunk,keyphrase_ngram_range=(2, 3),top_n=1)
    print(keywords)
    apnaKeywords = keywords[0]

    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    headers = {
        "X-RapidAPI-Key": "3312f61f1amsh588edf6c4996bf5p14e1a1jsn386260901b4f",
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
    }
    query = apnaKeywords
    search_queries = query

# Set up the search queries and image folder

    image_folder = "images" 
    scrapped_images_folder = "scrapped_images"

# Create the image folder and scrapped images folder if they don't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    if not os.path.exists(scrapped_images_folder):
        os.makedirs(scrapped_images_folder)

    if(query==""):
        pass
    else:
        querystring = {"q": query, "count": "3"} # Change count to 3
        response = requests.request("GET", url, headers=headers, params=querystring)
        results = response.json()["value"]

        image_filename=""
        # Download each image and save with an index
        for i, result in enumerate(results):
            image_url = result["contentUrl"]
            image_data = requests.get(image_url).content
            file_extension = os.path.splitext(image_url)[-1]
            file_extension = file_extension.split('?')[0]
            filename = os.path.join(image_folder, f"chunk_{meraNum}_{i+1}{file_extension}") # Use query name in filename
            with open(filename, "wb") as f:
                f.write(image_data)
            print(f"Image saved as {filename}")

            if(file_extension==".jpeg" or file_extension==".jpg" or file_extension==".png"):
                # img = Image.open(f"{filename}")
    
                # # Call draw Method to add 2D graphics in an image
                # I1 = ImageDraw.Draw(img)
                
                # # Specify the font and font size to use
                # font = ImageFont.truetype('times.ttf', 36)

                # # Calculate the x and y coordinates for the text
                # text_width, text_height = I1.textsize(apnaChunk, font=font)
                # x = (img.width - text_width) // 2
                # y = img.height - text_height - 10

                # # Add Text to an image
                # I1.text((x,y), apnaChunk, font=font, fill=(0, 0, 0))
                
                # # Save the edited image
                # img.save(f"{filename}")

                print(file_extension)
                image_filename = f"images\chunk_{meraNum}_{1}{file_extension}"
                break

# Define the voice-over function
# def voice_over(query):
#     # Set up the query string and get the results
#     # querystring = {"q": query, "count": "1"}
#     # response = requests.request("GET", url, headers=headers, params=querystring)
#     # results = response.json()["value"]
#     # # Get the audio from the first result
#     # audio_url = results[0]["hostPageUrl"] + "#tts-" + query
#     # audio_data = requests.get(audio_url).content
#     # Write the audio to a file
#     url = "https://large-text-to-speech.p.rapidapi.com/tts"
#     payload = {"text": query}

#     headers = {
#         'content-type': "application/json",
#         'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com",
#         'x-rapidapi-key': "4746f8dfa7msh12d29ab1b0cd7d9p186eb2jsne58f90e4151e"
#         }

#     # POST request
#     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
#     print(response.text)

#     # get id and eta of the job from the response
#     id = json.loads(response.text)['id']
#     eta = json.loads(response.text)['eta']

#     print(f'Waiting {eta} seconds for the job to finish...')
#     time.sleep(eta)

#     # GET the result from the API
#     response = requests.request("GET", url, headers=headers, params={'id': id})
#     # if url not returned yet, wait and try again
#     while "url" not in json.loads(response.text):
#         response = requests.get(url, headers=headers, params={'id': id})
#         time.sleep(5)
#     # if no error, get url and download the audio file
#     if not "error" in json.loads(response.text):
#         result_url = json.loads(response.text)['url']
#         # download the waw file from results_url
#         response = requests.get(result_url)
#         # save the waw file to disk
#         audio_filename = f"edict_ai/app/{query}.mp3"
#         with open('audio_filename', 'wb') as f:
#             f.write(response.content)
#         print("File output.mp3 saved!")
#         return audio_filename
    

# API website to get your (free) key: https://rapidapi.com/k_1/api/large-text-to-speech/
    text = apnaChunk
    url = "https://large-text-to-speech.p.rapidapi.com/tts"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "3312f61f1amsh588edf6c4996bf5p14e1a1jsn386260901b4f",
        "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
    }


    payload = {"text": text}

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
            # save the waw file to disk with corresponding name
        with open(f'chunk_{meraNum}.wav', 'wb') as f:
            f.write(response.content)
        print(f"File chunk_{meraNum}.wav saved!")
    else:
        print(json.loads(response.text)['error'])

    # Loop through each query and create a video

        # # Get the most similar image
        # similarity_scores = []
        # most_similar_filename = None
        # for filename in os.listdir(scrapped_images_folder):
        #     if query in filename:
        #         image = ImageClip(os.path.join(scrapped_images_folder, filename))
        #         similarity_score = image.cosine_similarity(query)
        #         similarity_scores.append(similarity_score)
        #         if similarity_score == max(similarity_scores):
        #             most_similar_filename = os.path.join(scrapped_images_folder, filename)
        # if most_similar_filename is None:
        #     querystring = {"q": query, "count": "3"} # Change count to 3
        #     response = requests.request("GET", url, headers=headers, params=querystring)
        #     results = response.json()["value"]
        #     most_similar_result = results[0]
        #     most_similar_image_url = most_similar_result["contentUrl"]
        #     most_similar_image_data = requests.get(most_similar_image_url).content
        #     most_similar_file_extension = os.path.splitext(most_similar_image_url)[-1]
        #     most_similar_file_extension = most_similar_file_extension.split('?')[0]
        #     most_similar_filename = os.path.join(image_folder, f"{query}{most_similar_file_extension}")
        #     with open(most_similar_filename, "wb") as f:
        #         f.write(most_similar_image_data)
        #     print(f"Most similar image saved as {most_similar_filename}")
    
    # Get the audio clip for the query
    audio_filename = f'chunk_{meraNum}.wav'
    print(audio_filename)
    audio = AudioFileClip(audio_filename)

    # Create the image clip and resize it to match the audio duration
    try: 
        print(image_filename)
        image = ImageClip(image_filename)
        image_duration = audio.duration
        audio_duration = audio.duration
        # if audio_duration > image_duration:
        #     image = image.resize(height=720).set_duration(audio_duration)
        # else:
        #     image = image.resize(height=720)

        # Create the clips and merge them into one video
        video = CompositeVideoClip([image.set_audio(audio)])
        final_clip = video.set_duration(audio_duration)
        final_filename = f"chunk_{meraNum}.mp4"
        
        final_clip.write_videofile(final_filename, fps=24)
        clips.append(final_filename)
        print(f"Video saved as {final_filename}")
    except:
        print("Laude lag gaye")

from moviepy.editor import *

# create VideoFileClip objects from the clips
clips_final = [VideoFileClip(clip) for clip in clips]

# concatenate the clips
final_clip = concatenate_videoclips(clips_final,method="compose")

# write the final video to file
final_clip.write_videofile("merged_video.mp4")