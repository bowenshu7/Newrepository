#name: douyu live cover image
#author: Bowen
#goal: to get the images of douyu live
#date: 2026/9/16
#stage: finished

import requests
from jsonpath import jsonpath
import os


def download_page_images(url):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies)

    #select nodes
    element_list = jsonpath(response.json(),'$..rl[*]')
    for element in element_list:
        # select title
        title = jsonpath(element, '$.rn')[0]
        print(title)
        #select user's name
        uname = jsonpath(element,'$.nn')[0]
        print(uname)
        # select image's url
        img_url = jsonpath(element, '$.rs16')[0][:-4]
        print(img_url)
        #download the image
        with open(f'./douyu/{uname}.jpg', 'wb') as f:
            f.write(requests.get(img_url,headers=headers,cookies=cookies).content)

if __name__ == '__main__':
    pages = 4 #(max=4)
    if not os.path.exists('douyu'):
        os.mkdir('douyu')
    #define headers
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.douyu.com/g_xingxiu",
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
        "Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7": "1789519878",
        "Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7": "1789519878",
        "HMACCOUNT": "876958FB013481E3",
        "dy_did": "9d4fd07dd5034d7ee38a0fc100051701",
        "acf_did": "9d4fd07dd5034d7ee38a0fc100051701",
        "_ga_5JKQ7DTEXC": "GS2.1.s1789519878$o1$g0$t1789519878$j60$l0$h733302194",
        "_ga": "GA1.1.363223942.1789519879",
        "acf_ssid": "1729747294842960058",
        "acf_web_id": "7685929355846883854",
        "acf_ab_pmt": "20100212%23webnewhome%23B%2C20100254%23WebTool0703%23new%2C20100249%23webTagRank%23B%2C20100248%23webTagHover%23B%2C20100272%23all_lists_sort%23c",
        "acf_ab_ver_all": "20100212%2C20100254%2C20100249%2C20100248%2C20100272",
        "acf_ab_vs": "webnewhome%3DB%2CWebTool0703%3Dnew%2CwebTagRank%3DB%2CwebTagHover%3DB%2Call_lists_sort%3Dc",
        "acf_ccn": "2df0f985efecce7761d5229a706da7f1"
    }
    for page in range(1, pages + 1):
        # define web's url
        url = f'https://www.douyu.com/wgapi/ordnc/live/web/room/mixList/2/1008/0/{page}'
        download_page_images(url)
