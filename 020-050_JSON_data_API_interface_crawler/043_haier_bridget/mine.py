#name: haier refrigerators
#author: Bowen
#goal: to get the information about haier refrigerators
#date: 2026/9/18
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time


def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(), '$..data[*]')
    for element in element_list:
        #select name
        name = jsonpath(element,'$.pname')[0]
        print(name)
        #select modelno
        modelno = jsonpath(element,'$.modelno')[0]
        print(modelno)
        #select image url
        img_url = 'https://image.haier.com/cn/cooling/'+jsonpath(element,'$.appFile')[0]
        print(img_url)
        #select price
        price = '￥'+str(jsonpath(element,'$.price')[0])
        print(price)
        #select labelname
        labelname = jsonpath(element,'$.labelName')
        labelname = labelname[0][:-4] if labelname else '暂无'
        print(labelname)

        data_list.append([name, modelno, img_url, price, labelname])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['名字', '编号', '图片链接', '价格', '标签'])
        writer.writerows(data_list)

if __name__ == '__main__':
    pages = 2
    data_list = []
    #define headers
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "cch": "1G42E696DF_G378C9D8",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://www.haier.com/cooling/?spm=cn.products_pc.header_1_20241118.1",
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
        "_trs_uv": "mu6deave_259_e00b",
        "_trs_ua_s_1": "mu6deave_259_6wxq",
        "token": "f0810c2e-f7c7-4a2a-84d8-9a1ac5b00137",
        "uuid": "f0810c2e-f7c7-4a2a-84d8-9a1ac5b00137",
        "_h_cur_co_inv": "e4b0a870bc224dcebe506ebc1976da66-17897003796356799",
        "h_trs_frequency_1": "1",
        "F8CF2A14": "94FF7D44GC",
        "AE43CGEG": "DE34F2AB7B",
        "CFEG32EA": "E429424398",
        "2F84F2E6": "GGDF6FD342",
        "G378C9D8": "1G42E696DF"
    }
    #define web's url
    url = 'https://www.haier.com/igs/front/cn_product/getProduct'
    for page in range(1, pages + 1):
        #define params
        params = {
            "code": "3e6bff6304c547dba650d9941aa472c0",
            "searchWord": "(channelId=38345) and (psale=0)",
            "pageNo": page,
            "pageSize": "18",
            "siteId": "2",
            "aggs": "",
            "filterJsonUrl": "https://www.haier.com/cn/cooling/filter_es.json",
            "orderBy": "hotProduct:desc,saleProduct:desc,productWt:desc,productAllWt:desc",
            "filter": "",
            "defaultSearch": "(channelId=38345) and (psale=0)",
            "retFilterJson": "yes",
            "searchColumns": "productShowLabel,productBigClassName,productClassName"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)