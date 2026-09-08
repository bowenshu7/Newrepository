#name: 4399 game information
#author: Bowen
#goal: to get the information about games from 4399 web
#date: 2026/9/4
#stage: finished

import requests
from lxml import etree
import csv
import time

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #set charset
    response.encoding = 'gb2312'
    #translate response to tree structure
    html_tree = etree.HTML(response.text)
    #sep
    print('='*75)

    #select nodes
    element_list = html_tree.xpath('//ul[@class="list affix cf"]/li/a')
    for element in element_list:
        #select name
        name = element.xpath('./img/@alt')[0]
        print(name)
        #select game's url
        game_url = element.xpath('./@href')[0]
        if '//' not in game_url:
            game_url = '//www.4399.com'+game_url
        game_url = 'https:'+game_url
        print(game_url)
        #select image's url
        img_url = element.xpath('./img/@lz_src')[0]
        img_url = 'https:'+img_url
        print(img_url)

        data_list.append([name,game_url,img_url])

        #sep
        print('='*75)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['游戏名','游戏链接','图片链接'])
        writer.writerows(data_list)


if __name__ == '__main__':
    #define headers
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.4399.com/flash_fl/2_1.htm",
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
        "_4399stats_vid": "1788490149518904",
        "UM_distinctid": "1a06a51f0d555b-01235e6be249f98-26071b51-144000-1a06a51f0d6e88",
        "Hm_lvt_334aca66d28b3b338a76075366b2b9e8": "1788490150",
        "HMACCOUNT": "876958FB013481E3",
        "CNZZDATA30039538": "cnzz_eid%3D197468038-1788490150-%26ntime%3D1788490210",
        "Hm_lpvt_334aca66d28b3b338a76075366b2b9e8": "1788490211",
        "webanlytics2020userinfo": "%7B%22distinct_id%22%3A%22cf2b5c4d87125141b1234402bbe42f4a%22%2C%22vid%22%3A%22cf2b5c4d87125141b1234402bbe42f4a%22%2C%22createTime%22%3A1788490211840%7D"
    }
    data_list = []
    pages = 1
    # define web's url
    for page in range(1,pages+1):
        if page == 1:
            url = 'https://www.4399.com/flash_fl/2_1.htm'
        else:
            url = f'https://www.4399.com/flash_fl/more_2_{page}.htm'
        get_page_data(url,data_list)
        time.sleep(1)
    save_data_csv(data_list)