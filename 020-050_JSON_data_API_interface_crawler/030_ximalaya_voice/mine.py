#name: ximalaya audiobook
#author: Bowen
#goal: to get the information about the audiobook from ximalaya web
#date: 2026/9/12
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time

def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    element_list = jsonpath(response.json(),'$..albums[*]')
    for element in element_list:
        #select title
        title = jsonpath(element,'$.albumTitle')[0]
        print(title)
        #select user
        user = jsonpath(element,'$.albumUserNickName')[0]
        print(user)
        #select album's url
        album_id = jsonpath(element,'$.albumId')[0]
        album_url = 'https://www.ximalaya.com/album/'+str(album_id)
        print(album_url)
        #select ispaid
        vip = jsonpath(element,'$.isPaid')[0]
        if vip:
            vip = '是'
        else:
            vip = '否'
        print(vip)
        #select isfinished
        isfinished = jsonpath(element,'$.isFinished')[0]
        if isfinished == 1:
            isfinished = '连载'
        elif isfinished == 2:
            isfinished = '完本'
        print(isfinished)
        #select intro
        intro = jsonpath(element,'$.intro')[0]
        print(intro)

        data_list.append([title,user,album_url,vip,isfinished,intro])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['标题','作者','详情链接','vip','状态','简介'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Pragma": "no-cache",
        "Referer": "https://www.ximalaya.com/category/",
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
        "HWWAFSESID": "9f6a427a20e54b9c3a8",
        "HWWAFSESTIME": "1789198398097",
        "_xmLog": "h5&ec577898-3d09-4ff6-97c6-c5a4029b7707&process.env.sdkVersion",
        "xm-page-viewid": "ximalaya-web",
        "DATE": "1789198401140",
        "wfp": "ACMwYjVhZmUxYzEwZmJhZDIzH2E0tRImUHB4bXdlYl93d3c",
        "crystal": "U2FsdGVkX1+Qcue2PMm1YtcDPkbFlN+lfuaqyOCcD4AyjpFapE0q8SVuqW/gdOTgJyImtPXDcW1Rka1WoxTGUKvCVoj4kdSnIbHkHsvdkTmtB8W1yN92S2x0NiaJ7pQGWXewSsipQgsxWgLLYlVE0L/c1Y+qDBuEHXb1USk7GRSTpa100EPmsMjlwb/ZBeSU2JPBBhMFWX0aIzIG/mK89DF6dM2uoQVDr22+ROtyur35B/4V145R7gzHTPaEk75z",
        "vmce9xdq": "U2FsdGVkX19tOdZAPNOwHbDyIkXNS56cnHbo8RvRLoor94LMKvGDgDeHhvNiueFmO+9LcSpdtYHPwzN+jEmtjFGI67hXXLTFLI+rbGQ2Qrs6/L/rHv6EPPOjfMSj+ulWC8WNoS5DpNJodqQkVxyGoGx8pUOvy86TotFAT3NhrmU=",
        "cmci9xde": "U2FsdGVkX1/O2dn1rMKJ4Bhtzgc9No7Fq/TFk3qeseYPRnGJnJxTQXxWmR6MVV2aPmIVjOKHLGFs9N1X+AmUDQ==",
        "pmck9xge": "U2FsdGVkX19k15AIr4qwkwla/f8ojzpPwjpgfmdajjc=",
        "assva6": "U2FsdGVkX187b6zOS/xgAOi1655Fa7jK3JMA4c4ExEk=",
        "assva5": "U2FsdGVkX1+WD3hCqLzWHvR1pmFsSbTRwCnoMv2aJ1S6Bv7e2OdFIDySJNP2BfxFttDIcaLtQrLBUvuf218K4A==",
        "impl": "www.ximalaya.com.login"
    }
    #define web's url
    url = 'https://www.ximalaya.com/revision/category/v2/albums'
    for page in range(1, pages + 1):
        # define params
        params = {
            "pageNum": page,
            "pageSize": "56",
            "sort": "1"
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)