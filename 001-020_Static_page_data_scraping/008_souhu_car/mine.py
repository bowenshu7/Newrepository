#name: souhu car sales volume
#author: Bowen
#goal: to get the information about the sales volume
#date: 2026/8/31
#stage: finished

import requests
from lxml import etree

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
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}
#define cookies
cookies = {
    "_sa_84db345b": "1788167209",
    "_sa": "vL7DWJCSNE1S_gW",
    "IPLOC": "CN4401",
    "SUV": "260831170650IWFZ"
}
#define web's url
url = 'https://db.auto.sohu.com/carsales'
#get the response
response = requests.get(url, headers=headers, cookies=cookies)
#translate html to tree structure
html_tree = etree.HTML(response.text)

#select area
title = html_tree.xpath('//div[@class="sale-data-province--label"]/text()')[0]
print(title)
#select month
month = html_tree.xpath('//span[@class="sale-data--month"]/text()')[0]
print(month)
#select total
total = html_tree.xpath('//ul[@class="sale-data-total"]//text()')
car_total = ''.join(total[:3])
print(car_total)
new_energy = ''.join(total[3:])
print(new_energy)
#select price
price_total = html_tree.xpath('//div[@class="sale-data-price"]//text()')
print(f'{price_total[0]}:')
for i in range(1,len(price_total),2):
    print(price_total[i],price_total[i+1])
#select level
level_total = html_tree.xpath('//div[@class="sale-data-level"]')[0]
level_title = level_total.xpath('./h4/text()')[0]
print(f'{level_title}:')
level_ul = level_total.xpath('./ul')
for ul in level_ul:
    line1_pro = ul.xpath('./li[1]/text()')[0]
    line1_after = ul.xpath('./li[2]/div[1]//text()')
    print(line1_pro, ' '.join(line1_after))
    for div in ul.xpath('./li[2]/div[2]/div'):
        trend_info = div.xpath('./@class')[0]
        trend = ''
        if 'up' in trend_info:
            trend = '增长'
        elif 'down' in trend_info:
            trend = '减少'
        brand = div.xpath('.//text()')[0]
        print(trend, brand)

    print('='*20)