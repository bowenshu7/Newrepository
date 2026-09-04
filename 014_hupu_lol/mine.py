#name: hupu lol hot hero message
#author: Bowen
#goal: to get the information about hero in lol from hupu web
#date: 2026/9/4
#stage: going

import requests
from lxml import etree
import csv


def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//li[@class="bbs-sl-web-post-body"]/div')
    for element in element_list:
        #select title
        title = element.xpath('./div[1]/a/text()')[0]
        print(title)
        #select passage's url
        pag = element.xpath('./div[1]/a/@href')[0]
        pag = 'https://bbs.hupu.com' + pag
        print(pag)
        #select look
        look = element.xpath('./div[2]/text()')[0]
        print(look)
        #select author
        author = element.xpath('./div[3]/a/text()')[0]
        print(author)
        #select time
        pub_time = element.xpath('./div[4]/text()')[0]
        print(pub_time)

        data_list.append([title, pag, author, pub_time])

        #sep
        print('='*75)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["标题", "文章链接", "回复/浏览", "作者", "发布时间"])
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
        "acw_tc": "2f61f27717885038251431037e767e47ddf0284c762c6f0b70eea01f7bafe1",
        "csrfToken": "ifqKO1PTRcUj1sb6IutOry-K",
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221a06b22a0118de-01d139855f7268f-26071b51-1327104-1a06b22a012936%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a06b22a0118de-01d139855f7268f-26071b51-1327104-1a06b22a012936%22%7D",
        "Hm_lvt_df703c1d2273cc30ba452b4c15b16a0d": "1788503827",
        "Hm_lpvt_df703c1d2273cc30ba452b4c15b16a0d": "1788503827",
        "HMACCOUNT": "876958FB013481E3",
        "smidV2": "20260904143706aa7b3fa7ead957f98d901eb917524e5200866add952759390",
        ".thumbcache_33f5730e7694fd15728921e201b4826a": "tZGmG4UojGY2bPKN3n9U4gu01yObxsOSkHl1P6UReoqP2lxDvONUeGqyyqcCilkC9iD6ri+5J9Th/SiKFZJg0w%3D%3D"
    }
    pages = 3
    data_list = []
    #sep
    print('='*75)
    # define web's url
    for page in range(1, pages+1):
        url = f'https://bbs.hupu.com/lol-hot-{page}'
        get_page_data(url,data_list)
    save_data_csv(data_list)
