#name: bidcenter search result crawl
#author: Bowen
#goal: to get the information about the bidcenter search result
#date: 2026/10/11
#stage: finished

import requests
import execjs
import time

page = 2
timestamp = int(time.time()*1000)
#define headers
headers = {
    "accept": "text/plain, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://search.bidcenter.com.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://search.bidcenter.com.cn/",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
#define url
url = 'https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx'
#define data
data = f'from=6137&guid=61f56d79-1ce7-4ee4-bb03-21b0f6ab23e9&location=6138&token=&deftag={page}&keywords=%25e6%25b8%25b8%25e6%2588%258f&mod=0&vtime={timestamp}'.encode('utf-8', 'surrogateescape')
#get the response
response = requests.post(url, headers=headers, data=data)
with open('decode.js','r',encoding='utf-8') as f:
    jscode = f.read()
result = execjs.compile(jscode).call('AESDecrypt',response.text)
print(result)