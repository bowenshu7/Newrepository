#name: wangxiao login encrypt
#author: Bowen
#goal: to get the encrypt algorithm
#date: 2026/10/15
#stage: finished

import requests
import ddddocr
import execjs
import base64


def get_image():
    ocr = ddddocr.DdddOcr(show_ad=False)
    count = 0
    url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
    while True:
        count += 1
        response = requests.post(url, headers=headers, cookies=cookies)
        code_data = response.json().get('data')
        content = code_data.replace('data:image/png;base64,','')
        content = base64.b64decode(content)
        with open('image_captcha.png', 'wb') as f:
            f.write(content)
        word = ocr.classification(content)
        if len(word) == 4:
            print(word)
            break
        if count == 11:
            word = '未识别图片'
            break
    return word

def get_timestamp():
    url = 'https://user.wangxiao.cn/apis//common/getTime'
    response = requests.post(url, headers=headers, cookies=cookies)
    return response.json().get('data')

def get_result(pwd,word):
    url = 'https://user.wangxiao.cn/apis//login/passwordLogin'
    data = {
        "userName": "19987654321",
        "password": pwd,
        "imageCaptchaCode": word
    }
    return requests.post(url, headers=headers, cookies=cookies, json=data)

if __name__ == '__main__':
    #define headers
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "EagleEye-SessionID": "U8mp2v5e9C0nppbazfam77LcbI8X",
        "EagleEye-TraceID": "19c3d38e1792075263657100481d1d",
        "EagleEye-pAppName": "ihuy5j2ab7@7cd9bc63da81d1d",
        "Origin": "https://user.wangxiao.cn",
        "Pragma": "no-cache",
        "Referer": "https://user.wangxiao.cn/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sessionId": "1792075221907",
        "source": "pc",
        "token;": ""
    }
    #define cookies
    cookies = {
        "sessionId": "1792075221907",
        "_bl_uid": "jnm6Lv1F9bvnssbb5fyvbpRs8Lp3",
        "Hm_lvt_86efc728d941baa56ce968a5ad7bae5f": "1792075222",
        "Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f": "1792075222",
        "HMACCOUNT": "876958FB013481E3"
    }

    #get the check code
    word = get_image()
    timestamp = get_timestamp()
    pwd = '12345678'
    #import jscode
    with open('encrypt.js','r',encoding='utf-8') as f:
        jscode = f.read()
    password = execjs.compile(jscode).call('rsaencrypt',pwd+timestamp)
    #get the response
    response = get_result(password,word)
    print(response.json())
