#name: fotile city list
#author: Bowen
#goal: to get the information about the fotile city list
#date: 2026/9/18
#stage: finished

import requests
from jsonpath import jsonpath
import time
import csv
import json


def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(), '$..list[*]')
    for element in element_list:
        #select name
        storename = jsonpath(element,'$.storeName')[0]
        print(storename)
        #select shop url
        shop_id = jsonpath(element,'$.id')[0]
        shop_url = f'https://www.fotile.com/service/storeDetail.html?id={shop_id}'
        print(shop_url)
        #select distance
        distance = jsonpath(element,'$.distance')[0]
        distance = distance if float(distance) < 9999 else '距离太远'
        print(distance)
        #select coverurl
        coverurl = jsonpath(element,'$.coverurl')[0]
        coverurl_json = json.loads(coverurl)
        cover_json = jsonpath(coverurl_json,'$.[0].url')[0]
        print(cover_json)

        data_list.append([storename, distance, cover_json])
def save_data_list(data_list):
    with open('fotile_citylist.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['店名', '详情链接', '距离', '店面'])
        writer.writerows(data_list)

if __name__ == '__main__':
    pages = 2
    data_list = []
    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.fotile.com/service/city/queryCity.html",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    #define cookies
    cookies = {
        "acw_tc": "76b20f6217897031418268099ed99ff50ce9655f19da2a14429ae4db6c1d87"
    }
    #define web's url
    url = 'https://www.fotile.com/service/findPlainStoreInfoByAreaCode'
    for page in range(1, pages + 1):
        #define params
        params = {
            "userLatitude": "",
            "userLongitude": "",
            "pagination": page,
            "size": "9",
            "areaCode": "330200000000"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_list(data_list)