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

# 定义cookie字典
cookies = {
    "SSCSum": "4",
    # 这个值有乱码，requests库使用cookie的时候是 latin-1 编码，这个编码不支持中文乱码
    # "NowDate": "Sun Apr 26 2026 16:24:25 GMT+0800 (ä¸­å›½æ ‡å‡†æ—¶é—´)",
    "name": "sinaAds",
    "post": "massage",
    "UOR": ",news.sina.com.cn,",
    "SINAGLOBAL": "116.128.254.95_1776673072.740059",
    "FSINAGLOBAL": "116.128.254.95_1776673072.740059",
    "Hm_lvt_90c40f528e0b2106bc03da5aadec190f": "1777183614",
    "ULV": "1777191865385:7:7:3::1777182102014",
    "Apache": "42.48.49.78_1777191865.586237"
}

# 定义请求的网址
url = "https://news.sina.com.cn/world/"

# 发起网络请求
response = requests.get(url, headers=headers, cookies=cookies)

# 指定字符集
response.encoding = 'utf-8'
# print(response.text)

# 转换成树形结构
html_tree = etree.HTML(response.text)

"""
目标节点的数据都放在这四个标签内部，所以需要同时定位到这个四个标签。
<div id="subShowContent1_news1">
<div id="subShowContent1_news2">
<div id="subShowContent1_news3">
<div id="subShowContent1_news4">
"""

# 使用 contains 方法来定位 id 包含 subShowContent1_news 内容的所有 div 标签
news_info_list = html_tree.xpath('//div[contains(@id,"subShowContent1_news")]/div')
# print(len(news_info_list), news_info_list)

# 使用 starts-with 方法来定位 id 以 subShowContent1_news 开头的所有 div 标签
# news_info_list = html_tree.xpath('//div[starts-with(@id,"subShowContent1_news")]/div')
# print(len(news_info_list), news_info_list)

# 遍历出每个节点
for news_info in news_info_list:
    # 从新闻节点中筛选出新闻标题
    news_title = news_info.xpath('./h2/a/text()')[0]
    print('新闻标题：', news_title)

    # 从新闻节点中筛选出新闻时间
    news_time = news_info.xpath('./div/div[@class="time"]/text()')[0]
    print('发布时间：', news_time)

    # 筛选出新闻页面的链接
    news_url = news_info.xpath('./h2/a/@href')[0]
    print('新闻链接：', news_url)

    # 打印分隔
    print('=' * 75)
