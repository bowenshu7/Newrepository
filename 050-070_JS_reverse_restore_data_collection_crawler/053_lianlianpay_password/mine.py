#name: global lianlianpay encode password reverse
#author: Bowen
#goal: to get the encode code about password of global lianlianpay
#date: 2026/9/24
#stage: finished

import requests
import json
import execjs

account = input("Enter account: ")
password_ori = input("Enter password: ")
with open('reverse_password.js','r',encoding='utf-8') as f:
    js_code = f.read()
password = execjs.compile(js_code).call('dd',password_ori)
#define headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "baggage": "sentry-environment=production,sentry-release=global-sso%401.0.89,sentry-public_key=3ed0768cf835395f20e8c3bca4499ed8,sentry-trace_id=824ac6a04d994d8d9ad5b1930e166ab4",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "dev-info-bs": "f6DLCQ4siw3_4619wHk_RDf8Yi7ZJWHK-A2xixbtBWjjQpS1j63nAC5wUehRqN5KiZsTibv1HT9c5uBLYrtYZFs_rRvyxEpsBpsJHK6cukyVKEU9HfI2CNJSAcLs-CLxU_jEQ0kX52JR3S-8y4SXOePU-WWNSvjY",
    "lang": "zh-CN",
    "origin": "https://global.lianlianpay.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://global.lianlianpay.com/signin?from=glabal",
    "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "824ac6a04d994d8d9ad5b1930e166ab4-bcb267cf37f4238f-0",
    "source": "PC",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}
#define cookies
cookies = {
    "sajssdk_2015_cross_new_user": "1",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221a0d2178a5f17e9-028bf989de25c92-26071d51-1327104-1a0d2178a601708%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fglobal.lianlianpay.com%2Fsignin%3Ffrom%3Dglabal%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMWEwZDIxNzhhNWYxN2U5LTAyOGJmOTg5ZGUyNWM5Mi0yNjA3MWQ1MS0xMzI3MTA0LTFhMGQyMTc4YTYwMTcwOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a0d2178a5f17e9-028bf989de25c92-26071d51-1327104-1a0d2178a601708%22%7D",
    "BSFIT_DFPUUID": "EADPQ_D3wpoGAnwlrSwVKBTZuLYFAWoZ",
    "BSFIT_EXPIRATION": "1790270315604",
    "BSFIT_COOKIE_CACHE": "F4MbLeyUR7lILXTZa0NnDiQcS7FlyaTs",
    "BSFIT_DEVICEID": "f6DLCQ4siw3_4619wHk_RDf8Yi7ZJWHK-A2xixbtBWjjQpS1j63nAC5wUehRqN5KiZsTibv1HT9c5uBLYrtYZFs_rRvyxEpsBpsJHK6cukyVKEU9HfI2CNJSAcLs-CLxU_jEQ0kX52JR3S-8y4SXOePU-WWNSvjY"
}
#define web's url
url = 'https://global.lianlianpay.com/cb-va-sso-api/login'
#define data
data = {
    "loginName":account,
    "password":password
}
data = json.dumps(data, separators=(',',':'))
#get the response
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
