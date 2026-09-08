#name: changsha baixing web's cars
#author: Bowen
#goal: to get the information about the used cars from changsha baixing web
#date: 2026/9/5
#stage: finished

import requests
from lxml import etree
import csv
import time

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//li/div[@class="media-body"]')
    for element in element_list:
        #select price
        price = element.xpath('./div[1]/span/text()')
        price = price[0] if price else '未知'
        print(price)
        #select title
        title = element.xpath('./div[1]/a[1]/text()')[0]
        print(title)
        #select passage's url
        pag = element.xpath('./div[1]/a[1]/@href')[0]
        print(pag)
        #select tags
        tags = element.xpath('./div[1]/a[starts-with(@class,"tag")]/text()')
        tags = ' | '.join(tags)
        print(tags)
        #select place
        place = element.xpath('./div[2]/text()')[0]
        print(place)
        #select ad_info
        ad_info = element.xpath('./div[3]//text()')
        ad_info = ''.join(ad_info)
        print(ad_info)

        data_list.append([title, pag, price, tags, place, ad_info])

    time.sleep(3)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["标题", "链接", "价格", "表签", "位置", "信息"])
        writer.writerows(data_list)

if __name__ == '__main__':
    #define headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://changsha.baixing.com/cheliang/",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define cookies
    cookies = {
        "__trackId": "4096539876016095",
        "__city": "changsha",
        "c0fc276cce08ba22dc": "2380e8744ef9803a3f8ca48893be1301",
        "c1fc276cce08ba22dc": "2a9c267119a92727c1e8a8b4851ac9142db",
        "bxf": "2a9c267119a92727c1e8a8b4851ac9142db",
        "sbxf": "2a9c267119a92727c1e8a8b4851ac9142db",
        "__s": "0pq9j4k17qdal4k8e073vjj2e7",
        "__sense_session_pv": "2",
        "Hm_lvt_5a727f1b4acc5725516637e03b07d3d2": "1788570892",
        "Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2": "1788570892",
        "HMACCOUNT": "876958FB013481E3"
    }
    data_list = []
    pages = 2
    # define web's url
    for page in range(1, pages+1):
        url = f'https://changsha.baixing.com/cheliang/?page={page}'
        get_page_data(url, data_list)
    save_data_csv(data_list)