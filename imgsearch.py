import json

import requests


import os
directory = 'data'

filePath = "./video2/frame119.jpg"
searchUrl = 'https://yandex.ru/images/search'
files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
params = {'rpt': 'imageview', 'format': 'json',
          'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
response = requests.post(searchUrl, params=params, files=files)
query_string = json.loads(response.content)['blocks'][0]['params']['url']
img_search_url = searchUrl + '?' + query_string

print(img_search_url)

tofile = open("url.txt", "w")

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        # print(os.path.join(directory, filename))
        fileME = os.path.join(directory, filename)
        searchUrl = 'https://yandex.ru/images/search'
        files = {'upfile': ('blob', open(fileME, 'rb'), 'image/jpeg')}
        params = {'rpt': 'imageview', 'format': 'json',
                'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
        response = requests.post(searchUrl, params=params, files=files)
        query_string = json.loads(response.content)['blocks'][0]['params']['url']
        img_search_url = searchUrl + '?' + query_string
        print(img_search_url)
        tofile.write(img_search_url + '\n')
        tofile.flush()
        continue
    else:
        continue
