#name: yiche login password encryption
#author: Bowen
#goal: to get the encrypted password of yiche login web
#date: 2026/10/14
#stage: finished

import requests
import ddddocr
import execjs

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.yiban.cn",
    "Pragma": "no-cache",
    "Referer": "https://www.yiban.cn/login",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "https_waf_cookie": "96415610-2eca-487c81bdfe8457e66f9730464932a03219b3",
    "YB_SSID": "a03c16cb6ad4b827f783b95313b40f60",
    "Hm_lvt_ed61a54fb63b75cc82ad5c1796518f16": "1791958189",
    "Hm_lpvt_ed61a54fb63b75cc82ad5c1796518f16": "1791958189",
    "HMACCOUNT": "876958FB013481E3",
    "smidV2": "202610141409504303fc93eafac29b653ba661658adca300a1413c9ba96fef0",
    ".thumbcache_0b5ab3041e948888ccef775c543ff764": "AYfildrang4UrtgZxqbxMIlilfqFMIxRyQxOMNFPec8vAwYBahVd4eNXtxjB6wjm/WKgtrpj2xWG3mj/Uy8zrg%3D%3D"
}

def get_chara():
    url = 'https://www.yiban.cn/captcha/index'
    params = {
        "Wed Oct 14 2026 21:23:46 GMT 0800 (中国标准时间)": ""
    }
    ocr = ddddocr.DdddOcr(show_ad=False)
    count = 0
    while True:
        count += 1
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        with open('code.jpg','wb') as f:
            f.write(response.content)
        result = ocr.classification(response.content)
        if len(result) == 1:
            print(result)
            return result
        if count > 10:
            return '未识别文字'

def get_the_response(pwd,result):
    url = 'https://www.yiban.cn/login/doLoginAjax'
    data = {
        "'account": "12345678911",
        "password": pwd,
        "captcha": result,
        "keysTime": "1791958187.81",
        "rid": "202610141415281ebe24b65e85520b4b",
        "yt": "BAYfildrang4UrtgZxqbxMIlilfqFMIxRyQxOMNFPec8vAwYBahVd4eNXtxjB6wjm/WKgtrpj2xWG3mj/Uy8zrg=='"
    }
    return requests.post(url, headers=headers, cookies=cookies, data=data)

if __name__ == '__main__':
    password = input('enter your pwd: ')
    with open('RSAencrypt.js','r',encoding='utf-8') as f:
        jscode = f.read()
    pwd = execjs.compile(jscode).call('get_ras_password',password)
    response = get_the_response(pwd,get_chara())
    print(response.json())
