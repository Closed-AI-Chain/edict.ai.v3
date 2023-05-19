import re
import spacy
from rake_nltk import Rake
from moviepy.editor import VideoFileClip, CompositeVideoClip
import nltk
from keybert import KeyBERT
nltk.download('stopwords')
import nltk
nltk.download('punkt')
from moviepy.editor import *
# from summ import summariser
from PIL import Image

# Open the image file


# from .summarise import summariser
# from scraper import scraped_content
# from voiceover import voice_over
from sklearn.metrics.pairwise import cosine_similarity
from moviepy.editor import VideoFileClip, concatenate_videoclips

import requests
import json
import time

import requests
import os

import os
import requests
from moviepy.editor import *

import requests
import json
import time
# from scraper import scraped_content
from moviepy.editor import *
# example_text = scraped_content
# paragraph = '''Since Musk purchased Twitter - for $44 billion - last year he has fired over 6,000 employees and left many of the rest fearing a similar fate. Twitter boss Elon Musk - who has made firing over three-fourth of the company's previously 8,000-strong workforce since buying it in October last year - was called out Thursday for reportedly asking senior managers to recommend their best employees for promotion, and then firing the former and replacing them with the latter as part of a 'cost-cutting drive', British publication iNews said.The publication quoted a former staffer as saying, "Managers were recently told to provide a list of people who ought to be promoted little did they realise they were signing their own death warrant: many of those managers were subsequently fired and replaced by those theyTMd recommended, as part of a cost-cutting drive." Note: The original report is behind a paywall.Hindustan Times cannot independently confirm the figure but reports indicate at least 50 ex-senior managers were so fired; this was reportedly after Musk claimed to be 'done' with layoffs.'''
# paragraph = summariser()

# chunks = []

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
def coindesk_merged(chuny):
    
    all_image_filenames = []
    chunks = []
    
    for i in chuny: 
        all_image_filenames.append(i[-1])
        chunks.append(i[0])
    
    print("image_filenames: ")
    print(all_image_filenames)
    
    print("chunks: ")
    print(chunks)
    # words = paragraph.split()
    # chunk_size = 20

    # import requests

    # API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
    # headers = {"Authorization": "Bearer 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"}

    # chunks =[]

    # def query(payload):
    #     response = requests.post(API_URL, headers=headers, json=payload)
    #     return response.json()
        
    # output_3 = query({
    #     "inputs": data,
    # })

    # sentences = output_3[0]['summary_text'].split("<n>")
    # for i in sentences: 
    #     words = i.split()
    #     index_to_break = 10 # Index of the word after which you want to insert the line break
    #     new_sentence = " ".join(words[:index_to_break+1]) + "\n" + " ".join(words[index_to_break+1:])
    #     chunks.append(new_sentence)



    # chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]

    meraNum = 0

    clips  = ['app/vidtemplates/intro.mp4']

    for chunk in chunks:
        meraNum += 1
    #     apnaChunk = ''.join(chunk)
    #     print(apnaChunk)
    #     keywords = kw_model.extract_keywords(apnaChunk,keyphrase_ngram_range=(2, 3),top_n=1)
    #     print(keywords)
    #     apnaKeywords = keywords[0]

    #     url = "https://bing-image-search1.p.rapidapi.com/images/search"
    #     headers = {
    #         "X-RapidAPI-Key": "4746f8dfa7msh12d29ab1b0cd7d9p186eb2jsne58f90e4151e",
    #         "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
    #     }
        
    #     print(apnaKeywords)

    #     query = apnaKeywords 

    #     search_queries = query

    # # Set up the search queries and image folder

    #     image_folder = "coindesk" 

    # # Create the image folder and scrapped images folder if they don't exist
    #     if not os.path.exists(image_folder):
    #         os.makedirs(image_folder)

    #     querystring = {"q": query, "count": "3"} # Change count to 3
    #     response = requests.request("GET", url, headers=headers, params=querystring)
    #     results = response.json()["value"]
    # 
    # # Download each image and save with an index
    #     for i, result in enumerate(results):
    #         image_url = result["contentUrl"]
    #         image_data = requests.get(image_url).content
    #         file_extension = os.path.splitext(image_url)[-1]
    #         file_extension = file_extension.split('?')[0]
    #         filename = os.path.join(image_folder, f"chunk_{meraNum}_{i+1}{file_extension}")
    # # Use query name in filename
    #         with open(filename, "wb") as f:
    #             f.write(image_data)
            
    #         if(file_extension==".jpeg" or file_extension==".jpg" or file_extension==".png"):


    #                 # print(file_extension)
    #                 image_filename = f"images\chunk_{meraNum}_{1}{file_extension}"

    #                 image = Image.open(f"{image_filename}")
    #                 # resized_image = image.resize((1280,720))
    #                 # resized_image.save(f"{image_filename}")
    #                 break


                    # Save the resized image as a new file
                    # tempimg.save(f"{filename}")
            # filenametemp = Image.open(filename)

            # Resize the image to 1280x720 pixels

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
        image_filename = all_image_filenames[meraNum-1]

    # API website to get your (free) key: https://rapidapi.com/k_1/api/large-text-to-speech/
        text = chunk
        url = "https://large-text-to-speech.p.rapidapi.com/tts"
        headers = {
                'content-type': "application/json",
                'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com",
                'x-rapidapi-key': "cb09b1e00cmsh1f2d0bb3adbab05p1b18f7jsn0d055623b10f"
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
        image = ImageClip(image_filename)
        image_duration = audio.duration
        audio_duration = audio.duration
        if audio_duration > image_duration:
            image = image.resize(height=655,width=1143).set_duration(audio_duration)
        else:
            image = image.resize(height=655,width=1143)


        base_video = VideoFileClip('app/vidtemplates/temp.mp4')
        # Create the clips and merge them into one video
        video = CompositeVideoClip([image.set_audio(audio)])


        # print(TextClip.list('font'))


        overlay_position = (662, 135) # (x, y) coordinates
        final_clip_fin = CompositeVideoClip([base_video, video.set_pos(overlay_position)], size=base_video.size)

        sub_vid = final_clip_fin.set_duration(audio_duration)
        
        # c=VideoFileClip("image_filename")
        textembed=TextClip(text,fontsize=34,color="white",font="Arial-Rounded-MT-Bold",stroke_color="black",stroke_width=1).set_position((100,975)).set_duration(audio_duration)
        final_clip=CompositeVideoClip([sub_vid,textembed])

        final_filename = f"edictai/app/chunk_{meraNum}.mp4"
        
        final_clip.write_videofile(final_filename, fps=24)
        clips.append(final_filename)
        print(f"Video saved as {final_filename}")

    

    # create VideoFileClip objects from the clips
    clips.append('app/vidtemplates/outro.mp4')
    clips_final = [VideoFileClip(clip) for clip in clips]

    # concatenate the clips
    final_clip = concatenate_videoclips(clips_final)

    # write the final video to file
    final_clip.write_videofile("merged_video.mp4")
    return "merged_video.mp4"

# from scraper import coinDesk 
# coindesk_merged(coinDesk())