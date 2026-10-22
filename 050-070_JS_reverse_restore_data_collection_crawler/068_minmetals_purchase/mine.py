#name: Chinese minmetals purchase information
#author: Bowen
#goal: to get the information about the purchase from minmetals web
#date: 2026/10/22
#stage: finished

import requests
import execjs

#define headers
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ec.minmetals.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
#define cookies
cookies = {
    "__jsluid_s": "f50217d5189e8d6b95a1b73b709b707e",
    "SUNWAY-ESCM-COOKIE": "5320e81a-e327-4f1b-a0a5-e52a135dc2d9",
    "JSESSIONID": "8A6F4E4F7FAB194EBBE350355D333EAB"
}

def get_publickey():
    url = 'https://ec.minmetals.com.cn/open/homepage/public'
    return requests.post(url, headers=headers, cookies=cookies).text

def get_the_response(param):
    #define url
    url = 'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page'
    #define data
    data = {
        "param": param
    }
    #get the response
    return requests.post(url, headers=headers, cookies=cookies, json=data)

if __name__ == '__main__':
    page = 4
    pubkey = get_publickey()
    with open('param.js','r',encoding='utf-8') as f:
        jscode = f.read()
    param = execjs.compile(jscode).call('get_param', page,pubkey)
    response = get_the_response(param)
    print(response.text)