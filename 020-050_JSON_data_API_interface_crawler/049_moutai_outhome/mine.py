#name: moutai outhome plan list
#author: Bowen
#goal: to get the information about the moutai outhome plan list
#date: 2026/9/19
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time

def get_page_data(url, data, data_list):
    #get the response
    response = requests.post(url, headers=headers, data=data)

    #select nodes
    element_list = jsonpath(response.json(), '$..Rows[*]')
    for element in element_list:
        #select title
        title = jsonpath(element,'$.FTITLE')[0]
        print(title)
        #select start time
        stime = jsonpath(element,'$.FSTIME')[0]
        print(stime)
        #select end time
        etime = jsonpath(element,'$.FETIME')[0]
        print(etime)

        data_list.append([title, stime, etime])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题', '开始时间', '结束时间'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 3
    #define headers
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://zp.moutai.com.cn",
        "Pragma": "no-cache",
        "Referer": "https://zp.moutai.com.cn/outhome/planList",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define web's url
    url = 'https://zp.moutai.com.cn/outhome/findPlanData'
    for page in range(1, pages + 1):
        # define data
        data = f'page={page}&pagesize=50'.encode('utf-8', 'surrogateescape')
        get_page_data(url, data, data_list)
        time.sleep(1)
    save_data_csv(data_list)