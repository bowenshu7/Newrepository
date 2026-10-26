#name: youzan account login slider verify
#author: Bowen
#goal: to pass the slider verify of youzan account login
#date: 2026/10/25
#stage: finished

import requests
from jsonpath import jsonpath
import ddddocr
import execjs

#define headers
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://account.youzan.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://account.youzan.com/",
    "sec-ch-ua": "\"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"156\", \"Google Chrome\";v=\"156\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
}
#define cookies
cookies = {
    "yz_log_ftime": "1792934716380",
    "yz_log_uuid": "0d80464e-8eb2-034e-6537-0edbdd1f5451",
    "yz_log_seqb": "1792934716384",
    "yz_fp_hash": "oWPVh1792934718VHQOhIBo4Ke",
    "dfp": "ff59922e13b7e6323cd49859e42e287162b87571",
    "yz_log_seqn": "18"
}

def get_token():
    #define url
    url = 'https://passport.youzan.com/api/captcha/get-behavior-captcha-token-v2.json'
    #define params
    params = {
        "bizType": "15",
        "version": "1.0"
    }
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    token = jsonpath(response.json(), '$..token')[0]
    randomStr = jsonpath(response.json(), '$..randomStr')[0]
    iv = randomStr.split('@')[0][::-1]
    key = randomStr.split('@')[1][::-1]
    return token, iv, key

def get_pic(token):
    url = 'https://passport.youzan.com/api/captcha/get-behavior-captcha-data.json'
    params = {
        "token": token,
        "captchaType": "1"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    cy = jsonpath(response.json(),'$..cy')[0]
    bigUrl = jsonpath(response.json(), '$..bigUrl')[0]
    smallUrl = jsonpath(response.json(), '$..smallUrl')[0]
    bigcontent = requests.get(bigUrl, headers=headers, cookies=cookies).content
    smallcontent = requests.get(smallUrl, headers=headers, cookies=cookies).content

    ocr = ddddocr.DdddOcr(show_ad=False)
    result = ocr.slide_match(smallcontent,bigcontent)

    return result.get('target_x'),cy

def get_userbehaviordata(cx,cy,iv,key):
    with open('userbehaviordata.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    return execjs.compile(jscode).call('get_userbehaviordata',cx,cy,iv,key)

def get_response(token,ubd):
    url = 'https://passport.youzan.com/api/captcha/check-behavior-captcha-data.json'
    data = {
        "token": token,
        "bizType": 15,
        "bizData": "",
        "captchaType": 1,
        "userBehaviorData": ubd
    }
    return requests.post(url, headers=headers, cookies=cookies, json=data)


if __name__ == '__main__':
    token,iv,key = get_token()
    cx,cy = get_pic(token)
    cx = int(cx/2) - 33
    cy = int(cy/2)
    userbehaviordata = get_userbehaviordata(cx,cy,iv,key)
    response = get_response(token,userbehaviordata)
    print(response.text)

