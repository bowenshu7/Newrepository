#name: juejin hot articles
#author: Bowen
#goal: to get the information about the popular articles from jujin web
#date: 2026/9/10
#stage: finished (web has updated)

import requests
from jsonpath import jsonpath

#define headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://juejin.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://juejin.cn/",
    "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "x-secsdk-csrf-token": "0001000000013d8dfc81116beaea0f9feadd761666f413dcf45b48b8987a935e7df104e1795718d3ea5991e06660"
}
#define cookies
cookies = {
    "_tea_utm_cache_2608": "undefined",
    "csrf_session_id": "631d0a39b127b25c78a006ae410252dd",
    "__tea_cookie_tokens_2608": "%257B%2522web_id%2522%253A%25227683822385058137652%2522%252C%2522user_unique_id%2522%253A%25227683822385058137652%2522%252C%2522timestamp%2522%253A1789029319534%257D"
}
#define web's url
url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed'
#define params
params = {
    "aid": "2608",
    "uuid": "7683822385058137652",
    "spider": "0"
}
#define data
data = '{"id_type":2,"client_type":2608,"sort_type":200,"cursor":"0","limit":20}'.encode('utf-8', 'surrogateescape')
#get the response
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

#select nodes
element_list = jsonpath(response.json(),'$..data[*]')
for element in element_list:
    if jsonpath(element,'$.item_type')[0] != 2:
        continue
    element = jsonpath(element,'$.item_info')[0]
    #select title
    title = jsonpath(element,'$.article_info.title')[0]
    print(title)