#name: Anjuke_renting_messages
#author: Bowen
#goal: to get the information about the house in Anjuke
#date: 2026/8/19
#stage: going(to do: add next page function)

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
    "ctid": "27",
    "lps": "https%3A%2F%2Fcs.zu.anjuke.com%2F%7C",
    "cmctid": "414",
    "aQQ_ajkguid": "0D1D2A0E-A26D-3B39-1052-AA22C3B4821A",
    "id58": "CkwA6mqFIqwJGp4aGe+KAg==",
    "wmda_session_id_6289197098934": "1787110060432-3d4af81c-68b5-3f86",
    "wmda_visited_projects": "%3B6289197098934",
    "wmda_uuid": "e7bb657d2d34927827900158dd8757d0",
    "wmda_new_uuid": "1",
    "xxzlclientid": "df9cb063-d1d3-4fd0-a6dc-1787110062183",
    "xxzlxxid": "pfmxiOkORY8jotXY1dJh6hTgc0mwQi9q6hTDc+ARhiQuu3ql1DJD3TAwsgXI9H/kZ33O",
    "xxzlbbid": "pfmbRFrRJsD6PLEC4w+KiRlIm7hGyDmlSaOzeWD7j0ki9+4hhPNtRArTtEWG8V79oCz3Zx13PzWLTRKIjEYypD60uRzbRZXL6uMP6SAYMQ+XWy+VG/jEr1MGSV4CIO+cwbEWwOiAHGsxNzg3MTExNTYyNjczODk3_1",
    "f_session": "9520e1d55b18de7667d76101100da5cc-2"
}
#define web's url
url = 'https://cs.zu.anjuke.com/'
#get the response
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)
#translate response to tree structure
html_tree = etree.HTML(response.text)

#move to the same note
element_list = html_tree.xpath('//div[@class="zu-itemmod clearfix"]')

#sep
print('='*75)

#select the information about houses
for element in element_list:
    #select the house info
    house_info = element.xpath('./div[1]')[0]
    # print(house_info)
    #house introduction
    intro = house_info.xpath('./h3/a/b/text()')[0]
    print(f'房子简介: {intro}')
    #house structure
    structure1 = house_info.xpath('./p[1]/text()')
    structure1[4] = structure1[4].replace(' ', '')
    structure2 = house_info.xpath('./p[1]/b/text()')
    print(f'房子规格: {structure2[0]}{structure1[1]}{structure2[1]}{structure1[2]} {structure2[2]}{structure1[3]} {structure1[4]}')
    #house address
    address1 = house_info.xpath('./address/a/text()')[0]
    address2 = house_info.xpath('./address/text()')
    address2[1] = address2[1].replace(' ', '').replace('\n','')
    address2[3] = address2[3].replace(' ', '')
    address2 = address2[1:4]
    print(f'房子地址: {address1}{address2[0]} | {address2[1]}| {address2[2]}')
    #house tag
    tags = house_info.xpath('./p[2]/span/text()')
    print(f'房子标签: {' '.join(tags)}')

    #select the house price
    house_price = element.xpath('./div[2]/strong/text()')[0]
    print(f'房子租金(元/月): {house_price}')

    #sep
    print('='*75)