#name: vivo smartphone list
#author: Bowen
#goal: to get the information about the vivo smartphone
#date: 2026/9/19
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time


def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(), '$..dataList[*]')
    for element in element_list:
        #select skuname
        skuname = jsonpath(element, '$.skuName')[0]
        print(skuname)
        #select brief
        brief = jsonpath(element,'$.brief')[0]
        print(brief)
        #select price
        saleprice = jsonpath(element,'$.salePrice')[0]
        saleprice = '￥'+str(saleprice) if saleprice < 999999 else '￥待发布'
        print(saleprice)
        #select picture
        picture = jsonpath(element,'$.images[0].hdPic')[0]
        print(picture)
        #select vivo url
        vivo_id = jsonpath(element,'$.id')[0]
        vivo_url = f'https://shopact.vivo.com.cn/pcspace/wk260914bd31ab61?skuId={vivo_id}'
        print(vivo_url)

        data_list.append([skuname, brief, saleprice, picture, vivo_url])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['型号','简介','销售价','图片链接','详情网址'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://shop.vivo.com.cn/product/list-1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        ".thumbcache_77352f771aaa31eaeebd60722ce25500": "",
        "smidV2": "202609191534037ae7045bcfec7b221634bc81041362520010b2d34a9270c40",
        "shop_outer_refer": "https%3A%2F%2Fshop.vivo.com.cn%2Fproduct%2Flist-1",
        "shop_token": "AnZkEIDK-LVSbzmM5ThhQwmo9Q",
        "vivo_fe_vftcookid": "44bf64f4cf704b358886cfc3c989d497",
        "vivo_fe_vftsessionid": "aa68b4961df24238be5ba9fc42d5b5e5",
        "login_flag_tmp": "0"
    }
    #define web's url
    url = 'https://shop.vivo.com.cn/api/v1/prodList/list-1'
    for page in range(1, pages + 1):
        # define params
        params = {
            "pageNum": page,
            "pageSize": "12",
            "t": "1789803243631"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)