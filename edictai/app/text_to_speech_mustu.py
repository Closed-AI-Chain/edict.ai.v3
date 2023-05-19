# Following pip packages need to be installed:
# !pip install git+https://github.com/huggingface/transformers sentencepiece datasets

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset
import requests
import json
import time 

# Microsoft
# Errored 
def speecht5_tts(data):

    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

    inputs = processor(text=data, return_tensors="pt")

    # load xvector containing speaker's voice characteristics from a dataset
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

    sf.write("speech.wav", speech.numpy(), samplerate=16000)

# Facebook
# Errored
def fastspeech2_ljspeech(text):

    from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
    from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
    import IPython.display as ipd

    models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
        "facebook/fastspeech2-en-ljspeech",
        arg_overrides={"vocoder": "hifigan", "fp16": False}
    )
    model = models[0]
    TTSHubInterface.update_cfg_with_data_cfg(cfg, task.data_cfg)
    generator = task.build_generator(model, cfg)

    sample = TTSHubInterface.get_model_input(task, text)
    wav, rate = TTSHubInterface.get_prediction(task, model, generator, sample)

    ipd.Audio(wav, rate=rate)

def large_tts(chunk,meraNum):

    text = chunk
    url = "https://large-text-to-speech.p.rapidapi.com/tts"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com",
        'x-rapidapi-key': "e38e930ad6msh1de1a764a5e59cbp14f9a7jsn8816f5870fb0"
        }

    payload = {"text": text}

    # POST request
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    id = json.loads(response.text)['id']
    eta = json.loads(response.text)['eta']  

    # GET the result from the API
    response = requests.request("GET", url, headers=headers, params={'id': id})

    # If url not returned yet, wait and try again
    while "url" not in json.loads(response.text):
        response = requests.get(url, headers=headers, params={'id': id})
        time.sleep(5)
        
    if not "error" in json.loads(response.text):
        result_url = json.loads(response.text)['url']
        response = requests.get(result_url)
        with open(f'audios/chunk_{meraNum}.wav', 'wb') as f:
            f.write(response.content)
        print(f"File chunk_{meraNum}.wav saved!")
    else:
        print(json.loads(response.text)['error'])

    return(f'audios/chunk_{meraNum}.wav')
