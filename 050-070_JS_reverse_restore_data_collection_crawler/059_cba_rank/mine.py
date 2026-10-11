#name: cba rank situation
#author: Bowen
#goal: to get the information about the latest cba rank
#date: 2026/10/11
#stage: finished

import requests
import execjs

#define headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "isencrypt": "encrypt",
    "origin": "https://www.cbaleague.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.cbaleague.com/",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
#define url
url = 'https://data-server.cbaleague.com/api/teams/seasons/2026/standings'
#get the response
response = requests.get(url, headers=headers)
with open('decode.js','r',encoding='utf-8') as f:
    jscode = f.read()
result = execjs.compile(jscode).call('SIe', response.text[1:-1])
print(result)