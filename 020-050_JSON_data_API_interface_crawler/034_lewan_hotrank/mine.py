#name: baidu lewan rankland hot games
#author: Bowen
#goal: to get the information about the hot games from baidu lewan rankland
#date: 2026/9/14
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time

def get_page_data(url, data_list,rank):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(), '$..list[*]')
    for element in element_list:
        #rank
        rank += 1
        print(rank)
        #select name_cn
        name_cn = jsonpath(element, '$.gameName')[0]
        print(name_cn)
        #select name_en
        name_en = jsonpath(element, '$.gameNameEn')
        name_en = name_en[0] if name_en[0] else '暂无'
        print(name_en)
        #select score
        score = jsonpath(element,'$.gameScore')
        score = score[0] if score[0] else '暂无'
        print(score)
        #select types
        types = jsonpath(element,'$.gameTypes[*]')
        types = '/'.join(types)
        print(types)
        #select game's url
        gameurl = jsonpath(element, '$.gameUrl')[0]
        print(gameurl)
        #select queryindex
        queryindex = jsonpath(element,'$.gameQueryIndex')[0]
        print(queryindex)
        #select game desc
        desc = jsonpath(element,'$.gameDesc')[0]
        print(desc)

        data_list.append([rank,name_cn,name_en,score,types,gameurl,queryindex,desc])

    return rank
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['排名','中文名','英文名','评分','类型','游戏链接','点击次数','简介'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    rank = 0
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://lewan.baidu.com/rankland",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-h5-refer": "https://lewan.baidu.com/rankland",
        "x-requested-with": "xmlhttprequest"
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
        "Hm_lvt_90624d8970c669347df5969a13eafa11": "1789369650",
        "Hm_lpvt_90624d8970c669347df5969a13eafa11": "1789369650",
        "HMACCOUNT": "876958FB013481E3",
        "RT": "\"z=1&dm=baidu.com&si=is429esc4fd&ss=mu0whmcq&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf\""
    }
    #define web's url
    url = 'https://lewan.baidu.com/lewanapi'
    for page in range(1, pages + 1):
        #define params
        params = {
            "action": "aladdin_rank_games_by_type",
            "page": page,
            "typeId": "0",
            "gameSource": "standalone"
        }
        rank = get_page_data(url, data_list,rank)
        time.sleep(1)
    save_data_csv(data_list)