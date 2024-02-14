import requests
import time
from api import API_KEY_ASSEMBLYAI
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers = {'authorization': API_KEY_ASSEMBLYAI}


CHUNK_SIZE = 5_242_880  # 5MB
filename = "D:\Python projects\Speech Recognition Project \Test2.ogg"

# upload

CHUNK_SIZE = 5_242_880  # 5MB
def upload(filename):
    def read_file(filename, CHUNK_SIZE):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers, data=read_file(filename, CHUNK_SIZE))
    audio_url = upload_response.json()['upload_url']
    return audio_url

# transcribe
def transcription(audio_url):
    transcript_request = {"audio_url" : audio_url}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request , headers=headers)
    job_id = transcript_response.json()['id']
    return job_id


# poll
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(audio_url):
    transcript_id = transcription(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data,None
        elif data['status'] == 'error':
            return data,data['error']

audio_url = upload(filename)
data, error = get_transcription_result_url(audio_url)

text_filename = filename + ".txt"
if data:
    with open(text_filename,'w') as f:
        f.write(data['text'])
    print("Transcription saved !!")
elif error:
    print("Error!!",error)




"""
import assemblyai as aai

aai.settings.api_key = "2ad863ce06ad4760bd401ac221f2e525"

FILE_URL = "D:\Python projects\Speech Recognition Project Series\Test1.wav"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

print(transcript.text)
"""
