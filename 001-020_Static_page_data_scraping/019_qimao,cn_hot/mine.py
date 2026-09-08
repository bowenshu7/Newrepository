#name: qimao Chinese hot books
#author: Bowen
#goal: to get the information about the hot books from qimao web
#date: 2026/9/7
#stage: finished

import requests
from lxml import etree
import csv


def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//li[@class="rank-list-item"]/div')
    for element in element_list:
        #select rank
        rank = element.xpath('./div[1]/a/span/text()')[0]
        print(rank)
        #select cover page's url
        cover_url = element.xpath('./div[1]/a/img/@src')[0]
        print(cover_url)
        #select title
        title = element.xpath('./div[2]/div/a/text()')[0]
        print(title)
        #select the book's url
        book_url = element.xpath('./div[2]/div/a/@href')[0]
        print(book_url)
        #select tags
        tags = element.xpath('./div[2]/span[1]//text()')
        tags = f'{tags[0]} | {tags[3]} • {tags[6]} | {tags[9]} | {tags[12]}'
        print(tags)
        #select content
        content = element.xpath('./div[2]/span[2]/text()')[0]
        content = content.replace('\n\n', '\n')
        print(content)
        #select the latest news
        news = element.xpath('./div[2]/span[3]/a/text()')[0]
        news = news.replace('\n','').strip()
        print(news)
        #select time
        pub_time = element.xpath('./div[2]/span[3]/em/text()')[0]
        print(pub_time)
        #select honor
        honor = element.xpath('./div[3]/div[1]//text()')
        honor = '/'.join(honor) if honor else ''
        print(honor)
        #select hot
        hot = element.xpath('./div[3]/div[2]/span/em/text()')
        trend = element.xpath('./div[3]/div[2]/span/i/@class')[0]
        if 'drop' in trend:
            trend = '下降'
        else:
            trend = '上升'
        book_info = f'{hot[0]}{hot[1]} {hot[2]}:{trend}'
        print(book_info)

        data_list.append([rank,cover_url,title,book_url,tags,content,news,pub_time,honor,book_info])

        #sep
        print('='*75)
def save_data_csv(data_list):
    with open('data.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['排名','图片链接','标题','文章链接','标签','简介','上次更新','时间','荣誉','热度'])
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
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        "acw_tc": "0000000017887440544426703e5fc5f1fb294ca20ab9fe5c93657544c711d4",
        "Hm_lvt_1b6d0fc94c391c78c2fbeda715896432": "1788744055",
        "HMACCOUNT": "876958FB013481E3",
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221a07974384cec7-00596827e477f554-26071b51-1327104-1a07974384d18b1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMWEwNzk3NDM4NGNlYzctMDA1OTY4MjdlNDc3ZjU1NC0yNjA3MWI1MS0xMzI3MTA0LTFhMDc5NzQzODRkMThiMSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a07974384cec7-00596827e477f554-26071b51-1327104-1a07974384d18b1%22%7D",
        "Hm_lpvt_1b6d0fc94c391c78c2fbeda715896432": "1788744094"
    }
    data_list = []
    # define web's url
    url = 'https://www.qimao.com/paihang/boy/hot/date/'
    get_page_data(url,data_list)
    save_data_csv(data_list)