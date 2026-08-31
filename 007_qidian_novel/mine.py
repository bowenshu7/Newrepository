#name: qidian novels
#author: Bowen
#goal: to get the information of novels in qidian novel site
#date: 2026/8/24
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
    "Referer": "https://www.qidian.com/book/1048498623/",
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
    "newstatisticUUID": "1775267392_365074624",
    "fu": "858412526",
    "Hm_lvt_f00f67093ce2f38f215010b699629083": "1775267394,1775274703",
    "supportwebp": "true",
    "x-waf-captcha-referer": "",
    "w_tsfp": "ltv2UU8E3ewC6mwF46vunEyrEz4udDkhkgBsXqNmeJ94Q7ErU5mN1oN/uML2MXDY6sxnt9jMsoszd3qAUd4ieBQSTM2Qdo4ZkB/Gy99yicxUQ0k5VYnWS1ZMK+p96DkTfW5XJ0y0i21+JIZDmOE2iw8P4nUhnvx/XvFqL5kXjB0ZufzCkpxuDW3HlFWQRzaZciVfKr/c9OtwraxQ9z/c5Vv7LFt0A6hewgfHg31dWzox6wOpaPsYd0W/Kdz3HKlw7ibwsyz1HIWur1Fkpk526UpkU4vqimqXOnQyclQ0Pk2w9L8kf6avP+4juzIMXtpdVUtG8VpK7qF8pFZFHy/sNnDZVvMo4VUGQ6Zcrp/+eivDh5O+cg1Rutkrxlg+qd8=",
    "_csrfToken": "3e279606-df53-4ae1-a705-938df6750a38"
}
#define web's url
url = 'https://www.qidian.com/book/1048498623/'
#get the response
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)
#translate response to tree structure
html_tree = etree.HTML(response.text)

count = 0
#select the book's name
name = html_tree.xpath('//h1[@id="bookName"]/text()')[0]
print('书名: ',name)
#select chapters' node
chapter_info_list = html_tree.xpath('//li[@class="chapter-item"]')
for chapter_info in chapter_info_list:
    #sep
    print('='*75)

    #select chapters' name
    chapter_name = chapter_info.xpath('./a/text()')[0]
    print(chapter_name)
    #select chapters' url
    chapter_url = chapter_info.xpath('./a/@href')[0]
    #add https: as url's head
    chapter_url = 'https:' + chapter_url
    print('本章链接: ', chapter_url)
    response = requests.get(chapter_url, headers=headers, cookies=cookies)
    # print(response.text)
    tree = etree.HTML(response.text)
    #select content in chapters
    content = tree.xpath('//main/p/text()')
    # print(content)
    content_text = '\n'.join(content)
    # print(content_text)
    content_text = '\n' + chapter_name + '\n' + content_text

    #sep
    print('='*75)
    count += 1
    print(f'{'-'*33}第{count}章结束{'-'*33}')
    with open('qidian.txt','a',encoding='utf-8') as f:
        f.write(content_text)
print('工作完成')