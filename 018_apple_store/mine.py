#name: Apple Store
#author: Bowen
#goal: to get the information about the Apple stores from apple_store_list
#date: 2026/9/6
#stage: finished

import requests
from lxml import etree
import csv


def get_data_list(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//div[@class="state"]')
    for element in element_list:
        #select state
        state = element.xpath('./h2//text()')[0]
        print(state)
        #select stores
        stores = element.xpath('./div/div')
        for store in stores:
            print()
            #select area
            area1 = store.xpath('./div/span/text()')[0]
            area2 = store.xpath('./div/span/a/text()')[0]
            area = f'{area1},{area2}'
            print(area)
            #select address
            address = store.xpath('./div/address/text()')[0]
            print(address)
            #select telephone number
            tele = store.xpath('./div/address/text()')[1]
            print(tele)

            data_list.append([state,area,address,tele])

        #sep
        print('='*75)

def save_data_csv(data_list):
    with open('data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['省/市','地区','地址','电话'])
        writer.writerows(data_list)

if __name__ == '__main__':
    #define headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define cookies
    cookies = {
        "geo": "CN"
    }
    data_list = []
    # define web's url
    url = 'https://www.apple.com.cn/retail/storelist/'
    get_data_list(url,data_list)
    save_data_csv(data_list)