#name: qimai appstore app download data
#author: Bowen
#goal: to get the information about app download from qimai web
#date: 2026/10/19
#stage: finished

import requests
import execjs
import time

pages = 10
#define headers
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.qimai.cn",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
#define cookies
cookies ={
    "PHPSESSID": "v8e1q02fa3seqqa8l7il0m07a3",
    "qm_check": "A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdASAFKBQcCCXtzABFFIg4aHRoOBnMDARlGR2dQOVdICAolAGgCHBl0B3xUV05KVFsZXVJRWxsKFghJVktYVElWBRVP",
    "gr_user_id": "4cf7fb51-d497-493b-a299-2c933032f732",
    "USERINFO": "W29RRgnsiZ%2B07Um%2FbuX3XXnqwmrT%2FMyNl3IO%2F%2FO11KRRtitnMdY2EWmeRWzFHHoKNSJf3k6Urd1t5X9adYjV6w9AAPljbbrKNX3KOso0WSmQvvAeul0uJKlCDnJn1JZYucIqbyNVUKuq31d0mks4nA%3D%3D",
    "ada35577182650f1_gr_last_sent_cs1": "qm29239708377",
    "aso_ucenter": "e82b01oMiN%2ByzH2BC6%2Bzp45mABnJUNyXmCs5NMNBaeLnhgcKk3tBqPAXQ%2FDwzYNtZH4",
    "AUTHKEY": "c3RH2gzaA1gJ8HLfeO90Ne8wJruZc2MFmyw2Ix95GZj3oWqi4Gf87XclxCOonOt8aDA5kksaqrWMgtcxEovDKV4MrLJjuCTq2o1mZNKKMha%2BInkQl1K7Kg%3D%3D",
    "ada35577182650f1_gr_cs1": "qm29239708377",
    "synct": "1792407682.170",
    "syncd": "-506"
}
#define url
rank = '/rank/indexPlus/brand_id/1'
url = 'https://api.qimai.cn'+rank
#define params
params = {
    "brand": "all",
    "genre": "36",
    "device": "iphone",
    "country": "cn",
}
date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
for page in range(1,pages+1):
    if page != 1:
        params["date"] = date
        params["page"] = page
    param = list(params.values())
    with open('analysis.js','r',encoding='utf-8') as f:
        jscode=f.read()
    analysis=execjs.compile(jscode).call('getanalysis', -int(cookies["syncd"]),param,rank)
    params["analysis"] = analysis
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.json())
    params.pop("analysis")
    time.sleep(1)
