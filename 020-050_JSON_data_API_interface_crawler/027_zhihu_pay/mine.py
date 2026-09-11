#name: zhihu payable consult
#author: Bowen
#goal: to get the information about the zhihu payable consult
#date: 2026/9/11
#stage: finished

import requests
from jsonpath import jsonpath
import csv


def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(),'$..data[*]')
    for element in element_list:
        #select name
        name = jsonpath(element,'$.fullname')[0]
        print(name)
        #select expert's url
        expert_id = jsonpath(element,'$.id')[0]
        expert_url = f'https://www.zhihu.com/consult/people/{expert_id}?hideHomeBar=1'
        print(expert_url)
        #select conversation_count
        conversation_count = jsonpath(element,'$.conversation_count')[0]
        print(conversation_count)
        #select score
        score = jsonpath(element,'$.score')[0]
        score = round(score / 100)
        print(score)
        #select price
        price = jsonpath(element,'$.question_price')[0]
        print(price)
        #select content
        content = jsonpath(element,'$.description')[0]
        content = content if content else '这个人很懒，什么都没写'
        print(content)

        data_list.append([name,expert_url,conversation_count,score,price,content])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['专家','链接','咨询人数','评分','价格','简介'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    # pages = 0
    # while pages < 1 or pages > 9:
    #     pages = int(input(''))
    #define headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.zhihu.com/consult",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "x-requested-with": "fetch"
    }
    #define cookies
    cookies = {
        "_zap": "857e74ff-85b2-454a-9474-d4b9c606bcfb",
        "_xsrf": "zCsu6upUcLCA8fN3osjrQC6GvWVeOqON",
        "BEC": "c838835709364588babacf97e45319e7"
    }
    #define web's url
    url = 'https://www.zhihu.com/api/v4/infinity/hot_responders'
    for page in range(pages):
        # define params
        params = {
            "limit": "10",
            "offset": f"{page * 10}"
        }
        get_page_data(url,data_list)
    # save_data_csv(data_list)