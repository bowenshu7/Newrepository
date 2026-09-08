#name: wangyi house news
#author: Bowen
#goal: to get the information about the house from wangyi's web
#date: 2026/9/3
#stage: finished

import requests
from lxml import etree
import csv

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select  nodes
    element_list = html_tree.xpath('//div[@class="list-item clearfix"]')
    for element in element_list:
        #select title
        title = element.xpath('./h2/a/text()')[0]
        #select title's url
        news_url = element.xpath('./h2/a/@href')[0]
        #select time
        pub_time = element.xpath('./p/span/text()')[0]
        data_list.append([title,news_url,pub_time])

def save_data_csv(data_list):
    with open('house_data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['title','news_url','pub_time'])
        writer.writerows(data_list)

if __name__ == '__main__':
    #define headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
    }
    #define cookies
    cookies = {
        "_ntes_nnid": "5874350a306ed2eecff611be2cefdfd3,1774310147727",
        "_ntes_nuid": "5874350a306ed2eecff611be2cefdfd3",
        "NTES_P_UTID": "1p7vGcO4xgu1xAH9xJq7xzQFHzqES8DM|1779758619",
        "P_INFO": "oldisnew0@163.com|1779758619|0|mail163|00&99|hun&1779606377&unireg#hun&null#10#0#0|&0|mail163&unireg|oldisnew0@163.com",
        "Hm_lvt_db91d2aef1b333f155cccbb9496c8424": "1788399058",
        "HMACCOUNT": "876958FB013481E3",
        "Hm_lpvt_db91d2aef1b333f155cccbb9496c8424": "1788399081"
    }
    data_list = []
    pages = int(input())
    for page in range(1,pages+1):
        # define web's url
        if page == 1:
            url = 'https://cs.house.163.com/special/021198NN/DCTT.html'
        else:
            url = f'https://cs.house.163.com/special/021198NN/DCTT_{page:02}.html'
        get_page_data(url,data_list)
    save_data_csv(data_list)