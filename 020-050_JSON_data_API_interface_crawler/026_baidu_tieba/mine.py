#name: baidu tieba hot news
#author: Bowen
#goal: to get the information about the hot news from baidu tieba
#date: 2026/9/10
#stage: finished

import requests
from jsonpath import jsonpath
from urllib.parse import quote
import csv

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(),'$..hot_topic_list[*]')
    rank = 0
    for element in element_list:
        #select rank
        rank += 1
        print(rank)
        #select title
        title = jsonpath(element,'$.topic_name')[0]
        print(title)
        #select topic's url
        topic_id = jsonpath(element,'$.topic_id')[0]
        topic_url = f'https://tieba.baidu.com/hottopic/browse/hottopic?topic_id={topic_id}&topic_name={quote(title)}'
        print(topic_url)
        #select topic number
        topic_num = jsonpath(element,'$.discuss_num')[0]
        print(topic_num)
        #select tag
        tag = jsonpath(element,'$.tag')[0]
        if tag == 1:
            tag = '新'
        elif tag == 2:
            tag = '热'
        elif tag == 3:
            tag = '荐'
        print(tag)

        data_list.append([rank,title,topic_url,topic_num,tag])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['排名','标题','链接','浏览数','标签'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://tieba.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-requested-with": "XMLHttpRequest"
    }
    #define cookies
    cookies = {
        "BIDUPSID": "6A4C7516FD0D880B2EEBB945D4DEFBF9",
        "PSTM": "1772890005",
        "BAIDUID": "6A4C7516FD0D880BAC8914C8EEEF3961:FG=1",
        "BAIDUID_BFESS": "6A4C7516FD0D880BAC8914C8EEEF3961:FG=1",
        "__bid_n": "1a022af12622256e11279b",
        "ZFY": "ZWvx9nBInW8KfNmwwiGoSkXzNFpoJfbAWNzlZqvp:BLE:C",
        "H_PS_PSSID": "63141_65590_72659_72726_72943_73010_73025_73054_73296_73322_73284_73340_73376_73448_73683_73646_73744_73787_73796_73792_73791_73798_73832_73877_73906_73920_73923_73951_73962_73995_74010_74013_73977_74054_74061_74144_74174_74371_74262_74256_74317_74344_74214_74204_74307_74463_74455_74366_74401_74395_74391_74502_74506_74522_74534_74533_74548_74485_74588_74600_74642_74643_74668_74666_74671_74700_74735_74679_74763_74662_74730_74673_74783_74793",
        "delPer": "0",
        "PSINO": "6",
        "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
        "BA_HECTOR": "ag0k0k018105842hak84a5018501801la4t5t28",
        "TIEBA_NEW_PC": "1",
        "TIEBA_SID": "H4sIAAAAAAAAA9MFAPiz3ZcBAAAA",
        "USER_JUMP": "-1",
        "BAIDU_WISE_UID": "wapp_1789035859912_450",
        "ab_sr": "1.0.1_YTYyNjcwNmI4OTNhY2Q4OTE5NTU0ZmM3YzI4YjVmMGY1ODU0YmIyNzk5NjhkNGQxNDgwMmM5ODY5NGVlMjJhMzczNmYxMjYzMTg4MDE2MTk5MjIxM2RhNTE2YWU3NjZkMmQ2YWEwNzdiM2YxMzNlZGMyY2NlZDNjOThhYmI2YWY3NzBmMTk3Yjc1Yzk1NzQ0YmIyNDlmY2Q5NzdjNzQ1M2I2ZTJkMzFjYjRhNmRmODEzNDU5Njc4OWRiMmY1ZDFiYjM3ODMyYmRlYTFiZjFhOWY3MTIyYmU4MTcwYzcxOWI=",
        "TIEBAUID": "cb23caae14130a0d384a57f1"
    }
    #define web's url
    url = 'https://tieba.baidu.com/c/f/pc/homeSidebarRight'
    # define params
    params = {
        "subapp_type": "pc",
        "_client_type": "20",
        "sign": "e9b101df871c39eedcf9a232c2d26ec8"
    }
    get_page_data(url,data_list)
    save_data_csv(data_list)