import json
import base64
import requests as requests
from config import catalog, api_key

with open("4.jpg", "rb") as f:
     image_data = base64.b64encode(f.read()).decode('utf-8')


vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'

p = requests.post(vision_url, headers={'Authorization': 'Api-Key '+api_key}, json={
     'folderId': catalog,
     'analyzeSpecs': [
     {
     'content': image_data,
     'features': [
     {
     'type': 'TEXT_DETECTION',
     'textDetectionConfig': {'languageCodes': ['ru']}
     }
     ],
     }
     ]}).json()

with open("data.json", "w", encoding='utf-8') as write_file:
    json.dump(p, write_file)
with open("data.json", "r", encoding='utf-8') as read_file:
     data_2 = json.load(read_file)
data_3 = data_2['results'][0]['results'][0]['textDetection']['pages'][0]['blocks']
word = []
for i in data_3:
     lines = i['lines']
     for j in lines:
          words=(j['words'])
          for y in words:
              word.append(y['text'])

print(word)

