#name: juejin hot articles
#author: Bowen
#goal: to get the information about the popular articles from jujin web
#date: 2026/9/10
#stage: finished

import requests
from jsonpath import jsonpath
import json
import time
import csv

def get_page_data(url, data, data_list):
    #get the response
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    #select nodes
    element_list = jsonpath(response.json(), '$..data[*]')
    for element in element_list:
        #select title
        title = jsonpath(element,'$.base_info.title')[0]
        print(title)
        #select book url
        book_id = jsonpath(element,'$.booklet_id')[0]
        book_url = 'https://juejin.cn/book/' + book_id
        print(book_url)
        #select summary
        summary = jsonpath(element,'$.base_info.summary')[0]
        print(summary)
        #select username
        username = jsonpath(element, '$.user_info.user_name')[0]
        print(username)
        #select price
        price = jsonpath(element, '$.max_discount.pay_money')[0]/100
        print(price)
        #select section count
        section = jsonpath(element, '$.base_info.section_count')[0]
        print(section)
        #select buy count
        buy_count = jsonpath(element, '$.base_info.buy_count')[0]
        print(buy_count)

        data_list.append([title, book_url, summary, username, price, section, buy_count])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题', '链接', '简介', '作者', '价格/￥', '课程数', '购买人数'])
        writer.writerows(data_list)

if __name__ == '__main__':
    pages = 2
    data_list = []
    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://juejin.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://juejin.cn/",
        "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
        "x-secsdk-csrf-token": "0001000000017fb199dbb8f201204aa8705fe0b195e4a2fabf8cabc50349fc90116d23486a9118d977ef3a820ca5"
    }
    #define cookies
    cookies = {
        "_tea_utm_cache_2608": "undefined",
        "__tea_cookie_tokens_2608": "%257B%2522web_id%2522%253A%25227683822385058137652%2522%252C%2522user_unique_id%2522%253A%25227683822385058137652%2522%252C%2522timestamp%2522%253A1789029319534%257D",
        "passport_csrf_token": "6dfe2be8d9c0ecebb56db0385f72cdd3",
        "passport_csrf_token_default": "6dfe2be8d9c0ecebb56db0385f72cdd3",
        "csrf_session_id": "72e8a572343da2ffd8b7a8eac1e89425"
    }
    #define web'a url
    url = 'https://api.juejin.cn/booklet_api/v1/booklet/listbycategory'
    #define params
    params = {
        "aid": "2608",
        "uuid": "7683822385058137652",
        "spider": "0"
    }
    for page in range(pages):
        # define data
        data = {"category_id": "0", "cursor": str(page * 20), "sort": 10, "is_vip": 0, "limit": 20}
        data = json.dumps(data, separators=(',', ':'))
        get_page_data(url, data, data_list)
        time.sleep(1)
    save_data_csv(data_list)