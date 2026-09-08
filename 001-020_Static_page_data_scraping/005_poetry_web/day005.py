"""
抓取古诗文网站的诗词数据
"""
import requests
from lxml import etree

page_num = int(input('请输入抓取的页数：'))

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
    "login": "flase",
    "Hm_lvt_9007fab6814e892d3020a64454da5a55": "1776667255,1776674039",
    "Hm_lpvt_9007fab6814e892d3020a64454da5a55": "1776674039",
    "HMACCOUNT": "D95B324C32F62368"
}

for page in range(1, page_num + 1):

    # 定义首页的请求的网址
    url = "https://www.gushiwen.cn/shiwens/default.aspx"

    # 如果是抓取第一页数据就使用首页的网址
    if page == 1:
        page_url = url
    # 如果是后面的页数内容，就对网址进行格式化
    else:
        page_url = url + f"?page={page}&tstr=&astr=&cstr=&xstr="
    # print(page_url)

    # 发起网络请求获取数据
    response = requests.get(page_url, headers=headers, cookies=cookies)
    # print(response.text)

    # 转换成树形结构
    html_tree = etree.HTML(response.text)

    # 筛选包含所有诗歌信息的节点
    poem_data_list = html_tree.xpath('//div[@id="leftZhankai"]/div[@class="sons"]/div[@class="cont"]')
    # print(len(poem_data_list), poem_data_list)

    # 遍历出每首诗歌的节点信息
    for poem_data in poem_data_list:
        # print(poem_data)

        # 从节点标签中筛选出诗歌标题
        poem_title = poem_data.xpath('.//b/text()')

        # 判断筛选的值是否存在，如果不存在就指定一个标题
        poem_title = poem_title[0] if poem_title else '未知标题'
        print('诗歌标题：', poem_title)

        # 从节点标签中筛选出作者信息
        author_info_list = poem_data.xpath('.//p[@class="source"]/a/text()')
        # print(author_info_list)

        # 判断筛选结果是否存在
        if author_info_list:
            # 将列表转换成字符串
            poem_author_info = ''.join(author_info_list).strip()

        else:
            poem_author_info = '未知作者'

        print('作者信息：', poem_author_info)

        # 筛选诗歌文本内容
        poem_data_list = poem_data.xpath('.//div[@class="contson"]//text()')
        # print(poem_data_list)

        # 将列表转换成字符串，并使用换行符进行分隔多个元素
        print('诗歌内容：', '\n'.join(poem_data_list))

        print('=' * 75)

    # 打印抓取完一页数据后的提示
    print(f'------------------------第{page}的数据抓取完毕------------------------')