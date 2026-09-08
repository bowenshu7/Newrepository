#name: CSDN_blog
#author: Bowen
#goal: to get the information about the CSDN blog
#date: 2026/8/21
#stage: finished

import requests
from lxml import etree

#define headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://blog.csdn.net/ityouknow?type=blog",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
#define cookies
cookies = {
    "bc_bot_session": "178727660602b756932d6a8521",
    "https_ydclearance": "c15ef461409d3223b8a1c4c3-160e-4d0f-aa02-455dc622001a-1787283806",
    "https_waf_cookie": "3432c674-4036-484ea992887a78547bdfa133b530bea41bc4",
    "uuid_tt_dd": "10_19960103570-1787276607253-228835",
    "dc_session_id": "10_1787276607253.582439",
    "waf_captcha_marker": "28c128a6b2ceca8e49248655209bfdbb888d6a4132e8a6830a2577382a5a1893",
    "c_pref": "",
    "c_ref": "https%3A//blog.csdn.net/ityouknow%3Ftype%3Dblog",
    "fid": "20_66647797309-1787276607486-136679",
    "c_dsid": "11_1787276607487.406451",
    "c_segment": "3",
    "c_page_id": "default",
    "log_Id_pv": "1",
    "loginbox_strategy": "%7B%22blog-threeH-dialog-exp11tipShowTimes%22%3A1%7D",
    "popPageViewTimes": "1",
    "dc_sid": "82fd1dde5069b52f96d8674c7bc02fc6",
    "creative_btn_mp": "1",
    "bc_bot_token": "100178727660602b756932d6a852100a2fc",
    "bc_bot_rules": "-",
    "bc_bot_score": "100",
    "bc_bot_fp": "87892947dde30cb4b2519829e2d51e2a",
    "Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac": "1787276608",
    "Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac": "1787276608",
    "HMACCOUNT": "876958FB013481E3",
    "hide_login": "1",
    "_clck": "1b4940p%5E2%5Eg8s%5E0%5E2424",
    "log_Id_view": "22",
    "_clsk": "uaplst%5E1787276609851%5E1%5E0%5Ea.clarity.ms%2Fcollect",
    "dc_tos": "tk3jhv"
}
#define web's url
url = 'https://blog.csdn.net/ityouknow?type=blog'
#get the response
response = requests.get(url, headers=headers, cookies=cookies)
#translate response to tree structure
html_tree = etree.HTML(response.text)

#select the same node
element_list = html_tree.xpath('//div[@class="mainContent"]//article')
# print(len(element_list),element_list)

#sep
print('='*75)

#select the information
for element in element_list:
    #article title
    article_title = element.xpath('.//h4/text()')[0]
    article_title = article_title.replace('\n','').replace(' ','')
    print('文章标题:',article_title)
    #article info
    article_info = element.xpath('.//div[@class="blog-list-content"]/text()')[0]
    print('文章简介:',article_info)
    #article content's url
    article_url = element.xpath('./a/@href')[0]
    print('文章链接:',article_url)
    #article tags
    article_tags = element.xpath('.//div[@class="blog-list-footer-left"]')[0]
    tag1 = article_tags.xpath('./div[1]/text()')[0]
    tag1 = tag1.replace('\n','').replace(' ','')
    tag2 = article_tags.xpath('./div[2]/text()')[0]
    tag2 = tag2.replace('\n','').replace(' ','')
    tag3_1 = article_tags.xpath('./div[3]/span/text()')[0]
    tag3_2 = article_tags.xpath('./div[3]/span/span/text()')[0]
    tag4_1 = article_tags.xpath('./div[4]/span/text()')[0]
    tag4_2 = article_tags.xpath('./div[4]/span/span/text()')[0]
    tag5_1 = article_tags.xpath('./div[5]/span/text()')[0]
    tag5_2 = article_tags.xpath('./div[5]/span/span/text()')[0]
    tag6_1 = article_tags.xpath('./div[6]/span/text()')[0]
    tag6_2 = article_tags.xpath('./div[6]/span/span/text()')[0]
    print('文章标签:',f'【{tag1}】 {tag2}{tag3_1}{tag3_2}{tag4_1}{tag4_2}{tag5_1}{tag5_2}{tag6_1}{tag6_2}')

    #sep
    print('='*75)
