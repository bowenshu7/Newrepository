#name: joyoung electrical appliances
#author: Bowen
#goal: to get the information about the joyoung appliances
#date: 2026/9/17
#stage: finished

import requests
from jsonpath import jsonpath
import time
import csv
import json

def get_page_data(url, data, data_list):
    #get the response
    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    try:
        #select nodes
        element_list = jsonpath(response.json(), '$..list[*]')
        for element in element_list:
            #select title
            title = jsonpath(element,'$.title')[0]
            print(title)
            #select selling point
            selling_point = jsonpath(element,'$.sellingPoint')[0]
            print(selling_point)
            #select image url
            img_url = jsonpath(element,'$.image')[0]
            print(img_url)
            #select product url
            pro_url = 'https://www.joyoung.com/product/detail/'+str(jsonpath(element,'$.id')[0])
            print(pro_url)
            #select price
            price = '￥'+str(jsonpath(element,'$.price')[0])
            print(price)

            data_list.append([title,selling_point,img_url,pro_url,price])
    except:
        print(response.status_code)

def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','卖点','图片链接','产品链接','价格'])
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
        "Content-Type": "application/json",
        "Origin": "https://www.joyoung.com",
        "Pragma": "no-cache",
        "Referer": "https://www.joyoung.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define web's url
    url = 'https://gateway-pub.joyoung.com/jy-website/product/getPage'
    for page in range(1, pages + 1):
        #define data
        data = {
            "page":page,
            "size":8,
            "sorter":"desc-id",
            "qp-cid-eq":23,
            "qp-categoryLevel-eq":1
        }
        data = json.dumps(data)
        get_page_data(url, data, data_list)
        time.sleep(1)
    save_data_csv(data_list)