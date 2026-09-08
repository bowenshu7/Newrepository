#name: HUAWEI phone comments
#author: Bowen
#goal: to get the comments about the HUAWEI Mate 80 from HUAWEI web
#date: 2026/9/8
#stage: going

import requests
from jsonpath import jsonpath
import csv


def get_page_data(url, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    #select nodes
    element_list = jsonpath(response.json(),'$..comments[*]')
    for element in element_list:
        #select username
        username = jsonpath(element,'$.userName')[0]
        print(username)
        #select creation time
        creationtime = jsonpath(element,'$.creationTime')[0]
        creationtime = creationtime[:-5]
        print(creationtime)
        #select IP location
        iplocation = jsonpath(element,'$.ipLocation')[0]
        print(iplocation)
        #select comment level
        commentlevel = jsonpath(element,'$.commentLevel')[0]
        print(commentlevel)
        #select score
        score = jsonpath(element,'$.score')[0]
        score = f'{score}星'
        print(score)
        #select content
        content = jsonpath(element,'$.content')[0]
        print(content)
        #select phone type
        sku = jsonpath(element,'$.skuAttrs')
        sku = sku[0] if sku else ''
        print(sku)
        #select images
        images = jsonpath(element,'$.images[*].large')
        images_url = '\n'.join(images) if images else ''
        print(images_url)
        #select replies
        replies = jsonpath(element,'$.replies[*].replyContent')
        replies = '\n'.join(replies) if replies else ''
        print(replies)
        #select likes
        likes = jsonpath(element,'$.likes')[0]
        print(likes)

        data_list.append([username,creationtime,iplocation,commentlevel,score,content,sku,images_url,replies,likes])

def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['用户名','评论时间','IP地址','评论等级','评分','内容','购买产品','产品图片','回复数','点赞数'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 3
    #define headers
    headers = {
        "Accept": "application/json",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-store",
        "Connection": "keep-alive",
        "Origin": "https://item.vmall.com",
        "Pragma": "no-cache",
        "Referer": "https://item.vmall.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "X-E2E-Trace": "e2eId=page#rn_product#1#4dba89abc9b307a7801d3fc10824b0c3;spanId=d8c5d3d2a1d6129005e61367d6528aba",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    #define cookies
    cookies = {
        "euid": "ff5d23859af2b30a40147639f90cea4cb05c85443b23b135",
        "perIdb": "401001097",
        "callAB": "1",
        "HWWAFSESTIME": "1788853982033",
        "HWWAFSESID": "fc27032b54dcd76a3bb",
        "recommendflag": "0",
        "showAds": "true",
        "deviceid": "87628ce4996d4945db987de9537078e3",
        "TID": "87628ce4996d4945db987de9537078e3",
        "cartId": "578b7c79b8804373a6f7e90c0e1293d5",
        "sdevid": "c824a56f6673d5cb3b3262f89a4b62c6652dd314",
        "referer": "https://item.vmall.com/product/comdetail/index.html?prdId=10086133363559&sbomCode=2601010586341",
        "BENSESSCC_TAG": "ff5d23859af2b30a40147639f90cea4cb05c85443b23b135",
        "device_data": "*2k48WHDnDhZwVWMQPMdA1VZ9mSZNJy5uxVOo60ED3vU4FJlZv2yxZNZZQRWZMeZdMgJ9AFUpyHMz4PTZJajDjSFmWmjTTT2FGjmzU4Bh0dyiTkMSPLWcUNMYEsRRIJgVx52mTH1MMWNbyMmq1y9mmmZmy1ThxlTVl11d4915NSLMMScNVdEYE44Z4EJo9ERuiaQJJc0mXmTX0TUjFSmTDTTXmJd1YkljSXlaeZaJWLOTk1IIdBBlYIyljXuNZTdZCU9Kwyh0auumtBNmmUMhYJ0Vxmx05JTUNZVMPTmY4hdEk0oBuvR43NcJTbT3WDVnymm3CiUV0DiWWEtVZE0ETGnadPcbbLJPS1Z4hYZYYlj3jnSYWUMUmm9SS5902GumuyCjmyw4lQZGJBBM1JeMPZUMMU2NZhRJUZkF9DwDVbPRZjTjV2j1jmmCFTiDZ1DjEdJNOSt8l01iEZU1xmmPQ2dm"
    }
    #define web's url
    url = 'https://openapi.vmall.com/rms/v1/comment/getCommentList'
    for page in range(1, pages + 1):
        #define params
        params = {
            "pid": "10086133363559",
            "extraType": "0",
            "pageSize": "10",
            "pageNum": f"{page}",
            "gbomCode": "",
            "systemTagIds": "",
            "sortType": "1",
            "showStatistics": "false",
            "isFold": "false"
        }
        get_page_data(url, data_list)
    save_data_csv(data_list)