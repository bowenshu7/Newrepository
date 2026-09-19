#name: mihome list
#author: Bowen
#goal: to get the information about the shop list from mihome
#date: 2026/9/19
#stage: finished

import requests
from jsonpath import jsonpath
import csv

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(), '$..zm[*]')
    for element in element_list:
        #select name
        store_name = jsonpath(element,'$.store_name')[0]
        print(store_name)
        #select address
        address = jsonpath(element,'$.address')[0]
        print(address)
        #select telephone number
        tel = jsonpath(element,'$.tel')[0]
        print(tel)
        #select open time
        open_time = jsonpath(element,'$.shop_time')[0]
        print(open_time)

        data_list.append([store_name, address, tel, open_time])
def save_data_list(data_list):
    with open('data_list.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['店名', '地址', '电话号码', '营业时间'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://www.mi.com",
        "Pragma": "no-cache",
        "Referer": "https://www.mi.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "X-User-Agent": "channel/mishop platform/mishop.pc",
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        "_utm_data": "{\"mtm\":\"\",\"device_id\":\"\"}",
        "xmuuid": "XMGUEST-B1443E90-B402-11F1-B0C9-BF58271B4600",
        "xmUuid": "XMGUEST-B1443E90-B402-11F1-B0C9-BF58271B4600",
        "XM_agreement": "0",
        "mstuid": "1789805908254_8266",
        "xm_vistor": "1789805908254_8266_1789805908260-1789805908260",
        "mstz": "||519567477.10|||",
        "pageid": "ea91881615b5c25e",
        "Hm_lvt_c3e3e8b3ea48955284516b186acf0f4e": "1789805908",
        "Hm_lpvt_c3e3e8b3ea48955284516b186acf0f4e": "1789805908",
        "HMACCOUNT": "876958FB013481E3",
        "deviceId": "xmdevice_3wdb3vmdlq075zbr",
        "mishopDeviceId": "Bnt2hFviFoC3uUrH1YHg4SXox5SsH9mTi6F0GJCTwvezRhOni1TR0MnHWnWOKwjm4TEKko8K00zoZSDl4UmqCbQ=="
    }
    #define web's url
    url = 'https://api2.service.order.mi.com/store/store_list'
    # define params
    params = {
        "area_type": "2",
        "area_id": "36",
        "area_name": "北京市",
        "t": "1789805910"
    }
    get_page_data(url, data_list)
    save_data_list(data_list)