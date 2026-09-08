#name: IT's home blog news
#author: Bowen
#goal: to get the information about blog news from IT's home
#date: 2026/9/2
#stage: finished

import csv
import requests
from lxml import etree

def get_data_list(url):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)
    #create a list
    data_list = []
    #select nodes
    element_list = html_tree.xpath('//ul[@class="bl"]/li/div')
    for element in element_list:
        #exclude advertisements and select content
        content_list = element.xpath('./div[@class="m"]/text()')
        content = ''
        if content_list:
            content = content_list[0]
        else:
            continue
        #select title
        title = element.xpath('./h2/a/text()')[0]
        #select tags
        tags_list = element.xpath('./div[@class="o"]/div[1]/a/text()')
        tags = ','.join(tags_list)
        #select url
        new_url = element.xpath('../a/@href')[0]
        data_list.append([title, content, tags, new_url])
    return data_list
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['标题', '简介', '标签', '链接'])
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
        "Hm_lvt_cfebe79b2c367c4b89b285f412bf9867": "1788313829",
        "Hm_lpvt_cfebe79b2c367c4b89b285f412bf9867": "1788313829",
        "HMACCOUNT": "876958FB013481E3"
    }
    # define web's url
    url = 'https://www.ithome.com/blog/'
    data = get_data_list(url)
    save_data_csv(data)