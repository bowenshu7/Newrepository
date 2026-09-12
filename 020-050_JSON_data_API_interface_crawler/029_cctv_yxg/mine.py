#name: CCTV television program schedule
#author: Bowen
#goal: to get the information about the program schedule from CCTV
#date: 2026/9/12
#stage: finished

import requests
import json
from jsonpath import jsonpath
import csv
import time

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, params=params)
    etl_response = response.text[9:-2]
    etl_response = json.loads(etl_response)
    #select nodes
    element_list = jsonpath(etl_response,'$..list[*]')
    for element in element_list:
        #select title
        title = jsonpath(element,'$.title')[0]
        print(title)
        #select image
        image = jsonpath(element,'$.image')[0]
        print(image)
        #select tv's url
        tv_url = jsonpath(element,'$.url')[0]
        print(tv_url)
        #select publish year
        year = jsonpath(element,'$.year')[0]
        print(year)
        #select publish area
        area = jsonpath(element,'$.area')[0]
        print(area)
        #select publish count
        count = jsonpath(element,'$.count')[0]
        print(count)
        #select actors
        actors = jsonpath(element,'$.actors')
        actors = actors[0] if actors else ''
        print(actors)
        #select brief
        brief = jsonpath(element,'$.brief')
        brief = brief[0] if brief else ''
        print(brief)

        data_list.append([title,image,tv_url,year,area,count,actors,brief])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','封面','详情链接','推出年份','区域','集数','主演','概要'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://tv.cctv.com/",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "cross-site",
        "sec-fetch-storage-access": "active",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define web's url
    url = 'https://api.cntv.cn/list/getVideoAlbumList'
    for page in range(1, pages + 1):
        #define params
        params = {
            "channelid": "CHAL1460955853485115",
            "area": "",
            "sc": "",
            "fc": "电视剧",
            "year": "",
            "letter": "",
            "p": "1",
            "n": "24",
            "serviceId": "tvcctv",
            "topv": page,
            "t": "jsonp",
            "cb": "Callback"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)