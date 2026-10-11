#name: scrape information about proxy sold game accounts
#author: Bowen
#goal: to get the information about proxy sold game accounts
#date: 2026/10/7
#stage: finished

import requests
import time
import execjs

#define timestamp
timestamp = int(time.time())
#quote js code
with open('ggmm.js','r',encoding='utf-8') as f:
    jscode = f.read()
visit = execjs.compile(jscode).call('result', timestamp)
#define headers
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.sxds.com/wares/?gt=1&gid=74&timer=1791360191044",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
    "X-CSRFToken;": "",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "timeStamp": str(timestamp),
    "visitauth": visit
}
#define cookies
cookies = {
    "Hm_lvt_0ba2a72994e25a778b9c8ed44b98596a": "1791360128",
    "HMACCOUNT": "876958FB013481E3",
    "Hm_lpvt_0ba2a72994e25a778b9c8ed44b98596a": "1791360258"
}
#define url
url = 'https://www.sxds.com/api/goods/getGoodsList'
#define params
params = {
    "pageSize": "12",
    "gameId": "74",
    "goodsTypeId": "1",
    "pages": "2"
}
#get the response
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)