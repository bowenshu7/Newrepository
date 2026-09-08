"""
抓取安居客网站中的租房信息
"""
import requests
from lxml import etree

# 定义请求头
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

# 定义cookie
cookies = {
    "ctid": "27",
    "cmctid": "414",
    "aQQ_ajkguid": "5CFE1CFE-C47E-5B02-6A2C-C4D7CDA95EDA",
    "id58": "dqCe5GnYpCu5jnR9BUsGAg==",
    "wmda_visited_projects": "%3B6289197098934",
    "xxzlclientid": "c40ac363-a9be-4fd1-a5ad-1775805485611",
    "wmda_uuid": "3750ed3624ea61199e9ffb22102598eb",
    "wmda_new_uuid": "1",
    "xxzlxxid": "pfmxlLqpngO/gy75MxgWLV0Xa88EO+0FntzVufT/r1rAKK01iVMCZCAz2vRNaSFn3f9Q",
    "wmda_session_id_6289197098934": "1776327214429-633d3ba4-7a88-5c20",
    "lps": "https%3A%2F%2Fcs.zu.anjuke.com%2F%7C",
    "xxzlbbid": "pfmbRKuhADG7XS3FgZPAr2kLScpAfD68DE+lvpEbhJ3T6xJxKHo01sd04lVTgoHitxsuxtr8AiFppw0OhQuPP9qlEVFUF3hWHOy6tEN4hl4OdFtARTK06oht4H1NxaeqY0o5rBx8H8ExNzc2MzI3NjcwMzA0ODM3_1",
    "f_session": "d05fc49a36b6b9d077ed95d3cb27554e-2"
}

# 定义请求的网址
url = "https://cs.zu.anjuke.com/"

# 发起请求获取响应
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)

# 转换成树形结构
html_tree = etree.HTML(response.text)

# 筛选目标数据
data_list = html_tree.xpath('//div[@class="list-content"]/div[@class="zu-itemmod clearfix"]')
# print(len(data_list), data_list)

# 遍历出每个节点的信息
for data in data_list:
    # print(data)

    # 筛选租房的标题信息
    home_title = data.xpath('./div[@class="zu-info"]/h3/a/b/text()')[0]
    print('租房标题：', home_title)

    # 筛选租房的介绍信息
    home_info1 = data.xpath('./div[@class="zu-info"]/p[@class="details-item tag"]/text()')[1:5]
    # print(home_info1)

    home_info2 = data.xpath('./div[@class="zu-info"]/p[@class="details-item tag"]/b/text()')
    # print(home_info2)

    # 房屋信息的字符串格式化
    home_info = f'{home_info2[0]}{home_info1[0]}{home_info2[1]}{home_info1[1]} | {home_info2[2]}{home_info1[2]} | {home_info1[3].replace(" ", "")}'
    print('租房介绍：', home_info)

    # 筛选房屋的地址信息
    home_address1 = data.xpath('./div[@class="zu-info"]/address/a/text()')[0]
    # print(home_address1)

    home_address2 = data.xpath('./div[@class="zu-info"]/address/text()')[1:4]
    # print(home_address2)

    home_address3 = home_address2[0].replace("\n", "").replace(' ', '')

    home_address4 = home_address2[2].replace(' ', '')

    # 房租地址的字符串格式化
    home_address = f'{home_address1}{home_address3} | {home_address2[1]}| {home_address4}'
    print('房屋地址：', home_address)

    # 筛选房租优势
    home_pros_list = data.xpath('./div[@class="zu-info"]/p[@class="details-item bot-tag"]/span/text()')
    # print(home_pros_list)

    # 将列表转换成字符串
    home_pros = ' | '.join(home_pros_list)
    print('房屋优点：', home_pros)

    # 筛选房租租金
    home_rent1 = data.xpath('./div[@class="zu-side"]/strong/text()')[0]
    # print(home_rent1)
    home_rent2 = data.xpath('./div[@class="zu-side"]/span/text()')[0]
    # print(home_rent2)

    home_rent = home_rent1 + home_rent2
    print('房屋租金：', home_rent)

    # 打印间隔
    print('=' * 75)
