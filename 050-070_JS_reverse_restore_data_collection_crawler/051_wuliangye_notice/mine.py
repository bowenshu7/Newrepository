#name: wuliangye employment notice
#author: Bowen
#goal: to get the information about the wuliangye notice
#date: 2026/9/21
#stage: finished

import requests
from jsonpath import jsonpath
import base64
from lxml import etree

def decode(data):
    data_decode = base64.b64decode(data)
    data = data_decode.decode('utf-8')
    html = etree.HTML(data)
    data = html.xpath('//p//text()')
    return ''.join(data)
def get_data(url):
    #get the response
    response = requests.get(url, headers=headers, params=params)

    #select nodes
    element = jsonpath(response.json(), '$..data[0]')[0]
    #select title
    title = jsonpath(element,'$.title')[0]
    print(title)
    #select date
    datum = jsonpath(element,'$.datum')[0]
    print(datum)
    #select notice
    notice = jsonpath(element,'$.notic')[0]
    notice = decode(notice)
    print(notice)
    #select file name
    file_name = jsonpath(element,'$.atta[0].filename')[0]
    print(file_name)
    #select file
    file = jsonpath(element,'$.atta[0].zhr_blob')[0]
    file = file.split(',')[-1]
    with open(file_name, 'wb') as f:
        f.write(base64.b64decode(file))

if __name__ == '__main__':
    guid = input('Enter guid: ')
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.wuliangye.com.cn/zhaopin/announcement/article?guid=50059621",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define web's url
    url = 'https://www.wuliangye.com.cn/zhaopin/sap_api/sap/bc/zhr/zhr'
    #define params
    params = {
        "sap-client": "800",
        "method": "HR-NOTICE",
        "SYSTEM": "ZHAOPIN",
        "objid": guid
    }
    get_data(url)