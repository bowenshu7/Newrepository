#name: Sina International News
#author: Bowen
#goal: to get the information about the world in Sina Weibo
#date: 2026/8/24
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
    "SSCSum": "1",
    # "NowDate": "Mon Aug 24 2026 09:40:26 GMT+0800 (ä¸­å›½æ ‡å‡†æ—¶é—´)",
    "name": "sinaAds",
    "post": "massage",
    "UOR": ",news.sina.com.cn,",
    "ULV": "1787535626572:1:1:1::",
    "SINAGLOBAL": "118.248.178.106_1787535626.915939",
    "Apache": "118.248.178.106_1787535626.915941"
}
#define web's url
url = 'https://news.sina.com.cn/world/'
#get the response
response = requests.get(url, headers=headers, cookies=cookies)
#set charset 'utf-8'
response.encoding = 'utf-8'
# print(response.text)
#translate response to tree structure
html_tree = etree.HTML(response.text)

#sep
print('='*75)

#select the same node
element_list = html_tree.xpath('//div[contains(@id,"subShowContent1_news")]/div')
# print(len(element_list),element_list)
#select news
for element in element_list:
    #select title
    title = element.xpath('./h2/a/text()')[0]
    print('新闻标题: ',title)
    #select news' url
    comment_url = element.xpath('./h2/a/@href')[0]
    print('新闻网址: ',comment_url)
    #select date
    date = element.xpath('./div/div/text()')[0]
    print('发布日期: ',date)

    #sep
    print('='*75)
