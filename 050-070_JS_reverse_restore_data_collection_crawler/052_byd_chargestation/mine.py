#name: byd charge station
#author: Bowen
#goal: to get the information about the location of byd charge station
#date: 2026/9/23
#stage: finished

import requests
import execjs
from jsonpath import jsonpath
import json
import csv

def get_page_data(url, data, data_list):
    #get the response
    response = requests.post(url, headers=headers, data=data)

    try:
        #select nodes
        element_list = jsonpath(response.json(), '$..rows[*]')
        for element in element_list:
            #select stationname
            stationname = jsonpath(element, '$.stationName')[0]
            print(stationname)
            #select address
            address = jsonpath(element, '$.address')[0]
            print(address)
            #select operatorname
            operatorname = jsonpath(element,'$.operatorName')[0]
            print(operatorname)
            #select acidle and ac
            acidle = jsonpath(element,'$.acIdleConnectorCount')[0]
            ac = jsonpath(element,'$.acConnectorCount')[0]
            ac = f'{acidle}/{ac}'
            print(ac)
            #select dcidle and dc
            dcidle = jsonpath(element,'$.dcIdleConnectorCount')[0]
            dc = jsonpath(element,'$.dcConnectorCount')[0]
            dc = f'{dcidle}/{dc}'
            print(dc)
            #select distance
            distance = f"{jsonpath(element,'$.distance')[0]}km"
            print(distance)

            data_list.append([stationname, address, operatorname, ac, dc, distance])
    except:
        print(response.text)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['地点', '地址', '管理方', '慢充桩', '快充桩', '距您'])
        writer.writerows(data_list)

if __name__ == '__main__':
    #run signMethods() in js code
    with open('xmac.js','r',encoding='utf-8') as f:
        js_code = f.read()
    xmac = execjs.compile(js_code).call('signMethods')

    data_list = []
    pages = 2
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://www.byd.com",
        "Pragma": "no-cache",
        "Referer": "https://www.byd.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        # "X-HMAC-SIGNATURE": "a32bf1b0273e12bc4e48c7ff30d98ffc1dd706f92aff50fc69ec20d9c27840b0",
        # "X-HMAC-SIGNKEY": "4a3688a5gcd88g443fga6b7fcb",
        # "X-HMAC-TIMESTAMP": "1790121810",
        "X-HMAC-SIGNATURE": xmac["X-HMAC-SIGNATURE"],
        "X-HMAC-SIGNKEY": xmac["X-HMAC-SIGNKEY"],
        "X-HMAC-TIMESTAMP": str(xmac["X-HMAC-TIMESTAMP"]),
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define web's url
    url = 'https://site-api.byd.com/domestic-official-api/charge/stations/search'
    for page in range(1, pages+1):
        #define data
        data = {"lat": "28.197500", "lng": "112.968307", "keyword": "", "pageNum": page, "pageSize": 500}
        data_json = json.dumps(data, separators=(',', ':'))
        get_page_data(url, data_json, data_list)
    save_data_csv(data_list)