#name: bilibili popular weekly videos
#author: Bowen
#goal: to get the information about the popular videos from bilibili
#date: 2026/9/9
#stage: finished

import requests
from jsonpath import jsonpath
import csv

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    #select nodes
    element_list = jsonpath(response.json(),'$..list[*]')
    for element in element_list:
        #select title
        title = jsonpath(element,'$.title')[0]
        print(title)
        #select video's url
        video_url = jsonpath(element,'$.short_link_v2')[0]
        print(video_url)
        #select up
        up = jsonpath(element,'$.owner.name')[0]
        print(up)
        #select view
        view = jsonpath(element,'$.stat.view')[0]
        print(view)
        #select danmaku
        danmaku = jsonpath(element,'$.stat.danmaku')[0]
        print(danmaku)
        #select popular comment
        comment = jsonpath(element,'$.rcmd_reason')[0]
        print(comment)

        data_list.append([title,video_url,up,view,danmaku,comment])
def save_data_csv(term,data_list):
    with open(f'data{term}.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','视频链接','up','播放量','弹幕','热评'])
        writer.writerows(data_list)

if __name__ == '__main__':

    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://www.bilibili.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.bilibili.com/v/popular/weekly?num=373",
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
        "buvid3": "FC5C7972-757D-9180-060C-A14D3B11CB8A95029infoc",
        "b_nut": "1788918795",
        "_uuid": "103B25424-144C-5289-E10EB-6FE10410D610DF795830infoc",
        "buvid_fp": "c973d208d12de03e11b8bacf5ee25498",
        "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODkxNzc5OTYsImlhdCI6MTc4ODkxODczNiwicGx0IjotMX0.0n9vJu2-Fbj4xyF0bnBKXmq3_V-YhiZAeaMe1fR1NqA",
        "bili_ticket_expires": "1789177936",
        "buvid4": "6DBE7417-A5C3-AD6B-E06F-BD81E03AD84C96403-026090909-OTGv3m1SI2CPmDGHymcYdsLSVSpPDqL4X2OQyeeNTn4%3D",
        "b_lsid": "830B9AD0_1A083FB550D"
    }
    #define web's url
    url = 'https://api.bilibili.com/x/web-interface/popular/series/one'
    while True:
        data_list = []
        term = input()
        if term.isdigit():
            term = int(term)
            # define params
            params = {
                "number": f"{term}",
                "web_location": "333.934",
                "w_rid": "1c1e1f70ac087a39e66750ce3ea93f90",
                "wts": "1788920682"
            }
            get_page_data(url,data_list)
            save_data_csv(term,data_list)
        else:
            print('查询结束')
            break