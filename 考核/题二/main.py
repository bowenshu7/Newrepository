"""
地址：https://weibo.com/
需求：使用requests库在该平台，找评论超过100的任意动态，采集评论区的数据
采集字段：评论用户id+评论时间(需将时间戳转换为北京时间+评论内容+用户地点)
保存方式：将数据存储使用MongoDB 数据库中
"""

"""
思路:
1.打开网页查找抓取数据包类型，确定为json
2.测试是否存在某些反爬内容
3.分析数据结构，找到目标数据
4.筛选数据并处理数据
5.由于时间数据与需求不符，定义一个函数timetransformer()来处理时间
6.单页抓取完后，就包装成函数，进行多页抓取
多页抓取时发现下一页的参数为max_id,需在上一页数据中获取,因此函数新增返回值max_id,又发现第
一页的max_id可以为空,故不另处理
7.最后将结果保存到MongoDB数据库中
"""

import requests
import pymongo
from jsonpath import jsonpath
import time

def timetransformer(t):
    t = t.split(' ')
    new_t = f'{t[5]}年 '
    if t[1]=='Jan':
        new_t += '1月'
    elif t[1]=='Feb':
        new_t += '2月'
    elif t[1]=='Mar':
        new_t += '3月'
    elif t[1]=='Apr':
        new_t += '4月'
    elif t[1]=='May':
        new_t += '5月'
    elif t[1]=='Jun':
        new_t += '6月'
    elif t[1]=='Jul':
        new_t += '7月'
    elif t[1]=='Aug':
        new_t += '8月'
    elif t[1]=='Sep':
        new_t += '9月'
    elif t[1]=='Oct':
        new_t += '10月'
    elif t[1]=='Nov':
        new_t += '11月'
    elif t[1]=='Dec':
        new_t += '12月'
    new_t += f'{t[2]}日'
    new_t += f' {t[3]} '
    if t[0]=='Mon':
        new_t += '周一'
    elif t[0]=='Tue':
        new_t += '周二'
    elif t[0]=='Wed':
        new_t += '周三'
    elif t[0]=='Thu':
        new_t += '周四'
    elif t[0]=='Fri':
        new_t += '周五'
    elif t[0]=='Sat':
        new_t += '周六'
    elif t[0]=='Sun':
        new_t += '周日'
    return new_t

def get_page_data(url, params, data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    #select nodes
    elements = jsonpath(response.json(), '$.data[*]')
    for element in elements:
        #select id
        userid = jsonpath(element,'$.user.id')[0]
        print(userid)
        #select username
        username = jsonpath(element,'$.user.screen_name')[0]
        print(username)
        #select time
        created_at = jsonpath(element,'$.created_at')[0]
        created_at = timetransformer(created_at)
        print(created_at)
        #select content
        content = jsonpath(element,'$.text_raw')[0]
        print(content)
        #select source
        source = jsonpath(element,'$.source')[0]
        print(source)


        print('='*75)

        data_list.append({'用户ID':userid, '用户名':username, '评论及时间':created_at+'\n'+content+'\n'+source})
    #select max_id
    max_id = jsonpath(response.json(),'$.max_id')[0]
    return max_id

if __name__ == '__main__':
    pages = int(input('Enter number of pages: '))
    data_list = []
    max_id = ''
    #define headers
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "client-version": "v1.1.250",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://weibo.com/1705586121/RkZ62ia1d?from=feed",
        "sec-ch-ua": "\"Chromium\";v=\"154\", \"Google Chrome\";v=\"154\", \"Not A(Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "server-version": "v2026.09.22.3",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "ozCJMojIU1g116w_e29k7ofJ"
    }
    #define cookies
    cookies = {
        "XSRF-TOKEN": "ozCJMojIU1g116w_e29k7ofJ",
        "SCF": "AhdP-9UmZUCQnGnWmJtaTFBfUne_vltsIs3gy7KH8M888Qwwx4SZ-D9wsIVSTyT1vrCzOlV6AWdMhh1C_01wU-k.",
        "SUB": "_2A25Hx3cJDeRhGe5N6lYR8yzPzDSIHXVkvfbBrDV8PUNbmtAYLRTkkW9NdO40Cz2bNrignPxAYbnBbNHVYSrnAjSk",
        "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EpzZiSl52SAhOHfU9zPyQ5NHD95QRe02XeheEe0MRWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zN1hepSh50eoeN15tt",
        "ALF": "02_1793758297",
        "WBPSESS": "ipLVx0Hqtp4IwvxqxwLtt_n0_gtMEKnPPTV6oOb4WZUv7H79S0A3qiNHvR3MLftBpV314Dx2xcLFor4fg1z1rDTvslEeMIp6lI5PpIgK7YiCEjvvaUTFVXu1IR0DKqpY-D7_Ntj3c-g5ewxRIA-arw=="
    }
    #define url
    url = 'https://weibo.com/ajax/statuses/buildComments'
    for page in range(1, pages + 1):
        #define params
        params = {
            "is_reload": "1",
            "id": "5350014184328419",
            "is_show_bulletin": "2",
            "is_mix": "0",
            "max_id": max_id,
            "count": page*10,
            "uid": "1705586121",
            "fetch_level": "0",
            "locale": "zh-CN"
        }
        max_id = get_page_data(url, params, data_list)
        #sleep 1 sec
        time.sleep(1)
    #create connection
    Client = pymongo.MongoClient()
    #assign database
    db = Client['examination']
    #assign collection
    collection = db['weibo']
    #insert data
    collection.insert_many(data_list)
    #close client
    Client.close()