#name: youzy tzy search collegeList
#author: Bowen
#goal: to get the information about the collect list from youzy
#date: 2026/9/26
#stage: finished

import requests
import json
import execjs
from jsonpath import jsonpath
import csv
import time

def get_page_data(url, data, data_list):
    data = json.dumps(data, separators=(',', ':'))
    # get the response
    response = requests.post(url, headers=headers, data=data)

    # select nodes
    element_list = jsonpath(response.json(), '$..items[*]')
    for element in element_list:
        # select code
        code = jsonpath(element, '$.code')[0]
        print(code)
        # select name
        name = jsonpath(element, '$.cnName')[0]
        print(name)
        # select college url
        college_url = f'https://www.youzy.cn/accounts/login?fromUrl=/colleges/detail?collegeCode={code}'
        print(college_url)
        # select features
        features = jsonpath(element, '$.features[*]')
        feature = ','.join(features) if features else ''
        print(feature)
        # select province
        province = jsonpath(element, '$.provinceName')[0]
        # select city
        city = jsonpath(element, '$.cityName')[0]
        address = f'{province} {city}'
        print(address)
        # select category
        category = jsonpath(element, '$.categories[0]')[0]
        print(category)
        # select belong
        belong = jsonpath(element, '$.belong')[0]
        print(belong)
        # select rank
        ranking = jsonpath(element, '$.ranking')[0]
        print(ranking)
        # select diffscore
        diff = jsonpath(element, '$.diffScore')[0]
        print(diff)
        # select hits
        hits = jsonpath(element, '$.hits')[0]
        print(hits)

        data_list.append([code, name, college_url, feature, address, category, belong, ranking, diff, hits])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['院校编号', '院校名称', '详情网址', '院校特点', '院校地址', '院校类别', '所属部门', '院校排名', '难度系数', '热度'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    #define web's url
    url = 'https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query'
    pages = int(input("Enter page number: "))
    with open('reverse.js','r',encoding='utf-8') as f:
        js_code = f.read()
    e = "/youzy.dms.basiclib.api.college.query"
    for page in range(1,pages+1):
        # define data
        data = {
            "keyword": "",
            "provinceNames": [],
            "natureTypes": [],
            "eduLevel": "",
            "categories": [],
            "features": [],
            "pageIndex": page,
            "pageSize": 20,
            "sort": 11
        }
        xsign = execjs.compile(js_code).call('u',e,data)
        #define headers
        headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://pv4y-pc.youzy.cn",
            "Pragma": "no-cache",
            "Referer": "https://pv4y-pc.youzy.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
            "agent": "objectId:;provinceId:;provinceCode:;userPermissionId:;score:0;",
            "deviceId": "co407e8445f22f7eee21cb6dd3a46b1b46nt",
            "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "u-dfs": "web",
            "u-sign": xsign,
            "u-token;": "",
            "x-hmac": "9d00b3a055108855ec1619b2687faf4c3deb51a0fda53b66ee731d43cea4d060",
            "x-nonce": "786174046995c784625ee506dc59bf7c",
            "x-timestamp": "1790396418",
            "x-version": "2.0.0"
        }
        get_page_data(url, data, data_list)
        time.sleep(3)
    save_data_csv(data_list)
