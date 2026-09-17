#name: Converse man shoes
#author: Bowen
#goal: to get the information about the man shoes from Converse web
#date: 2026/9/17
#stage: finished

import requests
from jsonpath import jsonpath
import time
import csv
import json

def get_page_data(url, data_list, rank):
    #get the response
    response = requests.get(url, headers=headers, params=params)
    try:
        #select nodes
        element_list = jsonpath(response.json(), '$..edges[*].node')
        for element in element_list:
            rank += 1
            print(rank)
            #select title
            title = jsonpath(element, '$.title')[0]
            print(title)
            #select sale price
            sale_price = jsonpath(element, '$.salePrice')[0]
            print(sale_price)
            #select list price
            list_price = jsonpath(element, '$.listPrice')
            list_price = list_price[0] if list_price else '暂无'
            print(list_price)
            #select  image url
            img_url = jsonpath(element,'$.mediaList[0].url')[0]
            print(img_url)

            data_list.append([rank, title, sale_price, list_price, img_url])
        return rank
    except Exception as e:
        print(e)
        print(response.status_code)
        return 0
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['排名', '标题', '售价', '折后价', '图片链接'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    rank = 0
    pages = 3
    #define headers
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://www.converse.com.cn",
        "Pragma": "no-cache",
        "Referer": "https://www.converse.com.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "UNEX-CHANNEL-CODE": "100",
        "UNEX-STORE-CODE": "Converse0419",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "accept": "*/*",
        "content-type": "application/json",
        "device-token;": "",
        "saastenantcode": "CONVERSE",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define web's url
    url = 'https://api-os.converse.com.cn/api/graphql/searchProductsByRoleGql'
    for page in range(pages):
        after = page*20-1 if page>0 else None
        #define params
        variables = {
            "input": {
                "pageInput": {
                    "after": after,
                    "first": 20
                },
                "searchInput": {
                    "conditionRoot": {
                        "operator": "AND",
                        "conditions": [
                            {
                                "fqRule": "NOT",
                                "key": "isCBY",
                                "userSelection": 'true',
                                "value": "Y"
                            },
                            {
                                "operator": "OR",
                                "conditions": [
                                    {
                                        "operator": "AND",
                                        "conditions": [
                                            {
                                                "fqRule": "IN",
                                                "combineType": "ATTR",
                                                "key": "extFirstCategory",
                                                "value": "FT"
                                            },
                                            {
                                                "fqRule": "IN",
                                                "key": "saleStatus",
                                                "value": 1
                                            },
                                            {
                                                "fqRule": "IN",
                                                "combineType": "ATTR",
                                                "key": "extGender",
                                                "value": "male"
                                            },
                                            {
                                                "fqRule": "NOT",
                                                "combineType": "ATTR",
                                                "key": "isCBY",
                                                "value": "Y"
                                            }
                                        ]
                                    },
                                    {
                                        "operator": "AND",
                                        "conditions": [
                                            {
                                                "fqRule": "IN",
                                                "combineType": "ATTR",
                                                "key": "extFirstCategory",
                                                "value": "FT"
                                            },
                                            {
                                                "fqRule": "IN",
                                                "combineType": "ATTR",
                                                "key": "extGender",
                                                "value": "general"
                                            },
                                            {
                                                "fqRule": "IN",
                                                "key": "saleStatus",
                                                "value": 1
                                            },
                                            {
                                                "fqRule": "NOT",
                                                "combineType": "ATTR",
                                                "key": "isCBY",
                                                "value": "Y"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "sort": [
                        {
                            "orderField": "hasInventory",
                            "order": "DESC"
                        },
                        {
                            "orderField": "TOP_top-plp",
                            "order": "ASC"
                        },
                        {
                            "orderField": "WEIGHT_search",
                            "order": "DESC"
                        }
                    ]
                }
            },
            "attrCodes": [],
            "userRole": "VISITOR"
        }
        variables = json.dumps(variables)
        params = {#first page is after null, the followings are 19, 39, 59 ...
            "operationName": "searchProductsByRoleGql",
            "variables": variables,
            "extensions": "{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"ba20c669fdb74d1588f409bf978365d2cd8fd7029bb1828631dc45845d7b8b58\"}}"
        }
        rank = get_page_data(url, data_list, rank)
        time.sleep(1)
    save_data_csv(data_list)