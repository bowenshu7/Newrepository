#name: adidas clothes sale
#author: Bowen
#goal: to get the information about the adidas clothes
#date: 2026/9/16
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(),'$.content[*]')
    for element in element_list:
        #select name
        articlename = jsonpath(element,'$.articleName')[0]
        print(articlename)
        #select subtitle
        subtitle = jsonpath(element,'$.subTitle')[0]
        print(subtitle)
        #select price
        discountprice = jsonpath(element,'$.discountPrice')
        saleprice = jsonpath(element,'$.salePrice')
        price = discountprice[0] if discountprice else saleprice[0]
        price = '￥'+str(price)
        print(price)
        #select recommendedpercentage
        recommendedpercentage = jsonpath(element,'$.recommendedPercentage')
        recommendedpercentage = recommendedpercentage[0]+'的顾客推荐' if recommendedpercentage else '暂无'
        print(recommendedpercentage)

        data_list.append([articlename,subtitle,price,recommendedpercentage])
def save_data_csv(data_list):
    t = time.localtime()
    with open(f'{t.tm_year}{t.tm_mon:02d}{t.tm_mday:02d}.csv','w',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['产品名称','标签','价格','推荐值'])
        writer.writerows(data_list)

if __name__ == '__main__':
    pages = 3
    data_list = []
    #define headers
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://www.adidas.com.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.adidas.com.cn/",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "x-source": "COM"
    }
    #define cookies
    cookies = {
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221a0a81ba595d0a-0baf17633d5047-26071b51-1327104-1a0a81ba5961883%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a0a81ba595d0a-0baf17633d5047-26071b51-1327104-1a0a81ba5961883%22%7D",
        "acw_tc": "af0c633417895267804696194ec9874ba8ea6c19eeedd5ed3bd74b903b",
        "cdn_sec_tc": "af0c633417895267804696194ec9874ba8ea6c19eeedd5ed3bd74b903b"
    }
    #define web's url
    url = 'https://ecp-public.api.adidas.com.cn/o2srh/v1/pub/platform-products/search'
    for page in range(1, pages + 1):
        #define params
        params = {
            "page": page,
            "pageSize": "24",
            "abTest": "A",
            "categoryCode": "/sp_football_app_male"
        }
        get_page_data(url, data_list)
        time.sleep(2)
    save_data_csv(data_list)

