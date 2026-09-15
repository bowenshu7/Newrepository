#name: baidu AI image
#author: Bowen
#goal: to get the information about AI images from baidu
#date: 2026/9/15
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time
import os

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(),'$..inspirations[*]')
    for element in element_list:
        #select image
        image_url = jsonpath(element,'$.img')[0]
        print(image_url)
        #select ratio
        ratio = jsonpath(element,'$.ratio')[0]
        print(ratio)
        #select description
        desc = jsonpath(element,'$.description')[0]
        print(desc)
        #select labels
        labels = jsonpath(element,'$.labels[*].label')[0]
        print(labels)

        data_list.append([image_url, ratio, desc, labels])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['图片', '比例', '提示词', '标签'])
        writer.writerows(data_list)
def download_image(data_list):
    rank = 0
    for data in data_list:
        rank += 1
        response = requests.get(data[0], headers=headers, cookies=cookies)
        print(response.status_code)
        if response.status_code == 200:
            with open(f'./baidu/{rank}.jpg', 'wb') as f:
                f.write(response.content)

if __name__ == '__main__':
    data_list = []
    pages = 1
    if not os.path.exists('baidu'):
        os.mkdir('baidu')
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://image.baidu.com/",
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
        "BIDUPSID": "6A4C7516FD0D880B2EEBB945D4DEFBF9",
        "PSTM": "1772890005",
        "BAIDUID": "6A4C7516FD0D880BAC8914C8EEEF3961:FG=1",
        "BAIDUID_BFESS": "6A4C7516FD0D880BAC8914C8EEEF3961:FG=1",
        "__bid_n": "1a022af12622256e11279b",
        "ZFY": "ZWvx9nBInW8KfNmwwiGoSkXzNFpoJfbAWNzlZqvp:BLE:C",
        "H_PS_PSSID": "63141_65590_72659_72726_72943_73010_73025_73054_73296_73322_73284_73340_73376_73448_73683_73646_73744_73787_73796_73792_73791_73798_73832_73877_73906_73920_73923_73951_73962_73995_74010_74013_73977_74054_74061_74144_74174_74371_74262_74256_74317_74344_74214_74204_74307_74463_74455_74366_74401_74395_74391_74502_74506_74522_74534_74533_74548_74485_74588_74600_74642_74643_74668_74666_74671_74700_74735_74679_74763_74662_74730_74673_74783_74793",
        "BAIDU_WISE_UID": "wapp_1789035859912_450",
        "RT": "\"z=1&dm=baidu.com&si=is429esc4fd&ss=mu0whl1e&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2p2&ul=197z2&hd=197zk\"",
        "H_WISE_SIDS": "65590_72726_73010_73296_73322_73284_73376_73787_73798_73832_73906_73962_74038_74054_74061_74371_74262_74256_74317_74344_74214_74204_74307_74366_74401_74395_74391_74502_74522_74534_74533_74548_74485_74588_74642_74643_74668_74666_74700_74735_74679_74763_74662_74730_74783_74793_74826_74837_74835_74839_74859_74890_74902_74894_74899_74909_74914_74942_74937_74944",
        "ab_sr": "1.0.1_ZjRmNDE2MDRjODBmNjRiOGFiMjQ0ZmFlYWJkNTBkNDcyNzcxZDRmMDY2NWFlNDU4ZDk1NGIwMWYyODI0YzM3OGI3YWE4YWRmYjg4ZjNjMzc1MmZiNzU4YWMzNmYzZTljYWYzZDllNGNiZGY4NDQ3NmIwYTJjMTc2ZjM1NzE4NWY1NzQwOWI1MDc4OGIyOTEyMjRjZTc1N2IxOWE2ZDBkZWY0NzcxODk4ODE0ZjkwY2VlNzNjNzM2NWM1YTBjYTBk"
    }
    #define web's url
    url = 'https://image.baidu.com/aigc/inspirepics'
    for page in range(pages):
        # define params
        params = {
            "pn": page * 20,
            "rn": "20"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)
    download_image(data_list)

