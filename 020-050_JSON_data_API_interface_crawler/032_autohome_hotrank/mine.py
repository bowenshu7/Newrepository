#name: autohome hotrank 1
#author: Bowen
#goal: to get the information about the cars from autohome hotrank 1
#date: 2026/9/14
#stage: finished

import requests
from jsonpath import jsonpath
import csv

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(),'$..rankList[*]')
    for element in element_list:
        #select rank
        rank = jsonpath(element,'$.rank')[0]
        print(rank)
        #select title
        title = jsonpath(element,'$.title')[0]
        print(title)
        #select hottag
        hottag = jsonpath(element,'$.hotTag')[0]
        if hottag=='1':
            hottag = '新'
        elif hottag=='3':
            hottag = '热'
        print(hottag)
        #select car's url
        car_url = jsonpath(element,'$.url')[0]
        print(car_url)
        #select subTitle
        subTitle = jsonpath(element,'$.subTitle')[0]
        print(subTitle)
        #select tags
        tags = jsonpath(element,'$.seriesInfo[*].seriesName')
        tags = ' '.join(tags) if tags else '--'
        print(tags)
        #select hot score
        hotscore = jsonpath(element,'$.hotScore')[0]
        print(hotscore)

        data_list.append([rank,title,hottag,car_url,subTitle,tags,hotscore])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['排名','标题','热度标签','详情链接','简介','车型标签','热度值'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    #define headers
    headers = {
        "accept": "application/json",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.autohome.com.cn/cars/hotrank/1",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
    }
    #define cookies
    cookies = {
        "fvlid": "1775573415600izUXRHdztW",
        "sessionid": "38CA98D4-0F00-4D75-8EBD-7D46D55822B3%7C%7C2026-04-07+22%3A50%3A15.440%7C%7Cwww.baidu.com",
        "autoid": "bbe82299ebd803fa677ba8635497e8c8",
        "area": "430104",
        "cookieCityId": "430100",
        "__ah_uuid_ng": "c_38CA98D4-0F00-4D75-8EBD-7D46D55822B3",
        "sessionuid": "38CA98D4-0F00-4D75-8EBD-7D46D55822B3%7C%7C2026-04-07+22%3A50%3A15.440%7C%7Cwww.baidu.com",
        "__utma": "1.305513435.1775574279.1775574279.1775625483.2",
        "__utmz": "1.1775625483.2.2.utmcsr=autohome.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/",
        "_ac": "ORr6_y6djIU1zD9Fd_UvjFlTBlMObp7KbD6HtY4nc1CsGLRT2K07",
        "sessionip": "175.13.120.194",
        "sessionvid": "0C18C62C-D9B3-4F67-A7AB-00BF87AE96C7",
        "ahpvno": "2",
        "v_no": "3",
        "visit_info_ad": "38CA98D4-0F00-4D75-8EBD-7D46D55822B3||0C18C62C-D9B3-4F67-A7AB-00BF87AE96C7||-1||-1||3",
        "ref": "www.baidu.com%7C0%7C100124%7C0%7C2026-09-14+10%3A41%3A04.168%7C2026-04-07+22%3A50%3A15.440"
    }
    # define web's url
    url = 'https://www.autohome.com.cn/web-main/car/web/hotRank/getList'
    # define params
    params = {
        "type": "1"
    }
    get_page_data(url, data_list)
    save_data_csv(data_list)