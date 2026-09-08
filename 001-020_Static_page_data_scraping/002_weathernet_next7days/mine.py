#name: weathernet_next7days
#author: Bowen
#goal: to get the information about the weather next 7 days in Changsha
#date: 2026/8/19
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
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}
#define cookies
cookies = {
    "sessionId": "uniqueSessionIdValue",
    "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b": "1787100912",
    "Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b": "1787100912",
    "HMACCOUNT": "876958FB013481E3",
    "userNewsPort0": "1",
    "f_city": "%E9%9B%A8%E8%8A%B1%7C101250111%7C"
}
#define web's url
url = 'https://www.weather.com.cn/weather/101250101.shtml'
#get response
response = requests.get(url, headers=headers, cookies=cookies)

#set the charset 'utf-8'
response.encoding = 'utf-8'

#translate response to tree structure
html_tree = etree.HTML(response.text)

#move to the note of the weather
element_list = html_tree.xpath('//ul[@class="t clearfix"]/li')
# print(element_list)

#sep
print('='*75)

#select the day one by one
for element in element_list:
    #get the date
    date = element.xpath('./h1/text()')[0]
    print(f'日期: {date}')

    #get the weather
    weather = element.xpath('./p[1]/text()')[0]
    print(f'天气: {weather}')

    #get the temperature
    highest = element.xpath('./p[2]/span/text()')[0]
    lowest = element.xpath('./p[2]/i/text()')[0]
    print(f'气温: {highest}~{lowest}')

    #get the wind
    #get wind direction
    direction = element.xpath('./p[3]/em/span/@title')
    print(f'风向: {' -> '.join(direction)}')
    #get wind force
    force = element.xpath('./p[3]/i/text()')[0]
    print(f'风力: {force}')

    #sep
    print('='*75)
print('长沙近7日的天气信息已全部获取')