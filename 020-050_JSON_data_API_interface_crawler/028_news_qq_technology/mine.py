#name: tengxun news in the technology category
#author: Bowen
#goal: to get the information about the tengxun news in the technology category
#date: 2026/9/11
#stage: going

import requests
import json
from jsonpath import jsonpath
import csv
import time

def get_page_data(url,data_list,data):
    #get the response
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    #select nodes
    element_list = jsonpath(response.json(),'$.data[*]')
    for element in element_list:
        #select articletype
        articletype = jsonpath(element,'$.articletype')[0]
        if articletype != "0" and articletype != "4":
            continue
        #select title
        title = jsonpath(element,'$.title')[0]
        print(title)
        #select link_url
        link_url = jsonpath(element,'$.link_info.url')[0]
        print(link_url)
        #select publishtime
        publish_time = jsonpath(element,'$.publish_time')[0]
        print(publish_time)
        #select publisher
        publisher = jsonpath(element,'$.media_info.chl_name')[0]
        print(publisher)
        #select description
        desc = jsonpath(element,'$.desc')[0]
        print(desc)

        data_list.append([title,link_url,publish_time,publisher,desc])

    time.sleep(1)
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','详情链接','发布时间','发布人','简介'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 5
    #define headers
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://news.qq.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://news.qq.com/",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define cookies
    cookies = {
        "pac_uid": "0_cYJEEjPp3wWHD",
        "omgid": "0_cYJEEjPp3wWHD",
        "current-city-name": "changsha",
        "_qimei_uuid42": "1a90b0f1f131002724127fe37ccad4c6c1698fd91c",
        "_qimei_fingerprint": "3c4f74f2b9b6614bd29548eedfcf2dcd",
        "_qimei_q36": "",
        "_qimei_h38": "2db8b34c24127fe37ccad4c60200000b01a90b"
    }
    #define web's url
    url = 'https://i.news.qq.com/web_feed/getPCList'
    #define data
    for page in range(1, pages + 1):
        data = {"base_req":{"from":"pc"},"forward":"2","qimei36":"0_cYJEEjPp3wWHD","device_id":"0_cYJEEjPp3wWHD","flush_num": page,
                "channel_id": "news_news_tech", "item_count": 12, "is_local_chlid": "0"}
        # etl data
        data = json.dumps(data, separators=(',', ':'))
        get_page_data(url, data_list, data)
        print('='*32,f'{page}','='*32)
    save_data_csv(data_list)