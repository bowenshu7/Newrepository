#name: eastmoney fund information
#author: Bowen
#goal: to get the information about the fund information from eastmoney web
#date: 2026/9/13
#stage: finished

import time
import requests
import json5
from jsonpath import jsonpath
import csv

def get_page_data(url,data,rank):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    #etl response text
    json_data = json5.loads(response.text[15:-1])

    #select nodes
    element_list = jsonpath(json_data, "$..datas[*]")
    for element in element_list:
        data_list = element.split(',')
        #select rank
        rank += 1
        print(rank)
        #select code name
        code_name = data_list[0]
        print(code_name)
        #select abbreviation
        abbreviation = data_list[1]
        print(abbreviation)
        #select date
        date = data_list[3]
        print(date)
        #select net unit value
        net_value = data_list[4]
        print(net_value)
        #select net sum value
        sum = data_list[5]
        print(sum)
        #select daily growth rate
        rate = data_list[6]+'%' if data_list[6] else '--'
        print(rate)
        #select week
        week = data_list[7]+'%' if data_list[6] else '--'
        print(week)
        #select month
        month = data_list[8]+'%' if data_list[6] else '--'
        print(month)

        data.append([rank, code_name, abbreviation, date, net_value, sum, rate, week, month])

    return rank
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['序号','基金代码','基金简称','日期','单位净值','累计净值','日增长率','近1周','近1月'])
        writer.writerows(data_list)

if __name__ == '__main__':
    rank = 0
    data_list = []
    pages = 2
    #define headers
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://fund.eastmoney.com/data/fundranking.html",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        "st_si": "17250238012306",
        "st_pvi": "82728945312900",
        "st_sp": "2026-09-13%2022%3A02%3A00",
        "st_inirUrl": "",
        "st_sn": "1",
        "st_psi": "20260913220200126-112200312936-2077752569",
        "st_asi": "delete",
        "ASP.NET_SessionId": "puqz05e2nkq3jr5stmjrvivu"
    }
    #define web's url
    url = 'https://fund.eastmoney.com/data/rankhandler.aspx'
    for page in range(pages):
        #define params
        params = {
            "op": "ph",
            "dt": "kf",
            "ft": "all",
            "rs": "",
            "gs": "0",
            "sc": "1nzf",
            "st": "desc",
            "sd": "2025-09-13",
            "ed": "2026-09-13",
            "qdii": "",
            "tabSubtype": ",,,,,",
            "pi": page,
            "pn": "50",
            "dx": "1",
            "v": "0.5211520698127373"
        }
        rank = get_page_data(url,data_list,rank)
        time.sleep(1)
    save_data_csv(data_list)