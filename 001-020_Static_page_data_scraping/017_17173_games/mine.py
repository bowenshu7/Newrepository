#name: 17173 hot games
#author: Bowen
#goal: to get the information about the hot games from 17173 web
#date: 2026/9/6
#stage: finished

import requests
from lxml import etree
import csv

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #tranlate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//ul[@class="list-plate js-rank"]/li/div')
    for element in element_list:
        #select rank
        rank = element.xpath('./div[1]/em/text()')[0]
        print(rank)
        #select name
        name = element.xpath('./div[2]/div/a/text()')[0]
        print(name)
        #select game's url
        game_url = element.xpath('./div[2]/div/a/@href')[0]
        game_url = 'https:'+game_url
        print(game_url)
        #select tickets
        tickets = element.xpath('./div[3]/text()')[0]
        tickets = tickets.replace('\n','').strip()
        print(tickets)
        #select time
        pub_time = element.xpath('./div[5]/text()')[0]
        pub_time = pub_time.replace('\n','').strip()
        print(pub_time)
        #select image's url
        img_url = element.xpath('./div[7]/a/img/@src')[0]
        print(img_url)
        #select content
        content = element.xpath('./div[7]/p/text()')[0]
        content = content.replace('\n','').strip()
        print(content)

        data_list.append([rank,name,game_url,tickets,pub_time,img_url,content])

        #sep
        print('='*75)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['排行','游戏名','游戏链接','票数','发行时间','图片链接','简介'])
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
        "SUV": "17886807931406538231",
        "SUV_SEC": "17886807931406538231",
        "PHPSESSID": "89cbed11f4d997753239339b4b4f88f6",
        "FID": "0ab654865bf339d27424d33af2d026bf",
        "OKIDEA_AD_BI_COOKIE_ID": "ece4fe9890ef4184bebd2f15eeabdd14"
    }
    data_list = []
    pages = 2
    # define web's url
    for page in range(1,pages+1):
        url = f'https://top.17173.com/list-2-0-0-0-0-0-0-0-0-0-{page}.html'
        get_page_data(url,data_list)
        print(f'第{page}抓取完毕')
    save_data_csv(data_list)