#name: tonghuashun financial news
#author: Bowen
#goal: to get the information about the financial news from tonghuashun's web
#date: 2026/9/3
#stage: finished
import requests
from lxml import etree
import csv

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//div[@class="list-con"]/ul/li')
    for element in element_list:
        #select title
        title = element.xpath('./span/a/text()')[0]
        #select page's url
        page_url = element.xpath('./span/a/@href')[0]
        #select publish time
        pub_time = element.xpath('./span/span/text()')[0]
        #select content
        content = element.xpath('./a/text()')[0]
        data_list.append([title,page_url,pub_time,content])
def save_data_csv(data_list):
    with open('data.csv', mode='w', newline='',encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['标题','链接','发布时间','简介'])
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    pages=3
    data_list = []
    for page in range(1,pages+1):
        # define web's url
        url = f'https://news.10jqka.com.cn/today_list/index_{page}.shtml'
        get_page_data(url,data_list)
    save_data_csv(data_list)