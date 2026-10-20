#name: kuwo music search list
#author: Bowen
#goal: to get the information about the search list from kuwo music
#date: 2026/10/20
#stage: finished

import requests
import execjs

def get_the_response(reqId):
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.kuwo.cn/search/list",
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
        "Hm_lvt_cdb524f42f0ce19b169a8071123a4797": "1792506778",
        "Hm_lpvt_cdb524f42f0ce19b169a8071123a4797": "1792506778",
        "HMACCOUNT": "876958FB013481E3",
        "_ga": "GA1.2.539732214.1792506778",
        "_gid": "GA1.2.966709231.1792506778",
        "_ga_ETPBRPM9ML": "GS2.2.s1792506778$o1$g0$t1792506778$j60$l0$h0",
        "Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324": "mQwpSRPSyR7prDFNazRiCwSXzfm8MiZQ"
    }
    #define url
    url = 'https://www.kuwo.cn/openapi/v1/www/search/searchKey'
    #define params
    params = {
        "key": "zhoujielun",
        "httpsStatus": "1",
        "reqId": reqId,
        "plat": "web_www",
        "from": ""
    }
    #get the response
    return requests.get(url, headers=headers, cookies=cookies, params=params)

if __name__ == '__main__':
    with open('webpack_n.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    reqId = execjs.compile(jscode).call('get_reqId')

    response = get_the_response(reqId)
    print(response.json())