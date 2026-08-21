#name: poetry web
#author: Bowen
#goal: to get the information about the poetry web
#date: 2026/8/21
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
    "login": "flase",
    "Hm_lvt_9007fab6814e892d3020a64454da5a55": "1787284016",
    "Hm_lpvt_9007fab6814e892d3020a64454da5a55": "1787284016",
    "HMACCOUNT": "876958FB013481E3"
}

def get_poem(page):
    #define web's url
    url = 'https://www.gushiwen.cn/shiwens/default.aspx'
    if page > 1:
        url = url + f'?page={page}'

    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)
    #sep
    print('='*75)

    #select the same node
    element_list = html_tree.xpath('//div[@class="cont"]/div[2]')[1:]
    #select the poems
    for element in element_list:
        title = element.xpath('.//b/text()')
        title = title[0] if title else '无名'
        print('诗文名:', title)
        poet = element.xpath('./p[2]/a/text()')
        poet = ''.join(poet).strip() if poet else '佚名'
        print('作者:',poet)
        poem = element.xpath('./div//text()')
        poem = poem[1:] if poem[0]=='\n' else poem
        poem = poem[:-1] if poem[-1]=='\n' else poem
        while poem[0].strip() == '':
            poem = poem[1:]
        poem[0] = poem[0].replace('\n', '')
        poem[-1] = poem[-1].replace('\n', '')
        poem = '\n'.join(poem)
        print(f'内容:\n{poem}')

        #sep
        print('='*75)



if __name__ == '__main__':
    pages = int(input('Enter the number of pages: '))
    for page in range(1, pages + 1):
        get_poem(page)
        print(f'{'-'*32}第{page}页抓取完毕{'-'*32}')