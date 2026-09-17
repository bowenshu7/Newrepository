#name: kukahome goods
#author: Bowen
#goal: to get the information about the kukahome goods
#date: 2026/9/17
#stage: finished

import time
import requests
import json
from jsonpath import jsonpath
import csv

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, params=params)
    json_data = json.loads(response.text)

    #select nodes
    element_list = jsonpath(json_data, '$.data.list[*]')
    for element in element_list:
        #select item name
        item_name = jsonpath(element,'$.item_name')[0]
        print(item_name)
        #select  brief
        brief = jsonpath(element,'$.brief')[0]
        brief = brief if brief else '暂无'
        print(brief)
        #select price
        price_info = jsonpath(element,'$.price')[0]
        price = '￥'+str(price_info*0.01)
        print(price)
        #select image url
        img_url = jsonpath(element,'$.pics[0]')[0]
        print(img_url)

        data_list.append([item_name, brief, price, img_url])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['产品名称', '简介', '价格', '图片链接'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer null",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://www.kukahome.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define web's url
    url = 'https://b.kukahome.com/api/h5app/wxapp/goods/items'
    for page in range(1, pages + 1):
        #define params
        params = {
            "is_star": "false",
            "category": "",
            "page": page,
            "pageSize": "20",
            "item_type": "normal",
            "goodsSort": "",
            "attribute_id": "",
            "is_point": "false",
            "company_id": "2"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)