# Text summarization and chunking 
from scraper_mustu import *

def create_chunks(data):

    API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
    headers = {"Authorization": "Bearer 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"}

    chunks =[]

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": data,
    })

    sentences = [sentence.strip() for sentence in output[0]['summary_text'].split("<n>")]

    return (sentences)

