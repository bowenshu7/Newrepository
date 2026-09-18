#name: opple customer products
#author: Bowen
#goal: to get the information about the opple customer products
#date: 2026/9/18
#stage: going

import requests
from jsonpath import jsonpath
import time
import csv
from urllib.parse import quote


def get_page_data(url, data, data_list):
    #get the response
    response = requests.post(url, headers=headers, cookies=cookies, data=data)

    #select nodes
    element_list = jsonpath(response.json(),'$..PageList[*]')
    for element in element_list:
        #select name
        name = jsonpath(element,'$.name')[0]
        print(name)
        #select image url
        img_url = 'https://www.opple.com.cn'+quote(jsonpath(element,'$.prodPic')[0])
        print(img_url)
        #select link
        link = jsonpath(element,'$.link')[0]
        print(link)
        #select apply
        apply = jsonpath(element,'$.apply[*]')
        apply = ','.join(apply) if apply else '暂无应用场景'
        print(apply)
        #select material
        material = jsonpath(element,'$.Material')[0]
        material = material if material else '-'
        print(material)
        #select size
        size = jsonpath(element,'$.Size')[0]
        size = size if size else '-'
        print(size)

        data_list.append([name,img_url,link,apply,material,size])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['名字','图片链接','详情链接','应用场景','材质','规格'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2#(max=18)
    #define headers
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.opple.com.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.opple.com.cn/products/customerproducts",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    #define cookies
    cookies = {
        "acw_tc": "2f646bd017897075122641019edb4f67d93df488f08e2dae477de5c821b2f7",
        "ASP.NET_SessionId": "bz5tp0v14cmgtrgok2vthebq",
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221a0b2e16d51c92-05c95bcb772f8c4-26071b51-1327104-1a0b2e16d52bb5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_latest_wx_ad_click_id%22%3A%22%22%2C%22_latest_wx_ad_hash_key%22%3A%22%22%2C%22_latest_wx_ad_callbacks%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMWEwYjJlMTZkNTFjOTItMDVjOTViY2I3NzJmOGM0LTI2MDcxYjUxLTEzMjcxMDQtMWEwYjJlMTZkNTJiYjUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221a0b2e16d51c92-05c95bcb772f8c4-26071b51-1327104-1a0b2e16d52bb5%22%7D",
        "sensorsdata2015jssdkchannel": "%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D",
        "cookieid": "3d109dd7-14c8-9dfd-f630-ebfaee261246"
    }
    #define web's url
    url = 'https://www.opple.com.cn/umbraco/surface/GetProductInfo/GetProductsNew'
    for page in range(1, pages + 1):
        #define data
        data = f'page%5BCurPage%5D={page}&page%5BPageSize%5D=9&page%5BSearch%5D%5BMaintainType%5D=1&page%5BJqSord%5D=desc'.encode(
            'utf-8', 'surrogateescape')
        get_page_data(url, data, data_list)
        time.sleep(1)
    save_data_csv(data_list)