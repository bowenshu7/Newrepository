#name: yiche news
#author: Bowen
#goal: to get the information about the latest news from yiche web
#date:2026/9/5
#stage: finished

import requests
from lxml import etree
import csv
import time

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)
    print(response)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)

    #select nodes
    element_list = html_tree.xpath('//div[@class="article-card"]/div')
    for element in element_list:
        #select title
        title = element.xpath('./div/h2/a/text()')[0]
        print(title)
        #select passage's url
        pag_url = element.xpath('./div/h2/a/@href')[0]
        pag_url = 'https://news.yiche.com' + pag_url
        print(pag_url)
        #select image's url
        img_url = element.xpath('./a/img/@data-original')[0]
        print(img_url)
        #select content
        content = element.xpath('./div/p/text()')
        content = content[0] if content else '暂无'
        print(content)
        #select author
        author = element.xpath('./div/div/div/a/text()')[0]
        print(author)
        #select date
        date = element.xpath('./div/div/div/span/text()')[0]
        print(date)
        #sep
        print('='*75)
        data_list.append([title,pag_url,img_url,content,author,date])
    time.sleep(3)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','文章链接','图片链接','简介','作者','日期'])
        writer.writerows(data_list)

if __name__ == '__main__':
    # define headers
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
    # define cookies
    cookies = {
        "UserGuid": "e17dc2150c4f88ef224b444d6b28b1bb",
        "tws2_1104958253": "3M66ABdZnq1RtDIT66LjlUquEjEifTohlg==",
        "CIGUID": "e17dc2150c4f88ef224b444d6b28b1bb",
        "suid": "zqs0fhae8jaufxnykfcwkg7kwodbeoa6",
        "Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44": "1788578435",
        "HMACCOUNT": "876958FB013481E3",
        "locatecity": "430100",
        "bitauto_ipregion": "118.248.176.56%3A%E6%B9%96%E5%8D%97%E7%9C%81%E9%95%BF%E6%B2%99%E5%B8%82%3B1301%2C%E9%95%BF%E6%B2%99%E5%B8%82%2Cchangsha",
        "isWebP": "true",
        "auto_id": "8724b4ec28bf3ce288d0b611fe0e2b7c",
        "CIGDCID": "rFjYHHkm8QyE7fHmsMieX4tTMrf6Yn5Z",
        "selectcity": "430100",
        "selectcityid": "1301",
        "selectcityName": "%E9%95%BF%E6%B2%99",
        "selectcityPinyin": "changsha",
        "report-cookie-id": "121687989_1788580788580",
        "Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44": "1788580789"
    }
    data_list = []
    pages = 3
    # define web's url
    for page in range(1, pages + 1):
        url = f'https://news.yiche.com/info/categoryId0_p0_l0_f0_g0_c0_b0_{page}.html'
        get_page_data(url,data_list)
        print(f'{page}页抓取完毕')
    save_data_csv(data_list)