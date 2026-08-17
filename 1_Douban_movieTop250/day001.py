"""
抓取目标：豆瓣电影榜单 Top250的电影数据
并使用xpath筛选出电影相关信息
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

# 定义cookie字典
cookies = {
    "ll": "\"118267\"",
    "bid": "XZOrSx7oBfY",
    "_pk_id.100001.4cf6": "2e86c609c3a54373.1775736939.",
    "__utmz": "223695111.1775736939.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    "__yadk_uid": "VgcYRQb7kvoaCERamo5I6mFOyFDwviNq",
    "_vwo_uuid_v2": "D1241AE10A39FB0C9FDD8AB6D5E875AD5|e0ef13ae9f49c8d5328faaaad0b2072d",
    "_pk_ref.100001.4cf6": "%5B%22%22%2C%22%22%2C1776155065%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DY8qyw947dvsqvYfZ51FQSAIxslDFD5X4WkNWMiyiKHbT2MgeCo8retuatkqRLAvg%26wd%3D%26eqid%3Db207efb60027ab7d0000000569d79863%22%5D",
    "_pk_ses.100001.4cf6": "1",
    "ap_v": "0,6.0",
    "__utma": "223695111.1302342815.1775736939.1775746047.1776155065.3",
    "__utmb": "223695111.0.10.1776155065",
    "__utmc": "223695111"
}

# 定义请求的网址
url = "https://movie.douban.com/top250"

# 发起网络请求并获取响应
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)

# 转换成树形结构
html_tree = etree.HTML(response.text)

# 筛选出包含每部电影详细信息的节点数据
element_list = html_tree.xpath('//ol[@class="grid_view"]/li/div/div[@class="info"]')
# print(len(element_list), element_list)

# 使用循环遍历出每部电影的节点标签
for element in element_list:
    # print(element)
    # 从每部电影的节点标签中再次筛选出目标数据
    movie_title_list = element.xpath('./div[@class="hd"]/a/span/text()')
    # print(movie_title_list)
    # 将电影名称列表转换成字符串
    movie_title = ''.join(movie_title_list)
    print('电影名称：', movie_title)

    # 筛选电影的详情页网址
    movie_url = element.xpath('./div[@class="hd"]/a/@href')[0]
    print('电影主页：', movie_url)

    # 筛选导演和演员名单信息
    movie_actors_list = element.xpath('./div[@class="bd"]/p[1]/text()')
    # print(movie_actors_list)
    # 将电影演员信息列表转换成字符串
    movie_actors = ''.join(movie_actors_list)

    # 对字符串中的多余信息进行处理
    movie_actors = movie_actors.replace('\n', '').replace(' ', '')
    print('演员名单：', movie_actors)

    # 筛选电影的评分信息
    movie_score = element.xpath('./div[@class="bd"]/div/span[2]/text()')[0]
    print('电影评分：', movie_score)

    # 筛选电影的评价人数
    movie_score_count = element.xpath('./div[@class="bd"]/div/span[4]/text()')[0]
    print('评价人数：', movie_score_count)

    # 筛选出电影的经典评论
    movie_comment = element.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')[0]
    print('经典评论：', movie_comment)

    # 打印间隔
    print('=' * 75)
