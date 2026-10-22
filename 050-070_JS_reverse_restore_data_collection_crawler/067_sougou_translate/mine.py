#name: sougou translate result
#author: Bowen
#goal: to get the information about the result from sougou translate
#date: 2026/10/21
#stage: finished

import requests
import execjs

def get_the_response(keywords):
    data = "autozh-CHS"+keywords+"109984457"
    with open('get_s.js','r',encoding='utf-8') as f:
        jscode = f.read()
    s = execjs.compile(jscode).call('get_s', data)

    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://fanyi.sogou.com",
        "Pragma": "no-cache",
        "Referer": "https://fanyi.sogou.com/text?keyword=%E6%98%8Et&transfrom=auto&transto=zh-CHS&model=general",
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
        "ABTEST": "7|1792544587|v17",
        "SNUID": "1CAA5AF2F9FFA7B6B7A700F0F9299F05",
        "SUID": "E552A20B1250A20B000000006AD80F4B",
        "wuid": "1792544587388",
        "translate.sess": "f193c841-6544-4b80-98d2-4488139feb62",
        "SUV": "1792544587844",
        "SGINPUT_UPSCREEN": "1792544587859",
        "FQV": "c475123730c96bfe7b57fcf5f64f8d2c"
    }
    #define url
    url = 'https://fanyi.sogou.com/api/transpc/text/result'
    #define data
    data = {
        "from": "auto",
        "to": "zh-CHS",
        "text": keywords,
        "client": "pc",
        "fr": "browser_pc",
        "needQc": 1,
        "s": s,
        "uuid": "5ad35b30-76a7-48b5-9f0d-7c83d4b181bd",
        "exchange": False
    }

    #get the response
    return requests.post(url, headers=headers, cookies=cookies, json=data)

if __name__ == '__main__':
    keywords = "明天"
    response = get_the_response(keywords)
    print(response.json())