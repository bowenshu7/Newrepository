"""
抓取天气网里长沙的最近 7 天的天气信息
"""
import requests
from lxml import etree

# 定义请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

# 定义cookie字典
cookies = {
    "sessionId": "uniqueSessionIdValue",
    "userNewsPort0": "1",
    "f_city": "%E5%B2%B3%E9%BA%93%7C101250109%7C",
    "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b": "1776157339,1776242178,1776242299",
    "Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b": "1776242299",
    "HMACCOUNT": "D95B324C32F62368"
}

# 定义请求的网址
url = "https://www.weather.com.cn/weather/101250101.shtml"

# 发起网络请求获取响应
response = requests.get(url, headers=headers, cookies=cookies)

# 指定解码字符集
response.encoding = 'utf-8'

# 转换成树形结构
html_tree = etree.HTML(response.text)

# 筛选包含七天天气信息的节点
week_weather_list = html_tree.xpath('//ul[@class="t clearfix"]/li')
# print(len(week_weather_list), week_weather_list)

# 遍历出每天天气信息的节点
for weather in week_weather_list:
    # print(weather)
    # 从每天的天气节点中筛选出具体日期
    date = weather.xpath('./h1/text()')[0]
    print('天气日期：', date)

    # 筛选出当天的具体天气信息
    wea = weather.xpath('./p[@class="wea"]/text()')[0]
    print('天气情况：', wea)

    # 筛选出当天的气温信息
    tem1 = weather.xpath('./p[@class="tem"]/span/text()')[0]
    # print(tem1)
    tem3 = weather.xpath('./p[@class="tem"]/i/text()')[0]
    # print(tem3)
    tem_string = tem1 + '℃ -> ' + tem3
    print('气温变化：', tem_string)

    # 筛选风向信息
    win_list = weather.xpath('./p[@class="win"]/em/span/@title')
    win_string = ' -> '.join(win_list)
    print('风向变化：', win_string)

    # 筛选风力等级信息
    win_level = weather.xpath('./p[@class="win"]/i/text()')[0]
    print('风力等级：', win_level)

    # 间隔每天的天气
    print('=' * 75)
