#name: honor club image
#author: Bowen
#goal: to get the information about the image from the honor club
#date: 2026/9/19
#stage: finished

import requests
from jsonpath import jsonpath
import csv
import time
import json


def get_page_data(url, data_list):
    #get the response
    response = requests.post(url, headers=headers, cookies=cookies, params=params)

    #select  nodes
    element_list = json.loads(response.text)
    for element in element_list:
        #select subject
        subject = jsonpath(element,'$.subject')[0]
        print(subject)
        #select username
        username = jsonpath(element,'$.username')[0]
        print(username)
        #select views
        views = jsonpath(element,'$.views')[0]
        print(views)
        #select replies
        replies = jsonpath(element,'$.replies')[0]
        print(replies)
        #select image url
        img_url = jsonpath(element,'$.imgurl')[0]
        print(img_url)

        data_list.append([subject, username, views, replies, img_url])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["主题", "用户名", "浏览量", "回复数", "图片下载链接"])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #select headers
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-length": "0",
        "origin": "https://club.honor.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://club.honor.com/cn/handphoto-1.html",
        "sec-ch-ua": "\"Google Chrome\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    #select cookies
    cookies = {
        "variedData": "ui1jnZYYJZaMZYbOMMNNYMNJcdQMdJZYjTTmmTWGyTGXF2ynmCy4ByzxDzihkllwGyllyJ4zwysp1lBwlwjjlRI0UVIIQyBDlpxpm3UQxJUEIIAVx4VBAIJ9gNUYVJNgFFIUMIIIsUINRcIhMURUUUVUJAmyTTiTjEjTTTj02jHiHUGzmiWyQZMTUMNQJMtM4J9Jxb0MAJYMNMIZYMQJUQ8JIJUJVbUcARNMdMUNAy0xyCyylxyluljyyhlhkl0lzz2ymJszw05OyjyjyTCTxXyyzTyTxTkyyCzj4zo2yX3i0ijjlTtXvm5jlkyCs0mzyyF2l0MFEUEHDTjTkIbUYIcVJ0RIJ0MIJMNyGzmuTyCw3lTwT3TlTUMNMNaIMUdINMMNZMZZZ9RAJBaMJUJJXJYRLEMIMUOkNFZMMIQUNIJNMJZRMhMENEYhMdfMSJJbMJJYOaMMMJJbaJJMZMMZMMZMbNJZOTyCyzDTyTy2BjlTUTi22nBWw0pzUTlT2Sz2yklTl2zGxmwjzyrGyYQUIUQlIYwVJFIUN5hwIkRJUERAcIEE5FUEJUIJxIhVJAQINZIEUTiTTCTSTG2T3jj2TmkjGmzjimWj2jkUjTjWc2CnDT2CTiGTijTTGj2TiTCl2TkU2T2TCT2mWjjHjCTTjTjT02mizTCTjWjCG3D3TDz2D2JQMMOUJJMMJLNMJMZTTTGk02SETHXVTTTTDTcNMMJbMJMUJMMJJOYNNMJMTVJMTRJUJbJbRbMMbMaNYYZMQMQMMXJMJMdMMdRMYJRMYNMaIER0NUYAgUUIQIIV5hgMMdUIUMNMwlg8kNEywlyyyyDypyylEB45jly6XxlwulpzpDzGjwlxDypz21xhllyyvyYNQIMdNBMAahYMMhcZMJJlZZYUZRMUONc5XMQhQIMdKhOBcJYVYJv5yz1zly5wyyw1GmBvlyyz1l0yDyslhwEk1QiyWl2zTyCvT2ktTzDzG3WyjCXLklTwTjT1mx0wTlikj1D2klTySxTyTlTinyGoDfTETxm2ULIM9JIJ1aMQQJYY21BnlHljuTwCwV4Wm2wdMQMJIJJMRJUNVSkYVNUJhJQNcS8bJLUd5bIdJZZSIMEMMMUa1bEJUbxMERIJJaNJkYcNJMMbJQMMYZMaMbJLQJMNYQYNQJXdVJJYNJYMiuWx2pT1yljyj0TzT2TyWuCwGljwjwTyToG0z2TlSwGhjljlTyjMJbMMQNMMMdbNZdMSbcMTVMJMOSGmTWSWC2DmGCT2jTzzlsDy2yy5mswXsuyG05By2j0B2isyylwyyy4g5I9UIRyyrlpDf21dUgNI5IJEJV5IYIJU0MIVMIJUVdJQJIk8JVVJUQVNQ1BQFMNIFIIdj0XCXCzjjCjTXTT3imjkDDjjyZA%3D%3D",
        "a3ps_2132_saltkey": "z8vyYDbyfR365II9uXWU1uow5zUP7e3b4Tw7T8uUXTUzK3oRjQCjWBrUtg6vro%2FawbeWauHEB6F0iy%2BQK9fYVXw6fGF1dGhrZXl8OnxvcGVuc3NsXzJ8Onxb32KppxG7tg5xXBB8Onxj3H%2FVgDmiVLbQI93ItNV5",
        "a3ps_2132_lastvisit": "1789796684",
        "a3ps_2132_deviceid": "3b6c662805725df4ed47548f643a3044",
        "Hm_lvt_fafee4d6bab477a8a4fafbd5dfbd0d6e": "1789800285",
        "Hm_lpvt_fafee4d6bab477a8a4fafbd5dfbd0d6e": "1789800285",
        "HMACCOUNT": "876958FB013481E3",
        "a3ps_2132_lastact": "1789800295%09plugin.php%09"
    }
    #select web's url
    url = 'https://club.honor.com/cn/plugin.php'
    for page in range(pages):
        # select params
        params = {
            "id": "handphoto",
            "mod": "loadmore",
            "num": "50",
            "start": page*50
        }
        get_page_data(url, data_list)
        time.sleep(1)
    save_data_csv(data_list)