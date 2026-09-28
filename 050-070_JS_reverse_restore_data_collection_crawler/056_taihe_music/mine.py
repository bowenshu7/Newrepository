#name: taihe music search
#author: Bowen
#goal: to get the information about the search from taihe music
#date: 2026/9/28
#stage: finished

import requests
import json
import time
import execjs
from jsonpath import jsonpath

with open('getsign.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

#define word
word = input('Enter key word: ')
#define timestamp
timestamp = int(time.time())
#define data dict
data = {
    "word": word,
    "type": "",
    "appid": "16073360",
    "timestamp": timestamp
}
sign = execjs.compile(js_code).call('createSign', data)
#define headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "device-id": "8a56ddc17d5dc536f819edcc326d5df6",
    "from": "web",
    "origin": "https://music.taihe.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.taihe.com/",
    "requestid": "1790586978_j5RT5SR",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
#define web's url
url = 'https://music.91q.com/v1/search/sug'
#define params
params = {
    "sign": sign,
    "word": word,
    "type": "",
    "appid": "16073360",
    "timestamp": str(timestamp)
}
#get the result
response = requests.get(url, headers=headers, params=params)
result = json.loads(response.text)

#select data
words = jsonpath(result,'$..data[*]')
words = '\n'.join(words)
print(words)