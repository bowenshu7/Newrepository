#name: qimao Chinese hot books
#author: Bowen
#goal: to get the information about the hot books from qimao web
#date: 2026/9/8
#stage: finished

import requests
from jsonpath import jsonpath
import csv


def get_page_data(url,data_list,rank):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    #select nodes
    element_list = jsonpath(response.json(),'$..table_data[*]')
    for element in element_list:
        #select rank
        rank = rank + 1
        print(rank)
        #select cover page's url
        cover_url = jsonpath(element,'$.image_link')[0]
        print(cover_url)
        #select title
        title = jsonpath(element,'$.title')[0]
        print(title)
        #select the book's url
        book_url = jsonpath(element,'$.book_url')[0]
        print(book_url)
        #select tags
        tag1 = jsonpath(element,'$.author')[0]
        tag2 = jsonpath(element,'$.category1_name')[0]
        tag3 = jsonpath(element,'$.category2_name')[0]
        tag4 = '已完结' if jsonpath(element,'$.is_over')[0] else '连载中'
        tag5 = jsonpath(element,'$.words_num')[0]
        tags = f'{tag1} | {tag2} • {tag3} | {tag4} | {tag5}'
        print(tags)
        #select content
        content = jsonpath(element,'$.intro')[0]
        print(content)
        #select the latest news
        news = f'最近更新  {jsonpath(element,'$.latest_chapter_title')[0]}'
        print(news)
        #select time
        update_time = jsonpath(element,'$.update_time')[0]
        print(update_time)
        #select hot
        hot = f'{jsonpath(element,'$.number')[0]}{jsonpath(element,'$.unit')[0]}'
        trend = jsonpath(element,'$.index_change')[0]
        if trend:
            trend = '上升'
        else:
            trend = '下降'
        book_info = f'{hot} 热度:{trend}'
        print(book_info)

        data_list.append([rank,cover_url,title,book_url,tags,content,news,update_time,book_info])

        #sep
        print('='*75)
def save_data_csv(data_list):
    with open('data.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['排名','图片链接','标题','文章链接','标签','简介','上次更新','时间','热度'])
        writer.writerows(data_list)

if __name__ == '__main__':
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Authorization;": "",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.qimao.com/paihang/boy/hot/date/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221a07974384cec7-00596827e477f554-26071b51-1327104-1a07974384d18b1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMWEwNzk3NDM4NGNlYzctMDA1OTY4MjdlNDc3ZjU1NC0yNjA3MWI1MS0xMzI3MTA0LTFhMDc5NzQzODRkMThiMSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a07974384cec7-00596827e477f554-26071b51-1327104-1a07974384d18b1%22%7D",
        "acw_tc": "0000000017888493595204649e44f5479194edb9b238ec279c2b9bc19082e3",
        "Hm_lvt_1b6d0fc94c391c78c2fbeda715896432": "1788744055,1788849360",
        "HMACCOUNT": "876958FB013481E3",
        "Hm_lpvt_1b6d0fc94c391c78c2fbeda715896432": "1788849372"
    }
    data_list = []
    pages = 2
    # define web's url
    url = 'https://www.qimao.com/qimaoapi/api/rank/book-list'
    for page in range(1,pages+1):
        rank = (page-1)*20
        #define params
        params = {
            "is_girl": "0",
            "rank_type": "1",
            "date_type": "1",
            "date": "202608",
            "page": f"{page}"
        }
        get_page_data(url, data_list, rank)
    save_data_csv(data_list)