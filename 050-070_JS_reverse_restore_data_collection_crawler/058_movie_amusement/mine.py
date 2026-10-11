#name: China movie scores
#author: Bowen
#goal: to get the information about the movie in China from web
#date: 2026/10/11
#stage: finished

import requests
import execjs
from jsonpath import jsonpath

#define headers
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.chinaindex.net/ranklist/4",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "UUID": "e2f5c591-3bf6-5525-9038-1f73f042524e",#it is normally the same
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
    "funcID": "undefined",
    "incognitoMode": "0",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
#define cookies
cookies = {
    "mobile_iindex_uuid": "e2f5c591-3bf6-5525-9038-1f73f042524e",
    "Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f": "1791644272",
    "HMACCOUNT": "876958FB013481E3",
    "Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f": "1791679418"
}
#define url
url = 'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank'
#define params
params = {
    "channel": "movielist",
    "sign": "5f3cce6a40c09a221b21104cc98436a3"#don't need to reverse
}
#get the response
response = requests.get(url, headers=headers, cookies=cookies, params=params)

with open('decode.js','r',encoding='utf-8') as f:
    jscode = f.read()
result = execjs.compile(jscode).call('dataFilter',response.json())
