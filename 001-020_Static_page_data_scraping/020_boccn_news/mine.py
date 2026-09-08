#name: Chinese bank news
#author: Bowen
#goal: to get the information about the news from Chinese bank
#date: 2026/9/7
#stage: going

import requests
from lxml import etree
import csv


def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//ul[@class="list"]/li')
    for element in element_list:
        #select title
        title = element.xpath('./a/text()')[0]
        print(title)
        #select passage's url
        pag = element.xpath('./a/@href')[0]
        pag = pag.replace('.','https://www.boc.cn/aboutboc/bi1',1)
        print(pag)
        #select time
        pub_time = element.xpath('./span/text()')[0]
        pub_time = pub_time.split(' ')[1]
        print(pub_time)

        data_list.append([title,pag,pub_time])
def save_data_csv(data_list):
    with open('boc.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','网页链接','发布时间'])
        writer.writerows(data_list)

if __name__ == '__main__':
    #define headers
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    data_list = []
    pages = 3
    # define web's url
    for page in range(pages):
        if page == 0:
            url = 'https://www.boc.cn/aboutboc/bi1/'
        else:
            url = f'https://www.boc.cn/aboutboc/bi1/index_{page}.html'
        get_page_data(url,data_list)
        print(f'第{page+1}页已抓取')
    save_data_csv(data_list)