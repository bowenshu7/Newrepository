#name: Anta man sports shoes
#author: Bowen
#goal: to get the information about the sports shoes from Anta web
#date: 2026/9/16
#stage: finished

import requests
import json
from jsonpath import jsonpath
import csv
import time

def get_page_url(page):
    url = f'https://www.anta.com/list/f2_f1_f5_f33-j1-k2?p={page}'
    response = requests.post(url, headers=headers, cookies=cookies)
    li = jsonpath(response.json(),'$.id_goods[*]')

    #define data
    data = f'id_goods={','.join(map(str,li))}'
    return data
def get_page_data(url, data_list, data):
    #define web's url
    url_info = 'https://www.anta.com/antacom/data.Goods/getGoods'
    # get the response
    response = requests.post(url_info, headers=headers, cookies=cookies, data=data)
    json_data = json.loads(response.text)

    #select nodes
    element_list = jsonpath(json_data,'$.data[*]')
    for element in element_list:
        #select category
        category = jsonpath(element,'$.info.pro_title')[0]
        print(category)
        #select price
        price = jsonpath(element,'$.info.price')[0]
        print(price)
        #select  image
        image = jsonpath(element,'$.info.image')[0]
        print(image)
        #select shoes' url
        shoes_url_info = jsonpath(element,'$.info.url')[0]
        shoes_url = 'https://www.anta.com' + shoes_url_info
        print(shoes_url)

        data_list.append([category, price, image, shoes_url])
def save_data_csv(data_list):
    with open('data.csv','w',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['category','price','image','url'])
        writer.writerows(data_list)

if __name__ == '__main__':
    pages = 7 #(max=7)
    data_list = []
    #define headers
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.anta.com",
        "Pragma": "no-cache",
        "Referer": "https://www.anta.com/list/f2_f1_f5_f33-j1-k2",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        "acw_tc": "784e2cb617895228707466284eb55b1aef062cd379396865316070e5eae2f8",
        "Hm_lvt_3f1c198435ca184800af888ebe1a0dc3": "1789522871",
        "Hm_lpvt_3f1c198435ca184800af888ebe1a0dc3": "1789522871",
        "HMACCOUNT": "876958FB013481E3",
        "_SID": "9c1278092dc26dfe98c2437833d51920"
    }
    for page in range(1, pages + 1):
        data = get_page_url(page)
        get_page_data(page, data_list, data)
        time.sleep(3)
    save_data_csv(data_list)