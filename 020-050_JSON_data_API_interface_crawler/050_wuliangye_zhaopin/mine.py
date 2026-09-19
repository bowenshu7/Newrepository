#name: wuliangye zhaopin announcement
#author: Bowen
#goal: to get the announcement about the wuliangye zhaopin
#date: 2026/9/19
#stage: finished

import requests
from jsonpath import jsonpath
import time
import csv


def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, params=params)

    #select nodes
    element_list = jsonpath(response.json(), '$..data[*]')
    for element in element_list:
        #select title
        title = jsonpath(element, '$.title')[0]
        print(title)
        #select publish time
        datum = jsonpath(element, '$.datum')[0]
        print(datum)
        #select passage url
        pag_id = jsonpath(element,'$.guid')[0]
        pag_url = f'https://www.wuliangye.com.cn/zhaopin/announcement/article?guid={pag_id}'
        print(pag_url)

        data_list.append([title, datum, pag_url])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题', '发布时间', '文章链接'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.wuliangye.com.cn/zhaopin/announcement",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define web's url
    url = 'https://www.wuliangye.com.cn/zhaopin/sap_api/sap/bc/zhr/zhr'
    for page in range(1, pages + 1):
        #define params
        params = {
            "sap-client": "800",
            "method": "HR-NOTICE",
            "pagenum": page,
            "rownum": "10"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)