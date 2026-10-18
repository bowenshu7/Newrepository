#name: shenzhengxin market data date web
#author: Bowen
#goal: to get the information about the market data from shenzhengxin date
#date: 2026/10/18
#stage: finished

import requests
import execjs

with open('enckey.js','r',encoding='utf-8') as f:
    jscode = f.read()
enckey = execjs.compile(jscode).call('getResCode')
#define headers
headers = {
    "Accept": "*/*",
    "Accept-EncKey": enckey,
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://webapi.cninfo.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://webapi.cninfo.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
#define cookies
cookies = {
    "MALLSSID": "6B4B507A32666D5A70306741744B6F42714536594C626F32624C4E633067527A4646524334464F59576A69747766512F2F4B754C64722F2F7732737236464E33",
    "Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1792330346",
    "HMACCOUNT": "876958FB013481E3",
    "Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1792330352"
}
#define url
url = 'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
#define data
data = 'tdate=2026-10-16&market=SZE'
#get the response
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)