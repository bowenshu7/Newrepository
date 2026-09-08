"""
抓取csdn的博客信息
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
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

# 定义cookie信息
cookies = {
    "uuid_tt_dd": "10_19546108010-1775807685200-423630",
    "fid": "20_93490177947-1775807685506-027874",
    "c_ab_test": "1",
    "https_waf_cookie": "0fd28827-586b-4a5fc2a24b664c41b5c18670d7c95bcbff96",
    "dc_session_id": "10_1776510112186.603925",
    "bc_bot_session": "1776510112606f724944dcdb9d",
    "waf_captcha_marker": "2d83ad2828d25108f2ad43912be070b6721f604c732fb544c26f3364229eaa2e",
    "c_pref": "default",
    "c_ref": "default",
    "c_first_ref": "default",
    "c_first_page": "https%3A//blog.csdn.net/ityouknow%3Ftype%3Dblog",
    "c_dsid": "11_1776510112592.550195",
    "c_segment": "14",
    "c_page_id": "default",
    "log_Id_pv": "1",
    "popPageViewTimes": "1",
    "creative_btn_mp": "1",
    "dc_sid": "fea3566d9ead2785dfeb295553dda626",
    "hide_login": "1",
    "bc_bot_token": "1001776510112606f724944dcdb9d458bf7",
    "bc_bot_rules": "-",
    "bc_bot_score": "100",
    "bc_bot_fp": "1c96237a27613140074992d513bf66d4",
    "Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac": "1775807687,1776510113",
    "Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac": "1776510113",
    "HMACCOUNT": "D95B324C32F62368",
    "_clck": "mlorkc%5E2%5Eg5b%5E0%5E2291",
    "_clsk": "1mzgakx%5E1776510114855%5E1%5E1%5Eb.clarity.ms%2Fcollect",
    "CookieNameTimes": "3",
    "loginbox_strategy": "%7B%22blog-threeH-dialog-exp11tipShowTimes%22%3A1%2C%22blog-threeH-dialog-exp11%22%3A1776510112912%7D",
    "SESSION": "ed0eaf77-3034-4776-9047-47e8fbd768ef",
    "log_Id_view": "34",
    "log_Id_click": "2",
    "dc_tos": "tdos01"
}

# 定义请求的网址
url = "https://blog.csdn.net/ityouknow?type=blog"

# 发起网络请求
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)

# 转换成树形结构
html_tree = etree.HTML(response.text)

# 筛选出所有的博客信息的节点
blog_info_list = html_tree.xpath('//div[@class="mainContent"]/div/div/div/article')
# print(len(blog_info_list), blog_info_list)

# 遍历出每个节点的信息
for blog_info in blog_info_list:
    # print(blog_info)

    # 筛选出每篇博客的标题
    blog_title = blog_info.xpath('./a//h4/text()')[0]
    # blog_title = blog_info.xpath('./a/div/div/div/h4/text()')

    # 去除博客标题中的换行和空格
    blog_title = blog_title.replace('\n', '').replace(' ', '')
    print('博客标题：', blog_title)

    # 筛选博客文章的链接
    blog_url = blog_info.xpath('./a/@href')[0]
    print('博客链接：', blog_url)

    # 筛选出每篇博客的标题
    blog_content = blog_info.xpath('./a//div[@class="blog-list-content"]/text()')[0]
    print('博客简介：', blog_content)

    # 筛选文章是原创还是转载
    blog_tag = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[1]/text()')[0]
    # print(blog_tag)

    # 去除标记中的换行和空格
    blog_tag = blog_tag.replace('\n', '').replace(' ', '')
    # print('博客标记：', blog_tag)

    # 筛选博客的发布时间
    blog_release_date = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[2]/text()')[0]
    # print(blog_release_date)

    # 去除发布时间中的换行和空格
    blog_release_date = blog_release_date.replace('\n', '').replace(' ', '')
    # print('发布时间：', blog_release_date)

    # 筛选博客的阅读人数
    blog_vive_num = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[3]/span/text()')[0]
    # print(blog_vive_num)

    # 筛选博客的阅读文本
    blog_vive_text = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[3]/span/span/text()')[0]
    # print(blog_vive_text)

    # 筛选点赞的人数
    blog_like_num = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[4]/span/text()')[0]
    # print(blog_like_num)

    # 筛选点赞的文本
    blog_like_text = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[4]/span/span/text()')[0]
    # print(blog_like_text)

    # 筛选评论的人数
    blog_comment_num = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[5]/span/text()')[0]
    # print(blog_comment_num)

    # 筛选评论的文本
    blog_comment_text = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[5]/span/span/text()')[0]
    # print(blog_comment_text)

    # 筛选收藏的人数
    blog_like1_num = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[5]/span/text()')[0]
    # print(blog_like1_num)

    # 筛选收藏的文本
    blog_like1_text = blog_info.xpath('./a//div[@class="blog-list-footer-left"]/div[5]/span/span/text()')[0]
    # print(blog_like1_text)

    # 将具体信息格式化成一个字符串
    blog_info_data = f'【{blog_tag}】{blog_release_date}{blog_vive_num}{blog_vive_text}{blog_like_num}{blog_like_text}{blog_comment_num}{blog_comment_text}{blog_like1_num}{blog_like1_text}'
    print(blog_info_data)

    # 打印分隔
    print('=' * 75)
