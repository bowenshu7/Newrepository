#name: Samsclub shoplist in China
#author: Bowen
#goal: to get the shop list of Samsclub in China
#date: 2026/9/15
#stage: going

import requests
import re
import json5
from jsonpath import jsonpath
import csv

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers)
    # print(response.text)
    #build re rule
    json_re = r'r=(\[.*?\]),N'
    result = re.findall(json_re, response.text)[0]
    # print(result)


    #select nodes
    element_list = json5.loads(result)
    for element in element_list:
        #select city
        city = jsonpath(element,'$.city')[0]
        print(city)
        #select en
        en = jsonpath(element,'$.cityEn')[0]
        print(en)
        #select shops
        shops = jsonpath(element,'$.shops[*]')
        for shop in shops:
            #select shopName
            shopName = jsonpath(shop,'$.shopName')[0]
            print(shopName)
            #select shopAddress
            shopAddress = jsonpath(shop,'$.shopAddress')[0]
            print(shopAddress)
            #select  openTime
            openTime = jsonpath(shop,'$.openTime')[0]
            print(openTime)

            data_list.append([city, en, shopName, shopAddress, openTime])

        print('='*75)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['城市', '英文名', '店名', '地址', '营业时间'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.samsclub.cn/",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "cross-site",
        "sec-fetch-storage-access": "active",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define web's url
    url = 'https://sams-home-online-1302115363.file.myqcloud.com/p__shopList__shopList.3b85fe8f.async.js'
    get_page_data(url, data_list)
    save_data_csv(data_list)